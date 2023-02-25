import requests  # 모듈들 불러오기
import bs4
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import re

import json

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIATMPH7BYJY6WQWIE6',aws_secret_access_key = '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')

url = "https://career.programmers.co.kr/job"

driver = webdriver.Chrome()

dic = {}

driver.get(url)

num = 1
namenum = 1
page = 3


while True :
    element = driver.find_element(By.XPATH, f'//*[@id="list-positions-wrapper"]/ul/li[{num}]')
    element.click()
    time.sleep(1)

    Id = driver.current_url
    Idd = Id.maketrans({
        '/': '',  # 왼쪽은 치환하고 싶은 문자, 오른쪽은 새로운 문자
    })
    Iddd = Id.translate(Idd)
    company_name_text = driver.find_element(By.XPATH, '//*[@id="career-app-legacy"]/div/div[1]/div[1]/header/div/div[2]/h4/a').text
    company_title_text = driver.find_element(By.XPATH, '//*[@id="career-app-legacy"]/div/div[1]/div[1]/header/div/div[2]/div').text


    #회사 이름,타이틀 딕셔너리에 넣기
    Rid = int(re.sub(r"[a-z]", "", Iddd)[5:])
    dic['id'] = Rid
    dic['회사이름'] = company_name_text
    dic['회사타이틀'] = company_title_text 

    source = driver.page_source
    bs = bs4.BeautifulSoup(source,'lxml')
    entire = bs.find('div', class_ = 'yO7TZRtCO7sznD0Csuw_').next_sibling.next_sibling
    dic['본문'] = str(entire)

    for i in range(1,11):
        try :
            DetailInfo_title_text = driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/section/div/div[1]/div[{i}]/div[1]').text

            DetailInfo_cont_text = driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/section/div/div[1]/div[{i}]/div[2]').text

            dic[DetailInfo_title_text ] =  DetailInfo_cont_text 
        except NoSuchElementException:
            pass
    stacks = ''
    for i in range(1,21) :
        try :
            stack = driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[2]/section/ul/li[{i}]').text
            stacks = stacks + stack + ','
        except NoSuchElementException :
            pass
    
    dic['기술스택'] = stacks

    driver.back()
    
    time.sleep(1)

    file_path = f"C:/Users/홍성학/Desktop/AWPS/awps-project/AWPS CRAWLLING/data/programmers/{str(Rid)+company_name_text}(programmers).json"
    with open(file_path,'w',encoding="utf-8") as f :
        json.dump(dic,f,indent=2,ensure_ascii = False)
    
    print(dic)

    table = dynamodb.Table('programmers')
    table.put_item(Item=dic)

    if (num%20 == 0) :
        driver.find_element(By.XPATH, f'//*[@id="tab_position"]/div[3]/ul/li[{page}]').click()
        time.sleep(1)
        page += 1
        num = 0
    
    
    namenum += 1
    num += 1
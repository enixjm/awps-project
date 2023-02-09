import requests  # 모듈들 불러오기
import bs4
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import random

import json

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIAUP5VXNX47G7WBK7T',aws_secret_access_key = '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')


url = "https://www.jumpit.co.kr/positions"


driver = webdriver.Chrome()

dic = {}

driver.get(url)

def dict_to_item(raw):
    if type(raw) is dict:
        resp = {}
        for k,v in raw.items():
            resp[k]

            # if type(v) is str:
            #     resp[k] = {
            #         'S': v
            #     }
            # elif type(v) is int:
            #     resp[k] = {
            #         'I': str(v)
            #     }
            # elif type(v) is dict:
            #     resp[k] = {
            #         'M': dict_to_item(v)
            #     }
            # elif type(v) is list:
            #     resp[k] = []
            #     for i in v:
            #         resp[k].append(dict_to_item(i))
                    
        return resp
    elif type(raw) is str:
        return {
            'S': raw
        }
    elif type(raw) is int:
        return {
            'I': str(raw)
        }

# random.uniform(1, 2)

num = 1

while True:
    # if num%16 == 0 :
    #     driver.execute_script("document.body.scrollHeight")
    time.sleep(1)
    items = driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div/section/div[{num}]')
    # time.sleep(0.5)
    items.click()
    time.sleep(1)

    #회사 정보 긁어오기
    company_name_text = driver.find_element(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').text   #회사이름 텍스트
    company_name_tag1 = '<' + driver.find_element(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').tag_name + '>' #회사이름 태그
    company_name_tag2 = '</' + driver.find_element(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').tag_name + '>' #회사이름 태그

    company_title_cont = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').text #회사타이틀 텍스트
    company_title_tag1 = '<' + driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').tag_name + '>' #회사타이틀 태그
    company_title_tag2 = '</' + driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').tag_name + '>' #회사타이틀 태그

    #딕셔너리에 넣기
    dic['회사이름'] = company_name_tag1 + company_name_text + company_name_tag2
    dic['회사제목'] = company_title_tag1 + company_title_cont + company_title_tag2
    
    # 정보 전체 다 긁어오기
    

    
    source = driver.page_source
    bs = bs4.BeautifulSoup(source,'lxml')
    entire = bs.find('section', class_ = 'styles_position_info__96hrw styles_skeleton__hl_0i')
    dic['본문'] = str(entire)
    

    for i in range(1,11) :
        try :
            DetailInfo_title = driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dt').text
            # DetailInfo_title_tag1 = '<' +driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dt').tag_name+ '>'
            # DetailInfo_title_tag2 = '</' +driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dt').tag_name+ '>'
            DetailInfo_cont = driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dd').text
            # DetailInfo_cont_tag1 = '<' +driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dd').tag_name+ '>'
            # DetailInfo_cont_tag2 = '</' +driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dd').tag_name+ '>'
            dic[DetailInfo_title ] =DetailInfo_cont 
        except NoSuchElementException:
            pass
    

    try :
        service_intro = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/div/section[4]/div[2]/pre').text
        dic['기업/서비스 소개'] = service_intro
    except NoSuchElementException:
        pass

    try :
        employ_price = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/aside/div[1]/span').text
        dic['취업축하금'] = employ_price
    except NoSuchElementException :
        pass

    file_path = f"C:/Users/홍성학/Desktop/AWPS/awps-project/AWPS CRAWLLING/jumpit/{str(num)+company_name_text}(jumpit).json"
    with open(file_path,'w',encoding="utf-8") as f :
        json.dump(dic,f,indent=2,ensure_ascii = False)

    table = dynamodb.Table('jumpit')
    print(dic)
    table.put_item(Item=dic)


    driver.back()

    # if (num%16 == 0) :
    #     time.sleep(1)
    #     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #     time.sleep(1)
    #     print("asdfasdf")
    
    if (num%16 == 0) :
        for i in range(1,5) :
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(1)


    time.sleep(1)
    # print(dic)
    num += 1
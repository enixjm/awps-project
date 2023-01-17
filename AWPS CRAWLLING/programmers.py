import requests  # 모듈들 불러오기
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

import random

import json

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

    company_name_text = driver.find_element(By.XPATH, '//*[@id="career-app-legacy"]/div/div[1]/div[1]/header/div/div[2]/h4/a').text
    company_name_tag1 = '<' + driver.find_element(By.XPATH, '//*[@id="career-app-legacy"]/div/div[1]/div[1]/header/div/div[2]/h4/a').tag_name + '>'
    company_name_tag2 = '</' + driver.find_element(By.XPATH, '//*[@id="career-app-legacy"]/div/div[1]/div[1]/header/div/div[2]/h4/a').tag_name + '>'
    company_title_text = driver.find_element(By.XPATH, '//*[@id="career-app-legacy"]/div/div[1]/div[1]/header/div/div[2]/div').text
    company_title_tag1 = '<' + driver.find_element(By.XPATH, '//*[@id="career-app-legacy"]/div/div[1]/div[1]/header/div/div[2]/div').tag_name + '>'
    company_title_tag2 = '</' + driver.find_element(By.XPATH, '//*[@id="career-app-legacy"]/div/div[1]/div[1]/header/div/div[2]/div').tag_name + '>'

    #회사 이름,타이틀 딕셔너리에 넣기
    dic['회사이름'] = company_name_tag1 + company_name_text + company_name_tag2
    dic['회사타이틀'] = company_title_tag1 + company_title_text + company_title_tag2

    for i in range(1,11) :
        try :
            info_title_text = driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[{i}]/h5').text # 업무소개, 자격조건, 우대사항, 개발팀&환경 등등
            info_title_tag1 = '<' + driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[{i}]/h5').tag_name + '>'
            info_title_tag2 = '</' + driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[{i}]/h5').tag_name + '>' #위에 태그
            try : #개발팀&환경 차례가 오면 세부정보 XPATH가 달라져서 예외처리 한번 더 함
                info_phrase_text = driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[{i}]/div/div/ul').text #위에 세부정보
                info_phrase_tag1 = '<' + driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[{i}]/div/div/ul').tag_name + '>'
                info_phrase_tag2 = '</' + driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[{i}]/div/div/ul').tag_name + '>'
                dic[info_title_tag1 + info_title_text + info_title_tag2] = info_phrase_tag1 + info_phrase_text + info_phrase_tag2
            except NoSuchElementException:
                for j in range(1,11) :
                    info_phrase_title_text = driver.find_element(By.XPATH,f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[5]/table/tbody/tr[{j}]/td[1]').text
                    info_phrase_title_tag1 ='<' + driver.find_element(By.XPATH,f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[5]/table/tbody/tr[{j}]/td[1]').tag_name + '>'
                    info_phrase_title_tag2 ='</' +  driver.find_element(By.XPATH,f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[5]/table/tbody/tr[{j}]/td[1]').tag_name + '>'
                    info_phrase_cont_text = driver.find_element(By.XPATH,f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[5]/table/tbody/tr[{j}]/td[2]').text
                    info_phrase_cont_tag1 = '<' + driver.find_element(By.XPATH,f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[5]/table/tbody/tr[{j}]/td[2]').tag_name + '>'
                    info_phrase_cont_tag2 = '</' + driver.find_element(By.XPATH,f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/div[3]/section[5]/table/tbody/tr[{j}]/td[2]').tag_name + '>'
                    # info_phrase_value = info_phrase_title_tag1 + info_phrase_title_text + info_phrase_title_tag2 + info_phrase_cont_tag1 + info_phrase_cont_text + info_phrase_cont_tag2
                    dic[info_phrase_title_tag1 + info_phrase_title_text + info_phrase_title_tag2] = info_phrase_cont_tag1 + info_phrase_cont_text + info_phrase_cont_tag2
        except NoSuchElementException :
            continue

    for i in range(1,11):
        try :
            DetailInfo_title_text = driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/section/div/div[1]/div[{i}]/div[1]').text
            DetailInfo_title_tag1 = '<' + driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/section/div/div[1]/div[{i}]/div[1]').tag_name + '>'
            DetailInfo_title_tag2 = '</' + driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/section/div/div[1]/div[{i}]/div[1]').tag_name + '>'
            DetailInfo_cont_text = driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/section/div/div[1]/div[{i}]/div[2]').text
            DetailInfo_cont_tag1 = '<' + driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/section/div/div[1]/div[{i}]/div[2]').tag_name + '>'
            DetailInfo_cont_tag2 = '</' + driver.find_element(By.XPATH, f'//*[@id="career-app-legacy"]/div/div[1]/div[1]/section/div/div[1]/div[{i}]/div[2]').tag_name + '>'
            dic[DetailInfo_title_tag1 + DetailInfo_title_text + DetailInfo_title_tag2] = DetailInfo_cont_tag1 + DetailInfo_cont_text + DetailInfo_cont_tag2
        except NoSuchElementException:
            pass
    

    driver.back()
    
    time.sleep(1)

    file_path = f"C:/Users/홍성학/Desktop/AWPS/awps-project/AWPS CRAWLLING/programmers/{str(namenum)+company_name_text}(programmers).json"
    with open(file_path,'w',encoding="utf-8") as f :
        json.dump(dic,f,indent=2,ensure_ascii = False)
    

    if (num%20 == 0) :
        driver.find_element(By.XPATH, f'//*[@id="tab_position"]/div[3]/ul/li[{page}]').click()
        time.sleep(1)
        page += 1
        num = 0
    
    
    namenum += 1
    num += 1
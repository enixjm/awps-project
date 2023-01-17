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


url = "https://www.jumpit.co.kr/positions"


driver = webdriver.Chrome()

dic = {}

driver.get(url)


scroll_location = driver.execute_script("return document.body.scrollHeight")

num = 1

while True:
    time.sleep(0.5)
    # if num%16 == 0 :
    #     driver.execute_script("document.body.scrollHeight")
    
    
    items = driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div/section/div[{num}]')
    action = ActionChains(driver)
    action.move_to_element(items).perform()

    items.click()
    time.sleep(0.5)

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
    for i in range(1,11) :
        try:
            info_title = driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[2]/dl[{i}]/dt').text
            info_title_tag1 ='<' +  driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[2]/dl[{i}]/dt').tag_name+ '>'
            info_title_tag2 ='</' +  driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[2]/dl[{i}]/dt').tag_name+ '>'
            info_phrase = driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[2]/dl[{i}]/dd/pre').text
            info_phrase_tag1 = '<' + driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[2]/dl[{i}]/dd/pre').tag_name+ '>'
            info_phrase_tag2 = '</' + driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[2]/dl[{i}]/dd/pre').tag_name+ '>'
            dic[info_title_tag1 + info_title + info_title_tag2] = info_phrase_tag1 + info_phrase + info_phrase_tag2
        
        except NoSuchElementException :
            pass

    for i in range(1,11) :
        try :
            DetailInfo_title = driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dt').text
            DetailInfo_title_tag1 = '<' +driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dt').tag_name+ '>'
            DetailInfo_title_tag2 = '</' +driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dt').tag_name+ '>'
            DetailInfo_cont = driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dd').text
            DetailInfo_cont_tag1 = '<' +driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dd').tag_name+ '>'
            DetailInfo_cont_tag2 = '</' +driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dd').tag_name+ '>'
            dic[DetailInfo_title_tag1 + DetailInfo_title + DetailInfo_title_tag2] = DetailInfo_cont_tag1 + DetailInfo_cont + DetailInfo_cont_tag2
        except NoSuchElementException:
            pass

    file_path = f"C:/Users/홍성학/Desktop/AWPS/awps-project/AWPS CRAWLLING/jumpit/{str(num)+company_name_text}(jumpit).json"
    with open(file_path,'w',encoding="utf-8") as f :
        json.dump(dic,f,indent=2,ensure_ascii = False)


    driver.back()
    time.sleep(0.5)
    # print(dic)
    num += 1
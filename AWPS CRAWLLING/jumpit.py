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
    company_name_cont = driver.find_element(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').text
    company_name_tag = '<' + driver.find_element(By.XPATH,'//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').tag_name + '>'
    company_title_cont = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').text
    company_title_tag = '<' + driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').tag_name + '>'
    
    dic['회사이름'] = company_name_tag + company_name_cont
    dic['회사제목'] = company_title_cont



    driver.back()
    time.sleep(0.5)
    print(dic)
    num += 1
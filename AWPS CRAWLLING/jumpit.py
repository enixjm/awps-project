import requests  # 모듈들 불러오기
import bs4
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import re

import json

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIATMPH7BYJY6WQWIE6',aws_secret_access_key = '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')


url = "https://www.jumpit.co.kr/positions"


driver = webdriver.Edge(executable_path='C:/Users/jake/AppData/Local/Programs/Python/MicrosoftWebDriver.exe')


driver.get(url)

# random.uniform(1, 2)

num = 1
um = 0

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        while True:
            dic = {}

            # if num%16 == 0 :
            #     driver.execute_script("document.body.scrollHeight")
            try:
                items = driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div/section/div[{num}]')
                items.click()
            except ElementNotInteractableException:
                print("공습경보!공습경보!공습경보!공습경보!공습경보!공습경보!공습경보!공습경보!공습경보!공습경보!공습경보!공습경보!")
                for i in range(0, 5):
                    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                items = driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div/section/div[{num}]')
                items.click()

            time.sleep(1)

            # 회사 정보 긁어오기
            Id = driver.current_url
            Idd = Id.maketrans({
                '/': '',  # 왼쪽은 치환하고 싶은 문자, 오른쪽은 새로운 문자
            })
            Iddd = Id.translate(Idd)
            company_name_text = driver.find_element(By.XPATH,
                                                    '//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').text  # 회사이름 텍스트
            company_name_tag1 = '<' + driver.find_element(By.XPATH,
                                                          '//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').tag_name + '>'  # 회사이름 태그
            company_name_tag2 = '</' + driver.find_element(By.XPATH,
                                                           '//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').tag_name + '>'  # 회사이름 태그

            company_title_cont = driver.find_element(By.XPATH,
                                                     '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').text  # 회사타이틀 텍스트
            company_title_tag1 = '<' + driver.find_element(By.XPATH,
                                                           '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').tag_name + '>'  # 회사타이틀 태그
            company_title_tag2 = '</' + driver.find_element(By.XPATH,
                                                            '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').tag_name + '>'  # 회사타이틀 태그

            # 딕셔너리에 넣기
            Rid = int(re.sub(r"[a-z]", "", Iddd)[4:])
            dic['id'] = Rid
            dic['회사이름'] = company_name_tag1 + company_name_text + company_name_tag2
            dic['회사제목'] = company_title_tag1 + company_title_cont + company_title_tag2

            # 정보 전체 다 긁어오기

            source = driver.page_source
            bs = bs4.BeautifulSoup(source, 'lxml')
            entire = bs.find('section', class_='position_info')
            dic['본문'] = str(entire)

            for i in range(1, 11):
                try:
                    DetailInfo_title = driver.find_element(By.XPATH,
                                                           f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dt').text

                    DetailInfo_cont = driver.find_element(By.XPATH,
                                                          f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dd').text

                    dic[DetailInfo_title] = DetailInfo_cont
                except NoSuchElementException:
                    pass

            # 기술스택
            stacks = ''
            for i in range(1, 20):
                try:
                    stack = driver.find_element(By.XPATH,
                                                f'//*[@id="root"]/main/div/div[2]/div/section[2]/dl[1]/dd/pre/div[{i}]').text
                    stacks = stacks + stack + ','
                except NoSuchElementException:
                    pass
            dic['기술스택'] = stacks

            try:
                service_intro = driver.find_element(By.XPATH,
                                                    '//*[@id="root"]/main/div/div[2]/div/section[4]/div[2]/pre').text
                dic['기업/서비스 소개'] = service_intro
            except NoSuchElementException:
                pass

            try:
                employ_price = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/aside/div[1]/span').text
                dic['취업축하금'] = employ_price
            except NoSuchElementException:
                pass

            print(dic)
            print(num)
            table = dynamodb.Table('jumpit')
            table.put_item(Item=dic)

            driver.back()

            # if (num%16 == 0) :
            #     for i in range(1,5) :
            #         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            #         time.sleep(1)
            # 이걸로 하면 300개까지는 되는데 메모리초과가 쉽게 걸림

            time.sleep(1)
            num += 1
    last_height = new_height




#주소 id 긁어오기

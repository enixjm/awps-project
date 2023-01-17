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

for i in range(100):  # 스크롤
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

# (random.randrange(5,11))/10
time.sleep(1)

scroll_location = driver.execute_script("return document.body.scrollHeight")

num = 1

while num <= 500:
    items = driver.find_element(By.XPATH, f'//*[@id="root"]/main/div/div/section/div[{num}]')
    items.click()
    time.sleep(1)

    title = driver.find_element(By.XPATH, f"//*[@id='root']/main/div/div[2]/div/section[1]/h1").text
    dic['<h1> 제목:'] = title
    name = driver.find_element(By.XPATH, f"//*[@id='root']/main/div/div[2]/div/section[1]/div/a").text
    dic['<a> 회사 이름:'] = name
    for num2 in range(10):
        try:
            options = driver.find_element(By.XPATH,
                                          f"//*[@id='root']/main/div/div[2]/div/section[2]/dl[{num2 + 1}]/dt").text
            pharse = driver.find_element(By.XPATH,
                                         f"//*[@id='root']/main/div/div[2]/div/section[2]/dl[{num2 + 1}]/dd/pre").text
            dic["<dt>" + options] = pharse
        except NoSuchElementException:
            pass
        num2 += 1
    for num2 in range(10):
        try:
            options = driver.find_element(By.XPATH,
                                          f"// *[ @ id = 'root'] / main / div / div[2] / div / section[3] / dl[{num2}] / dt").text
            pharse = driver.find_element(By.XPATH,
                                         f"// *[ @ id = 'root'] / main / div / div[2] / div / section[3] / dl[{num2}] / dd").text
            dic["<dl>" + options] = pharse
        except NoSuchElementException:
            pass
    time.sleep(1)

    driver.back()

    # driver.execute_script("window.scrollTo(0, 70)")

    time.sleep(1)
    # com_list.append(items.text)
    file_path = f"C:/Users/apnee/OneDrive/바탕 화면/physon/crawling/jumpit_raw_data/jumpit_{name + str(num)}.json"
    with open(file_path, 'w', encoding="utf-8") as f:
        json.dump(dic, f, indent=2, ensure_ascii=False)
    num += 1

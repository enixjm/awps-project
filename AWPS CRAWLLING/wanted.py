import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import random
import json

url = "https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&locations=all"

driver = webdriver.Chrome()

driver.get(url)

time.sleep(1)

dic = {}

num = 1

while True:
    if num%20 == 0:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
    items = driver.find_element(By.XPATH, f"//*[@id='__next']/div[3]/div/div/div[4]/ul/li[{num}]/div/a/header")
    driver.execute_script("arguments[0].click();", items)
    time.sleep(1)
    title = driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div[1]/div[1]/div/section[2]/h2").text
    title_tag = driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div[1]/div[1]/div/section[2]/h2").tag_name
    company = driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/div[1]/div[1]/div/section[2]/div[1]/h6/a").text
    company_tag = driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/div[1]/div[1]/div/section[2]/div[1]/h6/a").tag_name
    des = driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[1]/span").text
    des_tag = driver.find_element(By.XPATH, f"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[1]/span").tag_name
    dic['회사제목'] = title_tag + title
    dic['회사이름'] = company_tag + company
    dic["회사설명"] = des_tag + des

    for x in range(2,11):
        try:
            top_title  = driver.find_element(By.XPATH, f"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[1]/h6[{x-1}]").text
            if top_title == "기술스택 ・ 툴":
                phrase = driver.find_element(By.XPATH, f"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[{x}]/div").text
                phrase_tag = driver.find_element(By.XPATH, f"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[{x}]/div").tag_name
            else:
                phrase = driver.find_element(By.XPATH, f"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[{x}]/span").text
                phrase_tag = driver.find_element(By.XPATH, f"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[{x}]/span").tag_name
            dic[top_title] = phrase_tag + phrase
        except NoSuchElementException:
            pass

    #magam = driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[2]/div[1]/span[2]").text
    #magam_tag = driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[2]/div[1]/span[2]").tag_name
    #location = driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[2]/div[2]/span[2]").text
    #location_tag = driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[2]/div[2]/span[2]").tag_name
    #dic['마감일'] = magam_tag + magam
    #dic['마감일'] = magam_tag + magam
    file_path = f"C:/Users/apnee/OneDrive/바탕 화면/physon/crawling/wanted_raw_data/{str(num)+company}(wanted).json"
    with open(file_path,'w',encoding="utf-8") as f:
        json.dump(dic,f,indent=2,ensure_ascii = False)

    time.sleep(1)
    driver.back()
    time.sleep(1)
    num += 1
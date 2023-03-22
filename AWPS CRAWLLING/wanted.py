import requests
import bs4
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options

import re

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIATMPH7BYJY6WQWIE6',aws_secret_access_key = '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')


url = "https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&locations=all"

#크롬 이미지 로딩 안되게 해서 메모리 아낌
chrome_optrions = Options()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_optrions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_optrions)

driver.get(url)

time.sleep(1)


num = 1
while True:
    dic = {}
    time.sleep(1)

    # try :
    #     items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num}]')
    #     action = ActionChains(driver)
    #     action.move_to_element(items).perform()
    #     items.click()
    # except ElementNotInteractableException:
    #     for i in range(0,5):
    #         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #         time.sleep(1)
    #     items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num}]')
    #     action = ActionChains(driver)
    #     action.move_to_element(items).perform()
    #     items.click()
    # # driver.execute_script("arguments[0].click();", items)
    # except NoSuchElementException:
    #     for i in range(0,5):
    #         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #         time.sleep(1)
    #     items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num}]')
    #     action = ActionChains(driver)
    #     action.move_to_element(items).perform()
    #     items.click()
    # except ElementClickInterceptedException:
    #     for i in range(0,5):
    #         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #         time.sleep(1)
    #     items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num}]')
    #     action = ActionChains(driver)
    #     action.move_to_element(items).perform()
    #     items.click()
    # try :
    #     items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num}]')
    #     items.click()
    # except NoSuchElementException:
    #     items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num-1}]')
    #     action = ActionChains(driver)
    #     action.move_to_element(items).perform()
    #     items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num}]')
    #     items.click()
    # except ElementClickInterceptedException:
    #     items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num-1}]')
    #     action = ActionChains(driver)
    #     action.move_to_element(items).perform()
    #     items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num}]')
    #     items.click()
    # except ElementNotInteractableException:
    #     items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num-1}]')
    #     action = ActionChains(driver)
    #     action.move_to_element(items).perform()
    #     items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num}]')
    #     items.click()
    # driver.execute_scr
    try :
        items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num}]')
        action = ActionChains(driver)
        action.move_to_element(items).perform()
        items.click()
    except NoSuchElementException :
        items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num-1}]')
        action = ActionChains(driver)
        action.move_to_element(items).perform()
        items = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div/div/div[4]/ul/li[{num}]')
        items.click()
    time.sleep(1)

    Id = driver.current_url
    Idd = Id.maketrans({
        '/': '',  # 왼쪽은 치환하고 싶은 문자, 오른쪽은 새로운 문자
    })

    Iddd =Id.translate(Idd)
    Rid = int(re.sub(r"[a-z]", "", Iddd)[4:])
    dic['id'] = Rid

    try :
        title = driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div[1]/div[1]/div/section[2]/h2").text
        title_tag1 = '<' + driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div[1]/div[1]/div/section[2]/h2").tag_name + '>'
        title_tag2 = '</' + driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div[1]/div[1]/div/section[2]/h2").tag_name + '>'
        dic['회사제목'] = title_tag1 + title + title_tag2
    except NoSuchElementException:
        pass

    try :
        company_name = driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/div[1]/div[1]/div/section[2]/div[1]/h6/a").text
        company_tag1 = '<' + driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/div[1]/div[1]/div/section[2]/div[1]/h6/a").tag_name + '>'
        company_tag2 = '</' + driver.find_element(By.XPATH,"//*[@id='__next']/div[3]/div[1]/div[1]/div/section[2]/div[1]/h6/a").tag_name + '>'
        dic['회사이름'] = company_tag1 + company_name + company_tag2
    except NoSuchElementException:
        pass
 
    try :
        des = driver.find_element(By.XPATH, "//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[1]/span").text
        des_tag1 = '<' + driver.find_element(By.XPATH, f"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[1]/span").tag_name + '>'
        des_tag2 = '</' + driver.find_element(By.XPATH, f"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[1]/span").tag_name + '>'
        dic["회사설명"] = des_tag1 + des + des_tag2

    except NoSuchElementException:
        pass


    #페이지 로딩을 위해 아래 요소까지 스크롤
    while True:
        try :
            to_scroll = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[1]/div[2]/h5')
            action = ActionChains(driver)
            action.move_to_element(to_scroll).perform()
            break
        except NoSuchElementException:
            try :
                to_scroll = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/section[3]')
                action = ActionChains(driver)
                action.move_to_element(to_scroll).perform()
                break
            except NoSuchElementException:
                try :
                    to_scroll = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/section[4]')
                    action = ActionChains(driver)
                    action.move_to_element(to_scroll).perform()
                    break
                except NoSuchElementException:
                    try :
                        to_scroll = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[1]/div[2]')
                        action = ActionChains(driver)
                        action.move_to_element(to_scroll).perform()
                        break
                    except NoSuchElementException:
                        continue

    time.sleep(0.5)
    source = driver.page_source
    bs = bs4.BeautifulSoup(source,'html.parser')
    
    try :
        entire = bs.find('section', class_ = 'JobDescription_JobDescription__VWfcb')
        dic['본문'] = str(entire)
    except NoSuchElementException:
        pass
    except AttributeError:
        pass

    try :
        Dead_Line = bs.find('section', class_ = 'JobWorkPlace_className__ra6rp').find('span', class_ = 'body').text
        dic['마감일'] = str(Dead_Line)
    except NoSuchElementException:
        pass
    except AttributeError:
        pass

    try :
        Work_Location = bs.find('section', class_ = 'JobWorkPlace_className__ra6rp').find('div').next_sibling.find('span', class_ = 'body').text
        dic['근무지역'] = str(Work_Location)
    except NoSuchElementException:
        pass
    except AttributeError:
        pass

    stacks = ''

    for x in range(2,20):
        try:
            top_title  = driver.find_element(By.XPATH, f"//*[@id='__next']/div[3]/div[1]/div[1]/div/div[2]/section[1]/h6[{x-1}]").text
            if top_title == "기술스택 ・ 툴":
                for i in range(1,20) :
                    try :
                        stack = driver.find_element(By.XPATH, f'//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[6]/div/div[{i}]').text
                        stacks =  stacks + stack + ','
                    except NoSuchElementException :
                        pass
        except NoSuchElementException:
            pass
        
    dic['기술스택'] = stacks

    
    """region = driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/div[2]/section[2]/div[2]/span[2]').text"""



    print(dic)
    print(num)
    table = dynamodb.Table('wanted')
    table.put_item(Item=dic)

    driver.back()

    # if num%20 == 0:
    #     for i in range(1,5) :
    #         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #         time.sleep(1)


    num += 1
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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


dynamodb = boto3.resource('dynamodb', region_name='us-east-2',aws_access_key_id='AKIATMPH7BYJY6WQWIE6',aws_secret_access_key = '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')

url = "https://www.jumpit.co.kr/positions"

chrome_optrions = Options()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_optrions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_optrions)

url_list= []

driver.get(url)
dic = {}
# random.uniform(1, 2)

# def LEGO(url):
#     print(url)
#     driver.get(url)
#     Id = driver.current_url
#     Idd = Id.maketrans({
#     '/': '',  # 왼쪽은 치환하고 싶은 문자, 오른쪽은 새로운 문자
#     })
#     Iddd = Id.translate(Idd)
#     company_name_text = driver.find_element(By.XPATH,
#     '//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').text  # 회사이름 텍스트
#     company_name_tag1 = '<' + driver.find_element(By.XPATH,
#     '//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').tag_name + '>'  # 회사이름 태그
#     company_name_tag2 = '</' + driver.find_element(By.XPATH,
#      '//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').tag_name + '>'  # 회사이름 태그
#     company_title_cont = driver.find_element(By.XPATH,
#     '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').text  # 회사타이틀 텍스트
#     company_title_tag1 = '<' + driver.find_element(By.XPATH,
#     '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').tag_name + '>'  # 회사타이틀 태그
#     company_title_tag2 = '</' + driver.find_element(By.XPATH,
#     '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').tag_name + '>'  # 회사타이틀 태그
#     Rid = int(re.sub(r"[a-z]", "", Iddd)[4:])
#     dic['id'] = Rid
#     dic['회사이름'] = company_name_tag1 + company_name_text + company_name_tag2
#     dic['회사제목'] = company_title_tag1 + company_title_cont + company_title_tag2
#     source = driver.page_source
#     bs = bs4.BeautifulSoup(source, 'lxml')
#     entire = bs.find('section', class_='position_info')
#     dic['본문'] = str(entire)
#
#     for i in range(1, 11):
#         try:
#             DetailInfo_title = driver.find_element(By.XPATH,
#                                                    f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dt').text
#
#             DetailInfo_cont = driver.find_element(By.XPATH,
#                                                   f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dd').text
#
#             dic[DetailInfo_title] = DetailInfo_cont
#         except NoSuchElementException:
#             pass
#         # 기술스택
#         stacks = ''
#         for i in range(1, 20):
#             try:
#                 stack = driver.find_element(By.XPATH,
#                                             f'//*[@id="root"]/main/div/div[2]/div/section[2]/dl[1]/dd/pre/div[{i}]').text
#                 stacks = stacks + stack + ','
#             except NoSuchElementException:
#                 pass
#         dic['기술스택'] = stacks
#
#         try:
#             service_intro = driver.find_element(By.XPATH,
#                                                 '//*[@id="root"]/main/div/div[2]/div/section[4]/div[2]/pre').text
#             dic['기업/서비스 소개'] = service_intro
#         except NoSuchElementException:
#             pass
#
#         try:
#             employ_price = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/aside/div[1]/span').text
#             dic['취업축하금'] = employ_price
#         except NoSuchElementException:
#             pass
#
#     print(dic)
#     table = dynamodb.Table('jumpit')
#     table.put_item(Item=dic)










num = 0

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        a_tags = driver.find_elements(By.TAG_NAME,'a')
        for a in a_tags:
            href = a.get_attribute('href')
            print(href)
            url_list.append(href)
        new_list = [item for item in url_list if
                    item is not None and 'https://www.jumpit.co.kr/position/' in item and item != 'https://www.jumpit.co.kr/rookie/position']

        for i in new_list:
            num += 1
            print(num)
            print(i)
            driver.get(i)
            Id = driver.current_url
            Idd = Id.maketrans({
                '/': '',  # 왼쪽은 치환하고 싶은 문자, 오른쪽은 새로운 문자
            })
            Iddd = Id.translate(Idd)
            wait = WebDriverWait(driver, 1) #잠깐 기다려주기
            company_name_text_check = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/main/div/div[2]/div/section[1]/div/a'))) #기다려주기 2
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
            Rid = int(re.sub(r"[a-z]", "", Iddd)[4:])
            dic['id'] = Rid
            dic['회사이름'] = company_name_tag1 + company_name_text + company_name_tag2
            dic['회사제목'] = company_title_tag1 + company_title_cont + company_title_tag2
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
                    employ_price = driver.find_element(By.XPATH,
                                                       '//*[@id="root"]/main/div/div[2]/aside/div[1]/span').text
                    dic['취업축하금'] = employ_price
                except NoSuchElementException:
                    pass

            print(dic)
            table = dynamodb.Table('jumpit')
            table.put_item(Item=dic)
            #print(i)
            # id = str(i).replace("https://www.jumpit.co.kr/position/","")
            # file_path = f"C:/Users/apnee/OneDrive/바탕 화면/awps/awps-project/AWPS CRAWLLING/data/jumpit/{id}(jumpit).json"
            # with open(file_path,'w',encoding="utf-8") as f:
            #     json.dump(i,f,indent=2,ensure_ascii = False)
            time.sleep(1)
            dic = {}
        driver.quit()
        break
    last_height = new_height










    # time.sleep(1)
    #
    #     # 회사 정보 긁어오기
    #     Id = driver.current_url
    #     Idd = Id.maketrans({
    #         '/': '',  # 왼쪽은 치환하고 싶은 문자, 오른쪽은 새로운 문자
    #     })
    #     Iddd = Id.translate(Idd)
    #     company_name_text = driver.find_element(By.XPATH,
    #                                             '//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').text  # 회사이름 텍스트
    #     company_name_tag1 = '<' + driver.find_element(By.XPATH,
    #                                                   '//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').tag_name + '>'  # 회사이름 태그
    #     company_name_tag2 = '</' + driver.find_element(By.XPATH,
    #                                                    '//*[@id="root"]/main/div/div[2]/div/section[1]/div/a').tag_name + '>'  # 회사이름 태그
    #
    #     company_title_cont = driver.find_element(By.XPATH,
    #                                              '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').text  # 회사타이틀 텍스트
    #     company_title_tag1 = '<' + driver.find_element(By.XPATH,
    #                                                    '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').tag_name + '>'  # 회사타이틀 태그
    #     company_title_tag2 = '</' + driver.find_element(By.XPATH,
    #                                                     '//*[@id="root"]/main/div/div[2]/div/section[1]/h1').tag_name + '>'  # 회사타이틀 태그
    #
    #     # 딕셔너리에 넣기
    #     Rid = int(re.sub(r"[a-z]", "", Iddd)[4:])
    #     dic['id'] = Rid
    #     dic['회사이름'] = company_name_tag1 + company_name_text + company_name_tag2
    #     dic['회사제목'] = company_title_tag1 + company_title_cont + company_title_tag2
    #
    #     # 정보 전체 다 긁어오기
    #
    #     source = driver.page_source
    #     bs = bs4.BeautifulSoup(source, 'lxml')
    #     entire = bs.find('section', class_='position_info')
    #     dic['본문'] = str(entire)
    #
    #     for i in range(1, 11):
    #         try:
    #             DetailInfo_title = driver.find_element(By.XPATH,
    #                                                    f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dt').text
    #
    #             DetailInfo_cont = driver.find_element(By.XPATH,
    #                                                   f'//*[@id="root"]/main/div/div[2]/div/section[3]/dl[{i}]/dd').text
    #
    #             dic[DetailInfo_title] = DetailInfo_cont
    #         except NoSuchElementException:
    #             pass
    #
    #     # 기술스택
    #     stacks = ''
    #     for i in range(1, 20):
    #         try:
    #             stack = driver.find_element(By.XPATH,
    #                                         f'//*[@id="root"]/main/div/div[2]/div/section[2]/dl[1]/dd/pre/div[{i}]').text
    #             stacks = stacks + stack + ','
    #         except NoSuchElementException:
    #             pass
    #     dic['기술스택'] = stacks
    #
    #     try:
    #         service_intro = driver.find_element(By.XPATH,
    #                                             '//*[@id="root"]/main/div/div[2]/div/section[4]/div[2]/pre').text
    #         dic['기업/서비스 소개'] = service_intro
    #     except NoSuchElementException:
    #         pass
    #
    #     try:
    #         employ_price = driver.find_element(By.XPATH, '//*[@id="root"]/main/div/div[2]/aside/div[1]/span').text
    #         dic['취업축하금'] = employ_price
    #     except NoSuchElementException:
    #         pass
    #
    #     print(dic)
    #     print(num)
    #     table = dynamodb.Table('jumpit')
    #     table.put_item(Item=dic)
    #
    #     driver.back()
    #
    #     # if (num%16 == 0) :
    #     #     for i in range(1,5) :
    #     #         driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #     #         time.sleep(1)
    #     # 이걸로 하면 300개까지는 되는데 메모리초과가 쉽게 걸림
    #
    #     time.sleep(1)
    #     num += 1




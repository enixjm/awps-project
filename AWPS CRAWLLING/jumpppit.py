from selenium import webdriver
url = 'https://www.jumpit.co.kr/position/14219'
url_list= ['https://www.jumpit.co.kr/position/14219',
'https://www.jumpit.co.kr/position/14768',
'https://www.jumpit.co.kr/position/15113',
'https://www.jumpit.co.kr/position/14764',
'https://www.jumpit.co.kr/position/14754']
driver = webdriver.Chrome()
for i in url_list:
    driver.get(i)
driver.quit()
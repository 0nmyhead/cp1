import re
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

def get_pagelist(page_url):
    
    """
    
    get (company)pagelist url from https://wanted.co.kr/wdlist/~
    
    
    """
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(page_url)
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div/div/div[1]/div[1]/div/div[2]/div').click()
    driver.implicitly_wait(5)
    driver.find_element_by_xpath('//*[@id="__next"]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div[1]/ul/li[1]/button').click()
    driver.implicitly_wait(10)
    
    counter = 0
    
    while counter < 1 :
        
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)
        counter += 1

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    items = soup.select("#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li")
    pagelist = []
    
    for item in items:
        
        pagenum = item.select_one("#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li > div > a")["href"]
        pagelist.append(pagenum)
    
    driver.quit()
    
    return pagelist

def get_info(page_url):
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.wanted.co.kr'+page_url)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    driver.quit()
    
    name = soup.find('h2')
    
    return name

url = 'https://www.wanted.co.kr/wdlist/518/655?country=kr&job_sort=job.latest_order&years=-1&locations=all'

plist = get_pagelist(url)

namelist = []

for i in plist:
    
    namelist.append(get_info(i))
import time
from bs4 import BeautifulSoup
from selenium import webdriver

class WantedScrapper():
    
    def __init__(self, url = 'https://www.wanted.co.kr/wdlist/518/655?country=kr&job_sort=job.latest_order&years=-1&locations=all'):
        
        self.url = url

    def get_pagelist(page_url):
        
        """
        
        get (company)pagelist url from https://wanted.co.kr/wdlist/~
        
        동적 스크롤링으로 정보를 갱신하는 페이지를 selenium을 통해 직접 갱신
        
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
    
    def get_span_text(item):
        """
        
        Parameters
        ----------
        item : span tagged object from BeautifulSoup4
            collection of tags from bs4.
    
        Returns
        -------
        text_list : list of str 
            abstraced str list from item.
    
        """
        
        text_list = []
        
        for i in item:
            
            if i.text != '' : text_list.append(i.text)
        
        return text_list
    
    
    def get_info(page_url):
        '''
    
        Parameters
        ----------
        page_url : str
            part of url from end of https://wanted.co.kr/~.
    
        Returns
        -------
        dict
            informations from located page.
    
        '''
        
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('https://www.wanted.co.kr'+page_url)
        driver.implicitly_wait(5)
        
        action = webdriver.ActionChains(driver)
        action.move_to_element(driver.find_element_by_css_selector('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > hr')).perform()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        #header_name
        name = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > section.JobHeader_className__HttDA > h2').text
        print(name)
        #company_name
        company = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > section.JobHeader_className__HttDA > div:nth-child(2) > h6 > a')["data-company-name"]
        print(company)
        #주요업무
        work = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section > p:nth-child(3) > span')
        works = get_span_text(work)
        print(works)
        #자격요건
        requirement = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p:nth-child(5) > span')
        requirements = get_span_text(requirement)
        print(requirements)
        #우대사항
        advanced = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p:nth-child(7) > span')
        advancements = get_span_text(advanced)
        print(advancements)
        #혜택
        benefit = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p:nth-child(9) > span')
        benefits = get_span_text(benefit)
        print(benefits)
        #기술스택
        stack = soup.select('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p:nth-child(11) > div > div')
        stacks = []
        for i in stack:
            stacks.append(i.text)
        print(stacks)
        #마감일
        outdate = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobWorkPlace_className__ra6rp > div:nth-child(1) > span.body').text
        print(outdate)
        #근무지역
        loc = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobWorkPlace_className__ra6rp > div:nth-child(2) > span.body').text
        print(loc)
        driver.quit()
        
        return {'직무':name,'회사명':company,'주요업무':works,'자격요건':requirements,'우대사항':advancements,'혜택':benefits,'기술스택':stacks,'마감일':outdate,'근무지역':loc}

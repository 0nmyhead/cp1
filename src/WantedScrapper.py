import time
from bs4 import BeautifulSoup
from selenium import webdriver

class WantedScrapper():
    
    def __init__(self, url = 'https://www.wanted.co.kr/wdlist/518/655?country=kr&job_sort=job.latest_order&years=-1&locations=all'):
        
        self.url = url

        #chrome webdriver headless options for linux nogui
        self.op = webdriver.ChromeOptions()
        self.op.add_argument('--headless')
        self.op.add_argument("--no-sandbox")
        self.op.add_argument("--window-size=1280,720")

    def get_pagelist(self, page_url):
        
        """
        
        get (company)pagelist url from https://wanted.co.kr/wdlist/~
        
        동적 스크롤링으로 정보를 갱신하는 페이지를 selenium을 통해 직접 갱신
        
        """
        
        driver = webdriver.Chrome(options=self.op)
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
    
    def get_span_text(self, item):
        
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
        
        try:
        
            for i in item:
                
                if i.text != '' : text_list.append(i.text)
        
        except:
            
            text_list.append('')
        
        return text_list
    
    
    def get_info(self, page_url):
        
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
        
        driver = webdriver.Chrome(options=self.op)
        driver.maximize_window()
        driver.get('https://www.wanted.co.kr'+page_url)
        driver.implicitly_wait(5)
        
        action = webdriver.ActionChains(driver)
        action.move_to_element(driver.find_element_by_css_selector('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > section.CompanyInfo_className__VNf10')).perform()
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        infolist = []
        strlist = []
        
        #header_name
        infolist.append('직무')
        name = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > section.JobHeader_className__HttDA > h2').text
        print(name)
        strlist.append(name)
        
        #company_name
        infolist.append('회사명')
        company = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > section.JobHeader_className__HttDA > div:nth-child(2) > h6 > a')["data-company-name"]
        print(company)
        strlist.append(company)
        
        #info
        info = soup.select('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > h6')
        
        infolist.append('소개')
        for i in info:
            
            print(i.text)
            infolist.append(i.text)

        texts = soup.select('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p')

        texts = soup.select('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p')
        #never used
        spans = soup.select('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobDescription_JobDescription__VWfcb > p > span')
        
        for i in range(len(texts)):
            
            temp = []
        
            for span in texts[i]:
                
                txt = span.text
                txt.replace('・','•').replace('-','•')
                txtlist = txt.split('• ')
                [temp.append(txt) for txt in txtlist if txt != '']
            
            strlist.append(temp)
        
        #마감일
        infolist.append('마감일')
        outdate = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobWorkPlace_className__ra6rp > div:nth-child(1) > span.body').text
        print(outdate)
        strlist.append(outdate)
        
        #근무지역
        infolist.append('근무지역')
        loc = soup.select_one('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > div.JobContent_descriptionWrapper__SM4UD > section.JobWorkPlace_className__ra6rp > div:nth-child(2) > span.body').text
        print(loc)
        strlist.append(loc)
        driver.quit()
        
        dic = {}

        for i in range(len(infolist)):
            
            dic[infolist[i]] = strlist[i]
        
        return dic
    
# scrapper = WantedScrapper()
# dic = scrapper.get_info('/wd/111448')
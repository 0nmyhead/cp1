import re
import requests
from bs4 import BeautifulSoup

def get_page(page_url):
    
    """
    """

    page = requests.get(page_url)
    page.raise_for_status()

    soup = BeautifulSoup(page.text, 'html.parser')
    
    items = soup.select("#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li")
    pagelist = []
    
    for item in items:
        
        pagenum = item.select_one("#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li > div > a")["href"]
        print(pagenum)
    
    
    return 0
    

url = 'https://www.wanted.co.kr/wdlist/518/655?country=kr&job_sort=job.latest_order&years=-1&locations=all'

plist = get_page(url)
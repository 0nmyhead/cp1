import re
import requests
from bs4 import BeautifulSoup

def get_page(page_url):
    
    """
    """

    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup, page

url = 'https://www.wanted.co.kr/wdlist/518/655?country=kr&job_sort=company.response_rate_order&years=-1&locations=all'
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

import requests
from bs4 import BeautifulSoup as bs

browser = webdriver.Chrome()
# browser = webdriver.Firefox()

browser.maximize_window()
p=0
while True:
    p=p+1
    url='https://www.104.com.tw/jobbank/joblist/joblist.cfm?jobsource=104_bank1&ro=0&area=6001001000&indcat=1001001002&order=2&asc=0&page='+str(p)+'&psl=N_A'
    browser.get(url)
    soup = bs(browser.page_source,'lxml')
    tmp2_1 = soup.findAll(attrs={"class":"compname_summary"})
    tmp2_2 = soup.findAll(attrs={"class":"jobname_summary job_name"})
    # tmp2 = soup.findAll(attrs={"class":"jobname_summary job_name"} or {"class":"compname_summary"})
    tmp3 = zip(tmp2_2,tmp2_1)
    c=1
    for xx,yy in tmp3:
        print(c,xx.text.strip(),'----',yy.text.strip(),'---',str(xx).split("a href=")[1].split()[0])
        # print(c,xx.text.strip(),"\t\t\t\t",str(xx).split("a href=")[1].split()[0])        
        c+=1
    time.sleep(5)

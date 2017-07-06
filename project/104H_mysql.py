# -*- coding: utf-8 -*-
import time
import requests
import pymysql
from bs4 import BeautifulSoup as bs

def Conn(sql,data):
    conn = pymysql.connect('app.vietthuan.com', 'iii', '@Iii2017', 'iii', charset='utf8')
    curs = conn.cursor()
    curs.execute(sql,data)
    conn.commit()

    curs.close()
    conn.close()
    result = curs.fetchall()
    return result

p=0 #讀取頁數
tmp_area = []
while True:
    p=p+1
    url='https://www.104.com.tw/jobbank/joblist/joblist.cfm?jobsource=104_bank1&ro=0&area=6001001000&indcat=1001001002&order=2&asc=0&page='+str(p)+'&psl=N_A'
    res = requests.get(url)
    soup = bs(res.text,'lxml')
    tmp2_1 = soup.findAll(attrs={"class":"compname_summary"})
    tmp2_2 = soup.findAll(attrs={"class":"jobname_summary job_name"})
    # tmp2 = soup.findAll(attrs={"class":"jobname_summary job_name"} or {"class":"compname_summary"})
    tmp3 = zip(tmp2_2,tmp2_1)
    c=1

    for xx,yy in tmp3:
        # print(c,xx.text.strip(),'----',yy.text.strip(),'---',str(xx).split("a href=")[1].split()[0].replace(";jobsource=104_bank1&amp;hotjob_chr=",""))
        print(c,str(xx).split("a href=")[1].split()[0].replace("&amp;jobsource=104_bank1&amp;hotjob_chr=",""))

        sql ="""INSERT INTO List (Com,Job,URL) VALUES(%s,%s,%s)"""
        data =(xx.text.strip(),yy.text.strip(),str(xx).split("a href=")[1].split()[0])
        # Conn(sql,data)
        c+=1

    time.sleep(5)


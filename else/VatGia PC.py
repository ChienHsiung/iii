#encoding utf-8
import requests
import re
import time
import datetime
from pymongo import MongoClient
from bs4 import BeautifulSoup
import selenium
# from selenium import selenium
from selenium import webdriver


def toMangoDB(log):
	conn = MongoClient('app.vietthuan.com',27777)
	db = conn.hsiung
	db.authenticate('hsiung','ooxx@748',source='admin')
	db.vatgia.insert({'log':log})


def web():
	now = datetime.datetime.now()
	browser = webdriver.Firefox()
	browser.get('http://www.vatgia.com/392/may-tinh-linh-kien.html')
	c = 1
	while c < 50:
		c+=1
		soup = BeautifulSoup(browser.page_source, "html.parser")
		for item in soup.select('.no_picture_thumb'):
			if item.select('.name') and item.select('.price'):
				print (now,item.select('.name')[0].text.strip(),item.select('.price')[0].text)
				toMangoDB(str(now)+'~~'+item.select('.name')[0].text.strip()+'~~'+item.select('.price')[0].text)
				
		browser.get('http://www.vatgia.com/392/may-tinh-linh-kien.html,'+ str(c) +"'")
		print (len(item))

def main():
	web()

if __name__ == '__main__':
	main()
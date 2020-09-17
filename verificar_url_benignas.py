import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def readArchive():
	archive = open("/home/steven/Documents/GestorCapture/s/data_status/UrlActivas.txt","r")
	for i in archive.readlines():
		driver = createSession()
		managmentBrowser(i, driver)

def manipulateinput(driver):
	
	driver.find_element_by_xpath("//*[@id='url-tab-chooser']").click()
	driver.find_element_by_xpath("/html/body/div[1]/div[9]/div[3]/div[2]/form/div[1]/input").send_keys("https://codegolf.stackexchange.com/questions/210071/the-vanilla-factorial-challenge")
	driver.find_element_by_xpath("/html/body/div[1]/div[9]/div[3]/div[2]/form/div[1]/input").send_keys(Keys.ENTER)
	but = driver.find_element_by_xpath("//*[@id='btn-url-reanalyse']")
	print(but)
	if but is not None:
		driver.find_element_by_xpath("//*[@id='btn-url-reanalyse']").click()

	clasification(driver)

def clasification(driver):
	driver.implicitly_wait(100)
	driver.find_element_by_xpath("//*[@id='sampleCard']//div[1]").getText()

	#but = driver.find_element_by_xpath("/html/body/vt-ui-shell/url-view//vt-ui-main-generic-report//div/vt-ui-carousel/div[1]/vt-ui-url-mobile-card//div[1]")
	#driver.implicitly_wait(100)
	#print(but)

def createSession():
	driver = webdriver.Chrome("C:/Users/S T E V E N/AppData/Local/Programs/Python/Python37-32/chromedriver.exe")
	driver.maximize_window()
	return driver

def managmentBrowser(url, driver):
	print(str(url))
	driver.implicitly_wait(100)
	driver.get(str(url))
	driver.implicitly_wait(100)
	manipulateinput(driver)

	driver.quit()


def execution():
	readArchive()

if __name__ == '__main__':
	execution()

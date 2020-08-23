import time
import timeit
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

sitios = ["http://www.google.com","https://www.facebook.com/","https://stackoverflow.com/","https://www.w3schools.com/"]


def createSession():
	driver = webdriver.Chrome("/home/steven/Documents/GestorCapture/chromedriver")
	driver.maximize_window()
	return driver

def managmentBrowser(driver, url, i):
	print(str(url))
	driver.implicitly_wait(100)
	driver.get(str(url))
	trafficStartCapture(i)
	time.sleep(30)
	driver.implicitly_wait(100)
	driver.quit()

def execution():
	for i in range(len(sitios)):
		driver = createSession()
		managmentBrowser(driver, sitios[i], i)

	
	
def trafficStartCapture(i):
	print(i)
	cmd = "sudo tshark -a duration:30 -w - > /home/steven/Documents/GestorCapture/-Miner_Detector/CAPTURAS/{}.pcap".format(i)
	os.system(cmd)


	



if __name__ == '__main__':
	execution()    

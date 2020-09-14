import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def readArchive():
	archive = open("./Entrenamiento/data0.txt" , "r")
	print(archive)
	j = 434
	for i in archive.readlines():
		try:
			driver = createSession()
			managmentBrowser(driver, i, j)
			j+=1
		except:
			archive = open("./Entrenamiento/noEscaneada.txt" , "a")
			archive.write(i)
			pass
	
		
		

def createSession():
	driver = webdriver.Chrome("./chromedriver")
	driver.maximize_window()
	return driver

def managmentBrowser(driver, url, i):
	print(str(url))
	driver.implicitly_wait(100)
	driver.get('https://'+str(url))
	trafficStartCapture(i)
	time.sleep(30)
	driver.implicitly_wait(100)
	driver.quit()

def execution():
	readArchive();
	

	
	
def trafficStartCapture(i):
	print(i)
	cmd = "sudo tshark -i enp1s0 -a duration:300 -w - > /home/steven/Documents/GestorCapture/s/Entrenamiento/{}.pcap".format(i)
	os.system(cmd)



if __name__ == '__main__':
	execution()
	


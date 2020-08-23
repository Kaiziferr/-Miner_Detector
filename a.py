import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Navigate to the application home page
sitios = ["http://www.google.com","https://www.facebook.com/","https://stackoverflow.com/","https://www.w3schools.com/"]
for i in sitios:
	# create a new Firefox session
	driver = webdriver.Chrome("C:/Users/S T E V E N/AppData/Local/Programs/Python/Python37-32/chromedriver.exe")
	driver.maximize_window()
	print(str(i))	
	driver.implicitly_wait(100)
	driver.get(str(i))
	time.sleep(300)
	driver.implicitly_wait(100)
	# close the browser window
	driver.quit()



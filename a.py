import requests
import os
import csv

URL = 'https://www.virustotal.com/vtapi/v2/url/scan'
url = 'https://www.virustotal.com/vtapi/v2/url/report'

def urlScan(params):
	requests.post(URL, data=params)

def getReport(params):
	response = requests.get(url, params=params)
	return response.json()


def managementResponse(file):
	print(file)
	

def execution():
	#params = {'apikey': 'eff112509d99ba0ef88682356a0c1f134cb973310a6d3512e9ff13a04437b3f5', 'url':'https://crypto-loot.org/'}
	#params2 = {'apikey': 'eff112509d99ba0ef88682356a0c1f134cb973310a6d3512e9ff13a04437b3f5', 'resource':'bed5db125302663b090d4dcf170873a5ff60bbe44d72e451801497751e5a78df-1598663151'}
	#urlScan(params)
	#response = getReport(params2)

def maliFile():
	print("hola")




if __name__ == '__main__':
	maliFile()
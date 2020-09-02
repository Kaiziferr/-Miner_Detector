import os
import requests
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def fileRead():
    file = open('test.txt',"r")
    for i in file.readlines():
        i = i.replace('\n','')
        checkUrl(i)
        

def checkUrl(url):
    status = 0
    try:
       response =requests.get(url)
       status = response.status_code
       print(response)
    except requests.exceptions.RequestException as e:
        print(e)
        pass

    if status == 200:
        file = open("UrlActivas.txt","a")
        file.write(str(url)+"\n")
        file.close()
    elif status == 0:
        file = open("UrlnoEscaneadas.txt","a")
        file.write(str(url)+"\n")
        file.close()
    else:
        file = open("UrlInactivas.txt","a")
        file.write(str(url)+"\n")
        file.close()


def execute():
    fileRead()

if __name__ == "__main__":
    execute()
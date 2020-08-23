import webbrowser as web
import subprocess as sub
import time as tm

def readFile():
	file = open('url_Benignas.txt', 'r')
	while(True):
		line = file.readline()
		RunProcess(line)
		if not line:
			break;
	file.close()
	

def RunProcess(line):		
	sub.Popen(['C:/Program Files/Mozilla Firefox/firefox.exe',line])
	tm.sleep(5)
	sub.Popen(['C:/Program Files/Wireshark/Wireshark.exe',line])
	tm.sleep(30)
	sub.Popen("TASKKIll /im firefox.exe ", shell=True)
	sub.Popen("TASKKIll /im Wireshark.exe ", shell=True)
	

if __name__ == '__main__':
	readFile();


import os
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import update_calendar

def main():
	chromeOptions = webdriver.ChromeOptions()
	prefs = {"download.default_directory" : "D:/Projects/Python/api"}
	chromeOptions.add_experimental_option("prefs",prefs)
	chromedriver = "D:/Projects/Python/api/chromedriver.exe"
	driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chromeOptions)

	driver=webdriver.Chrome()

	driver.get('https://s1.wcy.wat.edu.pl/ed/')
	plik=open("login.txt","r") 
	line=plik.readlines()
	login=line[0]
	username = driver.find_element_by_name('userid')
	username.send_keys('jacekromaszewski')
	password=line[1]
	time.sleep(.300)
	password = driver.find_element_by_name('password')
	time.sleep(.300)
	password.send_keys(password)
	driver.find_element_by_class_name("inputLogL").click()
	url=(driver.current_url)
	print(url)
	rest=url.split("&")[0]
	rest=rest+"&mid=328&iid=20181&pos=0&rdo=1&t=6800743"
	driver.get(rest)
	url="""javascript:showGroupPlan('I7Y5S1');"""
	driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
	driver.find_element_by_xpath('//*[@title="Zapisz formularz w pliku  tekstowym w formacie OutLook"]').click()
	time.sleep(3)
	driver.quit()
	os.system('del ./old.txt')
	os.system('move ./new.txt ./old.txt')
	os.system('move C:/Users/Jack/Downloads/*.txt ./new.txt')
	os.system('python update_calendar.txt')
	update_calendar.main()

if __name__ == '__main__':
  main()
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
time.sleep(2)
driver.get('https://mail.google.com/mail/h')


# driver.find_elements_by_xpath

user_name = "lovekush@innovaccer.com"
user_pwd = '<passwd>'

def login(user_name,user_pwd):
	time.sleep(2)
	email = driver.find_element_by_xpath('//*[@id="Email"]')
	email.send_keys(user_name)

	driver.find_element_by_xpath('//*[@id="next"]').click()
	time.sleep(2)
	passwd = driver.find_element_by_xpath('//*[@id="Passwd"]')
	passwd.send_keys(user_pwd)

	driver.find_element_by_xpath('//*[@id="signIn"]').click()

login(user_name,user_pwd)
time.sleep(2)
print "hello"
# label = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[1]/table[2]/tbody/tr/td/a[1]')
# label.click()
driver.get('https://mail.google.com/mail/u/0/h/1qykcbvua1ugl/?&s=l&l=forward')
# label.click()

time.sleep(2)
# driver.find_element_by_xpath('//*[@id=":kf"]')
print driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/td[3]').get_attribute('href')

# forward = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[3]/a/span')
# forward.click()

# driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/table[4]/tbody/tr/td/table[1]/tbody/tr[3]/td/div/font/a[3]').click()

# to = driver.find_element_by_xpath('//*[@id="to"]')
# to.send_keys('gangwarlovekush@gmail.com')

# send = driver.find_element_by_xpath('/html/body/table[3]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[3]/tbody/tr/td/input[1]')
# send.click()

# ?&th=154558ff32e9f02c&v=c&s=l&l=forward
# ?&th=1542de24e75a3d69&v=c&s=l&l=forward

# /html/body/table[3]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/td[3]





# /html/body/table[3]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/td[3]/a/span
# /html/body/table[3]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[2]/td[3]/a/span


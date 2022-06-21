from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser= webdriver.Chrome()
browser.get("https://demo.yetenekkapisi.org/login")
browser.implicitly_wait(10)
Ogrenci_Mezun = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div/div[2]/div/div[2]/div/div/div/div/div/ul/li[1]")
e_posta = browser.find_element_by_name("username")
e_posta.send_keys("admin@tsb.com")
sifre = browser.find_element_by_name("password")
sifre.send_keys("15.T35T_23.!")
time.sleep(1)
giris_yap = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/form/div[3]/button[1]").click()
time.sleep(5)

dil_degistir = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[1]/div[1]/div/div[2]/div[2]/button/span/span").click()
ingilizce_sec=browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[1]/div[1]/div/div[2]/div[2]/div/button[1]/span/span").click()
time.sleep(5)

browser.close()
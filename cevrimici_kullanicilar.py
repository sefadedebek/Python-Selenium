from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser= webdriver.Chrome()

def adminLogin(browser):
    browser.get("https://demo.yetenekkapisi.org/login")
    browser.implicitly_wait(10)
    Ogrenci_Mezun = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div/div[2]/div/div[2]/div/div/div/div/div/ul/li[1]")
    e_posta = browser.find_element_by_name("username")
    e_posta.send_keys("admin@tsb.com")
    sifre = browser.find_element_by_name("password")
    sifre.send_keys("15.T35T_23.!")
    time.sleep(2)
    giris_yap = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/form/div[3]/button[1]").click()

def cevrimici_kullanicilar(browser):
    cevrimici_kullanicilar = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[1]/div[2]/div/section/div[1]/div/div[1]/div/ul/div[4]/div/button").click()
    time.sleep(1)
    yenile = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[1]/div[2]/div/section/div[1]/div/div[1]/div/ul/div[4]/div/div/ul/div/li[1]/a/span").click()
    time.sleep(2)

adminLogin(browser)
cevrimici_kullanicilar(browser)
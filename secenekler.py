from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

browser= webdriver.Chrome()
#browser.maximize_window()

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
    time.sleep(3)


def universiteler(browser):

    browser.get("https://demo.yetenekkapisi.org/settings/universities")
    #yeni_ekle = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/a/button").click()
    time.sleep(2)

def is_ilani_istekleri(browser):

    browser.get("https://demo.yetenekkapisi.org/settings/company/jobposting/request")
    incele = browser.find_element_by_xpath("//*[@id='detailButton_891459']").click()
    time.sleep(2)

def isveren_istekleri(browser):

    browser.get("https://demo.yetenekkapisi.org/settings/company/access/request")
    incele = browser.find_element_by_xpath("//*[@id='detailCompanyRequestButton_1553998']").click()
    time.sleep(2)

def etkinlik_istekleri(browser):

    browser.get("https://demo.yetenekkapisi.org/settings/company/activity/request")
    incele = browser.find_element_by_xpath("//*[@id='detailActivityButton_13505']").click()
    time.sleep(2)

def universite_fakülteleri(browser):

    browser.get("https://demo.yetenekkapisi.org/settings/university_faculties")
    yeni_ekle = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div[1]/a/button").click()
    time.sleep(2)

def universite_bölümleri(browser):

    browser.get("https://demo.yetenekkapisi.org/settings/university_departments")
    yeni_ekle = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div[1]/a/button").click()
    time.sleep(2)

def bütün_bölümler(browser):

    browser.get("https://demo.yetenekkapisi.org/settings/departments")
    düzenle = browser.find_element_by_xpath("//*[@id='editButtonId_11606']").click()
    time.sleep(2)

adminLogin(browser)
universiteler(browser)
is_ilani_istekleri(browser)
isveren_istekleri(browser)
etkinlik_istekleri(browser)
universite_fakülteleri(browser)
universite_bölümleri(browser)
bütün_bölümler(browser)
browser.close()
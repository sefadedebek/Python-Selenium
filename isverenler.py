from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


browser= webdriver.Chrome()
browser.maximize_window()


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


veriler = ["KURUM ADI", "ADRES1", "TÜRKİYE", "ANKARA", "wergweghg.com.tr", "wergweghg@wergweghg.com", "Ahmet Yilmaz", "905368746587", "ahmetyilmaz@deneme.com", "TÜRKİYE" ]


def isveren_ekle(browser,veriler):

    isveren = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div[2]/a").click()
    time.sleep(3)
    yeni_ekle = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/a/button").click()
    time.sleep(3)

    browser.find_elements_by_class_name("form__form-group-input-wrap")[0].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(veriler[0]).perform()     
    time.sleep(0.5)

    browser.find_elements_by_class_name("form__form-group-input-wrap")[1].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(veriler[1]).perform()    
    time.sleep(0.5)

    
    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/form/div[3]/div/ul/li[2]/div/div/div/div").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(veriler[2]).send_keys(Keys.ENTER).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    
    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/form/div[3]/div/ul/li[3]/div/div/div/div").click()                
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(veriler[3]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)   

    webSite = browser.find_element_by_name("webSite")
    webSite.send_keys(veriler[4])
    time.sleep(0.5)

    email = browser.find_element_by_name("email")
    email.send_keys(veriler[5])
    time.sleep(0.5)

    personalNameSurname = browser.find_element_by_name("personalNameSurname")
    personalNameSurname.send_keys(veriler[6])
    time.sleep(0.5)

    personalPhone = browser.find_element_by_name("personalPhone")
    personalPhone.send_keys(veriler[7])
    time.sleep(0.5)

    personalEmail = browser.find_element_by_name("personalEmail")
    personalEmail.send_keys(veriler[8])
    time.sleep(0.5)

    browser.find_element_by_class_name("countryFilterDataDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(veriler[9]).send_keys(Keys.ENTER).send_keys(Keys.ENTER).perform()
    time.sleep(2)

    universite_sec = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/form/div[8]/div[3]/div/div/div/div[1]/div[2]").click()
    time.sleep(0.5)

    browser.find_element_by_css_selector("button.btn-primary").click()
    time.sleep(1)


def detayli_arama(browser):
    
    isveren = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div[2]/a").click()
    time.sleep(1)
    browser.find_element_by_link_text("Detaylı Arama").click()
    time.sleep(0.5)

    name = browser.find_element_by_xpath("//input[@name='title']")
    name.send_keys("Örnek Kurum Adı")


    email = browser.find_element_by_xpath("//input[@name='email']").send_keys("deneme@deneme.com")

    browser.find_element_by_class_name("countryFilterDataDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("TÜRKİYE").send_keys(Keys.ENTER).perform()     
    time.sleep(0.5)

    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/form/div[7]/button[1]").click()


def arama_sonucları(browser):

    isveren = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div[2]/a").click()
    time.sleep(1)
    browser.find_element_by_link_text("Arama Sonuçları").click()
    time.sleep(0.5)

def arsivlenmis_isverenler(browser):
    time.sleep(1)
    browser.get("https://demo.yetenekkapisi.org/companies")
    time.sleep(1)
    browser.find_element_by_link_text("Arşivlenmiş İşverenler").click()
    time.sleep(0.5)


adminLogin(browser)
isveren_ekle(browser,veriler)
detayli_arama(browser)
arama_sonucları(browser)
arsivlenmis_isverenler(browser)
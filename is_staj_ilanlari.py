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


def is_ilanlari_ekle(browser,veriler):

    isveren = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div[3]/a").click()
    time.sleep(3)

    yeni_ekle = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/a/button").click()
    time.sleep(3)

    pozisyon_turu = browser.find_element_by_xpath("//*[@id='react-select-3-option-2']").click()
    time.sleep(3)

    browser.find_element_by_class_name("companyDto").click()
    ActionChains(browser).send_keys("AEGON EMEKLİLİK VE HAYAT A.Ş.").send_keys(Keys.ENTER).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element_by_class_name("companyDto").click()
    ActionChains(browser).send_keys("AEGON EMEKLİLİK VE HAYAT A.Ş.").send_keys(Keys.ENTER).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element_by_class_name("contactEmployeeDto").click()
    ActionChains(browser).send_keys("ECE DURMAZ ÇOBAN").send_keys(Keys.ENTER).perform()     
    time.sleep(0.5)

    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/form/div[9]/div/div/input").click()
    ActionChains(browser).send_keys("ÇALIŞAN").send_keys(Keys.ENTER).perform()     
    time.sleep(0.5)

    browser.find_element_by_class_name("description").click()
    ActionChains(browser).send_keys("AÇIKLAMA").perform()     
    time.sleep(0.5)

    
    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/form/div[11]/div/ul/li[1]/div/div/div/div").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("TÜRKİYE").send_keys(Keys.ENTER).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    
    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/form/div[11]/div/ul/li[2]/div/div/div/div").click()                
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("ANKARA").send_keys(Keys.ENTER).perform()
    time.sleep(0.5)   

    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/form/div[11]/div/ul/li[3]/div/div/input").click()                
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("ÇANKAYA").send_keys(Keys.ENTER).perform()
    time.sleep(0.5)   

    browser.find_elements_by_class_name("date-picker")[0].click()
    time.sleep(0.5)
    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/form/div[12]/div/div[1]/div/div[2]/div/div[2]/div[2]/div[5]/div[5]").click()
    time.sleep(0.5)
    browser.find_elements_by_class_name("date-picker")[1].click()
    time.sleep(0.5)
    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/form/div[13]/div/div[1]/div/div[2]/div/div[2]/div[2]/div[5]/div[7]").click()
    time.sleep(0.5)

    browser.find_element_by_class_name("countryFilterDataDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("TÜRKİYE").send_keys(Keys.ENTER).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element_by_class_name("countryFilterDataDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("TÜRKİYE").send_keys(Keys.ENTER).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/form/div[17]/div[4]/div/div/div/div[1]/div[2]").click()
    time.sleep(0.5)

    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/form/div[18]/div[2]/div/div/div/div[1]/div[2]/div/div/div[3]/div").click()
    time.sleep(0.5)

    browser.find_element_by_css_selector("button.btn-primary").click()
    time.sleep(0.5)



def detayli_arama(browser):
    
    browser.get("https://demo.yetenekkapisi.org/jobpostings")
    time.sleep(1)
    browser.find_element_by_link_text("Detaylı Arama").click()
    time.sleep(0.5)

    name = browser.find_element_by_xpath("//input[@name='title']")
    name.send_keys("Frontend Developer")

    browser.find_element_by_class_name("countryFilterDataDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("TÜRKİYE").send_keys(Keys.ENTER).perform()     
    time.sleep(0.5)

    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/form/div[11]/button[1]").click()

def arama_sonucları(browser):

    browser.get("https://demo.yetenekkapisi.org/jobpostings")
    time.sleep(1)
    browser.find_element_by_link_text("Arama Sonuçları").click()
    time.sleep(0.5)

def suresi_dolmuş_is_ilanlari(browser):
    time.sleep(1)
    browser.get("https://demo.yetenekkapisi.org/jobpostings")
    time.sleep(1)
    browser.find_element_by_link_text("Süresi Dolmuş İş İlanları").click()
    time.sleep(0.5)


adminLogin(browser)
is_ilanlari_ekle(browser,veriler)
detayli_arama(browser)
arama_sonucları(browser)
suresi_dolmuş_is_ilanlari(browser)

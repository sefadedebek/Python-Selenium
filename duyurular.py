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


duyuru_liste=["Başlıkkk", "Örnek Açıklama", "Aralık 2020", "14", "Şubat 2021", "19","Örnek Adres", "TÜRKİYE", "Ankara", "www.linkedin.com", "www.twitter.com","www.youtube.com/", "Örnek Mail Açıklamasıı"]


def yeni_duyuru_ekle(browser, duyuru_liste):

    browser.get("https://demo.yetenekkapisi.org/announcements")

    yeni_ekle = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/a/button").click()
    time.sleep(3)

    browser.find_element(By.XPATH, "//input[@name='title']").send_keys("Örnek Başlık")
    time.sleep(0.5)

    browser.find_element_by_class_name("DraftEditor-editorContainer").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("Örnek Açıklama").send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_elements_by_class_name("date-picker")[0].click()
    time.sleep(0.5)
    ay_yil = browser.find_elements_by_class_name("react-datepicker__current-month")[0]
    while (ay_yil.text != "Aralık 2020"):
        browser.find_element_by_class_name("react-datepicker__navigation--next").click()
        time.sleep(0.5)
    time.sleep(0.5)
    browser.find_element_by_class_name("react-datepicker__day--0" + "10").click()

    browser.find_elements_by_class_name("date-picker")[1].click()
    time.sleep(0.5)
    ay_yil = browser.find_elements_by_class_name("react-datepicker__current-month")[0]
    while (ay_yil.text != "Aralık 2020"):
        browser.find_element_by_class_name("react-datepicker__navigation--next").click()
        time.sleep(0.5)
    time.sleep(0.5)
    browser.find_element_by_class_name("react-datepicker__day--0" + "29").click()

    browser.find_element_by_class_name("countryFilterDataDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("TÜRKİYE").send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element_by_class_name("cityFilterDataDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("ANKARA").send_keys(Keys.ENTER).perform()  # kariyer fuarı seçimi combobox
    time.sleep(0.5)

    universite_sec=browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div/div/div/div/form/div[6]/div[4]/div/div/div/div[1]/div[2]").click()

    browser.find_element_by_css_selector("button.btn-primary").click()
    time.sleep(0.5)



adminLogin(browser)
yeni_duyuru_ekle(browser, duyuru_liste)


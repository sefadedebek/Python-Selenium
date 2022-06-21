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


kar_fuari_liste=["Başlıkkk", "Açıklamaaçıklamaaçıklamaaçıklama", "Aralık 2020", "30", "Ocak 2021", "15", "Aralık 2020", "10", "Aralık 2020", "15",
           "Örnek Adres", "TÜRKİYE", "Ankara", "Örnek Mail Açıklamasıı"]


def yeni_kariyer_fuarı_ekle(browser, kar_fuari_liste ):
    
    browser.get("https://demo.yetenekkapisi.org/career_fair")

    yeni_ekle = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/a/button").click()
    time.sleep(3)

    browser.find_element(By.XPATH, "//input[@name='title']").send_keys("Örnek Başlık")
    time.sleep(0.5)

    browser.find_element_by_class_name("DraftEditor-editorContainer").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("Örnek AÇıklama").send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_elements_by_class_name("date-picker")[0].click()
    time.sleep(0.5)
    ay_yil = browser.find_elements_by_class_name("react-datepicker__current-month")[0]
    while (ay_yil.text != "Aralık 2020"):
        browser.find_element_by_class_name("react-datepicker__navigation--next").click()
        time.sleep(0.5)
    time.sleep(0.5)
    browser.find_element_by_class_name("react-datepicker__day--0" + "30").click()
    
    browser.find_elements_by_class_name("date-picker")[1].click()
    time.sleep(0.5)
    ay_yil = browser.find_elements_by_class_name("react-datepicker__current-month")[0]
    while (ay_yil.text != "Ocak 2021"):
        browser.find_element_by_class_name("react-datepicker__navigation--next").click()
        time.sleep(0.5)
    time.sleep(0.5)
    browser.find_element_by_class_name("react-datepicker__day--0" + "15").click()
    
    browser.find_elements_by_class_name("date-picker")[2].click()
    time.sleep(0.5)
    ay_yil = browser.find_elements_by_class_name("react-datepicker__current-month")[0]
    while (ay_yil.text != "Aralık 2020"):
        browser.find_element_by_class_name("react-datepicker__navigation--next").click()
        time.sleep(0.5)
    time.sleep(0.5)
    browser.find_element_by_class_name("react-datepicker__day--0" + "10").click()
    browser.find_elements_by_class_name("date-picker")[3].click()
    time.sleep(0.5)
    ay_yil = browser.find_elements_by_class_name("react-datepicker__current-month")[0]
    while (ay_yil.text != "Aralık 2020"):
        browser.find_element_by_class_name("react-datepicker__navigation--next").click()
        time.sleep(0.5)
    time.sleep(0.5)
    browser.find_element_by_class_name("react-datepicker__day--0" + "15").click()


    browser.find_element(By.XPATH, "//textarea[@name='street']").send_keys("Örnek Adres")
    time.sleep(0.5)

    browser.find_elements_by_class_name("cityDto")[0].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("TÜRKİYE").send_keys(Keys.ENTER).perform()
    time.sleep(0.5)


    browser.find_elements_by_class_name("cityDto")[1].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("Ankara").send_keys(Keys.ENTER).perform()  # kariyer fuarı seçimi combobox
    time.sleep(0.5)


    browser.find_elements_by_class_name("DraftEditor-editorContainer")[1].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("Örnek Mail Açıklaması").send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_elements(By.XPATH, "//button[@type='submit']")[0].click()
    

adminLogin(browser)
yeni_kariyer_fuarı_ekle(browser, kar_fuari_liste )

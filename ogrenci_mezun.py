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

ogrenci_bilgi_listesi = ["Ahmet", "Yilmaz", "hjgfjhgfhh@gmail.com", "93345159380", "ERKEK", "TECILLI", "905425412569", "TÜRKİYE", "ADRES1", "TÜRKİYE", "Ankara", "Evet", "Hayır", "Evet", "ÖNLİSANS","TÜRKİYE", "ESKİŞEHİR OSMANGAZİ ÜNİVERSİTESİ" , "MEKATRONİK", 2, "ÇALIŞIYOR", 2018, 6, "3,50", 1998, 22, 12]


def ogrenci_ekle(browser,values):

    ogrenci_mezun = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div[1]/a").click()
    time.sleep(3)
    yeni_ekle = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/a/button").click()
    time.sleep(3)
    
    browser.find_elements_by_class_name("form__form-group-input-wrap")[0].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[0]).perform()    
    time.sleep(0.5)

    browser.find_elements_by_class_name("form__form-group-input-wrap")[1].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[1]).perform()     
    time.sleep(0.5)
    browser.find_elements_by_class_name("form__form-group-input-wrap")[2].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[2]).perform()     
    time.sleep(0.5)

    browser.find_element(By.XPATH, "//input[@name='tckn']").send_keys(ogrenci_bilgi_listesi[3])    
    time.sleep(0.5)
    browser.find_element_by_class_name("gender").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[4]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_elements_by_class_name("date-picker")[0].click()
    time.sleep(0.5)
    browser.find_element_by_class_name("react-datepicker__year-read-view").click()
    time.sleep(2)
    browser.find_element(By.XPATH, '//div[text()="' + str(ogrenci_bilgi_listesi[23]) + '"]').click()
    time.sleep(2)
    if(ogrenci_bilgi_listesi[25]>9):
        for i in range(0, ogrenci_bilgi_listesi[25]-9):
            browser.find_element_by_class_name("react-datepicker__navigation--next").click()
            time.sleep(0.5)
        browser.find_element_by_class_name("react-datepicker__day--0" + str(ogrenci_bilgi_listesi[24])).click()
        time.sleep(0.5)
    elif(ogrenci_bilgi_listesi[23]<9):
        for i in range(0, 9-ogrenci_bilgi_listesi[25]):
            browser.find_element_by_class_name("react-datepicker__navigation--previous").click()
            time.sleep(0.5)
        browser.find_element_by_class_name("react-datepicker__day--0" + str(ogrenci_bilgi_listesi[24])).click()
        time.sleep(0.5)
    else:
        browser.find_element_by_class_name("react-datepicker__day--0" + str(ogrenci_bilgi_listesi[24])).click()
    time.sleep(0.5)
    browser.find_element_by_class_name("militaryServiceStatusDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[5]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element(By.XPATH, "//input[@name='phone']").send_keys(ogrenci_bilgi_listesi[6])
    time.sleep(0.5)
  
    browser.find_element_by_class_name("nationalityDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[7]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element(By.XPATH, "//textarea[@name='street']").send_keys(ogrenci_bilgi_listesi[8])
    time.sleep(1)

    browser.find_element_by_class_name("countryDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[9]).send_keys(Keys.ENTER).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)
    browser.find_element_by_class_name("cityDto").click()                
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[10]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)   
    if (ogrenci_bilgi_listesi[11] == "Evet"):  
        browser.find_elements_by_class_name("radio-btn")[0].click()
        time.sleep(0.5)
    if (ogrenci_bilgi_listesi[12] == "Evet"):  
        browser.find_elements_by_class_name("radio-btn")[2].click()
        time.sleep(0.5)
    if (ogrenci_bilgi_listesi[13] == "Hayır"):  
        browser.find_elements_by_class_name("radio-btn")[4].click()
        time.sleep(0.5)
    time.sleep(1)
    browser.find_elements_by_class_name("departmentDto")[0].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[14]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_elements_by_class_name("universityDto")[0].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[15]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_elements_by_class_name("universityDto")[1].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[16]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_elements_by_class_name("departmentDto")[1].click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[17]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)
    
    browser.find_element_by_class_name("classLevelDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[18]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)
  
    browser.find_element_by_class_name("careerStatusDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[19]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)
 
    browser.find_elements_by_class_name("date-picker")[1].click()
    yil_farki = 2020 - ogrenci_bilgi_listesi[20]
    for i in range(0, yil_farki):
        browser.find_element_by_class_name("react-datepicker__navigation--previous").click()
        time.sleep(0.5)
    time.sleep(0.5)
    browser.find_element_by_class_name("react-datepicker__month-" + str(ogrenci_bilgi_listesi[21] - 1)).click()

    browser.find_element(By.XPATH, "//input[@name='gpa']").send_keys(ogrenci_bilgi_listesi[22])
    time.sleep(0.5)
    
    browser.find_element_by_css_selector("button.btn-primary").click()
    time.sleep(1)

    browser.find_element_by_class_name("countryDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[9]).send_keys(Keys.ENTER).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element_by_class_name("cityDto").click()                
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(ogrenci_bilgi_listesi[10]).send_keys(Keys.ENTER).perform()
    time.sleep(0.5)  

    # Kaydet
    browser.find_element_by_css_selector("button.btn-primary").click()
    time.sleep(0.5)
    
    #browser.close()

arama_listesi=["Kriterleri Kaydet", "Örnek arama", "", "Ahmet", "Yilmaz", "", "", "", "", "", "", "", ""]

def detayli_arama(browser, arama_listesi):
    
    browser.get("https://demo.yetenekkapisi.org/students/students")
    time.sleep(0.5)
    browser.find_element_by_link_text("Detaylı Arama").click()
    time.sleep(0.5)

    name = browser.find_element_by_xpath("//input[@name='firstName']")
    name.send_keys("Ahmet")

    surmane = browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/form/div[4]/div/div/input").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("Yilmaz").perform()

    #email = browser.find_element_by_xpath("//input[@name='email']").send_keys("deneme@deneme.com")

    browser.find_element_by_class_name("countryDto").click()
    ActionChains(browser).send_keys("TÜRKİYE").send_keys(Keys.ENTER).perform()     

    time.sleep(0.5)
    browser.find_element_by_class_name("gender").click()
    ActionChains(browser).send_keys("ERKEK").send_keys(Keys.ENTER).perform()     

    LİSANS=browser.find_elements_by_class_name("react-select__option")[1].click()
    time.sleep(0.5)

    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/form/div[11]/div[1]/div/div[1]/div/div/div").click().key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("TÜRKİYE").send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element(By.XPATH,"//input[@name='minGpa']").send_keys("2.5")
    time.sleep(0.5)

    browser.find_element_by_xpath("//*[@id='root']/div[1]/div/div/main/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/form/div[17]/button[1]").click()

def arama_sonucları(browser):
    time.sleep(1)
    browser.get("https://demo.yetenekkapisi.org/students/students")
    browser.find_element_by_link_text("Arama Sonuçları").click()
    time.sleep(0.5)

def arsivlenmis_ogrenciler(browser):
    time.sleep(1)
    browser.get("https://demo.yetenekkapisi.org/students/students")
    time.sleep(0.5)
    browser.find_element_by_link_text("Arşivlenmiş Öğrenciler").click()
    time.sleep(0.5)

def ogrenci_duzenle(browser):

    time.sleep(1)
    browser.get("https://demo.yetenekkapisi.org/students/students")
    time.sleep(0.5)
    browser.find_element_by_css_selector(".lnr-pencil").click()
    time.sleep(1)

    browser.find_element(By.XPATH, "//input[@name='tckn']").send_keys("60117296956")  # tc kimlik
    time.sleep(0.5)

    browser.find_element_by_class_name("gender").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("ERKEK").send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element_by_class_name("countryDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("TÜRKİYE").send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element_by_class_name("cityDto").click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys("Ankara").send_keys(Keys.ENTER).perform()
    time.sleep(0.5)

    browser.find_element_by_css_selector("button.btn-primary").click()
    time.sleep(1)
    browser.close()


adminLogin(browser)
ogrenci_ekle(browser,ogrenci_bilgi_listesi)
detayli_arama(browser, arama_listesi)
arama_sonucları(browser)
arsivlenmis_ogrenciler(browser)
ogrenci_duzenle(browser)
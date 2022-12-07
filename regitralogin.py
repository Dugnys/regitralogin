#selenium/webdriver required
#Automatiskai prisijungia prie regitros puslapio ir iesko laisvos vietos vairavimo egzaminui
#Del panaikinto prisijungimo naudojant telefono numeri, nuo 2022-01-01 nebeveikia.


from selenium import webdriver
from time import sleep

def recursor():

    recursor()
    prevdate = 99
    month = "Lapkričio mėn." #ieskomas menuo (Kilmininku)
    username = "" #irasyti tel. numeri
    password = "" #slaptazodis
    url = "https://vp.regitra.lt/login"
    driver = webdriver.Chrome ("C:/chromedriver")

    driver.get(url)
    driver.find_element_by_name("userid").send_keys(username) 
    driver.find_element_by_name("pass").send_keys(password) 
    driver.find_element_by_css_selector("btn login").click()
    #print("success")

    sleep(4)
    driver.find_element_by_class("head-icon left").click()
    sleep(4)
    driver.find_element_by_class("col-sm-2 kat").click()
    sleep(4)
    driver.find_element_by_id("schedule").click()
    sleep(4)
    if driver.find_element_by_class("btn btn-md ng-binding btn-primary") < prevdate:
        prevdate = driver.find_element_by_class("btn btn-md ng-binding btn-primary")
        driver.find_element_by_class("btn btn-md ng-binding btn-primary").click()

    driver.find_element_by_class("glyphicon glyphicon-arrow-right").click()
    driver.find_element_by_class("btn btn-danger ng-scope").click()

driver.close()
recursor()
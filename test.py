import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#this is a function to check whether an element exists or  not
from selenium.common.exceptions import NoSuchElementException
def check_exists_by_xpath(xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

driver = webdriver.Chrome("J:\\Chromedriver.exe")

driver.set_page_load_timeout(300)

driver.get("https://gmail.com") #  opens gmail
driver.find_element_by_name('identifier').send_keys("seleniumprojectsid")
driver.find_element_by_id('identifierNext').click()
time.sleep(5)
driver.find_element_by_name('password').send_keys("fdsajkl;")
driver.find_element_by_id('passwordNext').click()

time.sleep(5)

driver.get("https://facebook.com") #  opens facebook
driver.find_element_by_id('email').send_keys(9752506990)
driver.find_element_by_name('pass').send_keys("fdsajkl;")

driver.get("https://tinder.com") #opens tinder

time.sleep(5)

tinder = driver.current_window_handle

if (check_exists_by_xpath("//button[@aria-label='Log in with Google']")) :
     driver.find_element_by_xpath("//button[@aria-label='Log in with Google']").click()
     time.sleep(5)

     # changing the handles to access login page
     for handle in driver.window_handles:
          if handle != tinder:
               login_page = handle

     # change the control to signin page
     driver.switch_to.window(login_page)

     driver.find_element_by_id('profileIdentifier').click()
     driver.find_element_by_xpath("//button[@aria-label='Allow']").click()
     driver.find_element_by_xpath("//button[@aria-label='Not interested']").click()
     driver.switch_to.window(tinder)

if(check_exists_by_xpath("//button[@aria-label='Log in with Facebook']")):
     driver.find_element_by_xpath("//button[@aria-label='Log in with Facebook']").click()

time.sleep(10)

counter = 0

while (1):
     driver.save_screenshot("screenshot.png")
     if(counter == 0) :
          driver.find_element_by_name('body').send_keys(Keys.CONTROL + 't') #  tried to open a new tab
          driver.get("facelytics.io")
          driver.find_element_by_xpath("//button[@aria-label='Try Facelytics']").click()
          counter +=1
     driver.find_element_by_xpath("//button[@aria-label='Browse a picture']").click()

     driver.find_element_by_xpath("//button[@aria-label='Like']").click()
driver.close()
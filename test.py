import selenium
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from PIL import Image
from io import BytesIO

#  Function to check gender, have used variable name revird because it is driver spelled backwards

driver = webdriver.Chrome("J:\\Chromedriver.exe")

#this is a function to check whether an element exists or  not
from selenium.common.exceptions import NoSuchElementException
def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

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
driver.find_element_by_id('loginbutton').click()

time.sleep(5)

driver.get("https://tinder.com") #opens tinder

time.sleep(5)

tinder = driver.current_window_handle

if (check_exists_by_xpath("//button[@aria-label='Log in with Facebook']")):
     driver.find_element_by_xpath("//button[@aria-label='Log in with Facebook']").click()

elif (check_exists_by_xpath("//button[@aria-label='Log in with Google']")) :
    driver.find_element_by_xpath("//button[@aria-label='Log in with Google']").click()
    time.sleep(5)
    # changing the handles to access login page
    for handle in driver.window_handles:
        if (handle != tinder):
            login_page = handle
            # change the control to signin page
            driver.switch_to.window(login_page)
            driver.find_element_by_id('profileIdentifier').click()
            time.sleep(5)
            driver.switch_to.window(tinder)

time.sleep(5)
driver.find_element_by_xpath("//button[@aria-label='Allow']").click()
time.sleep(5)
driver.find_element_by_xpath("//button[@aria-label='Not interested']").click()

time.sleep(5)

counter = 0

driver.find_element_by_xpath("//button[@aria-label='Close']").click()

time.sleep(5)
driver.find_element_by_xpath("//button[@aria-label='Close']").click()

'''element = driver.find_element_by_class_name("recsCardboard__cardsContainer H(100%) Pos(r) Z(1)") # find part of the page you want image of
location = element.location
size = element.size
time.sleep(10)
'''

#  main part
while (1):

    time.sleep(5)

    #  for screenshot
    driver.save_screenshot("screenshot.png")
    ''' im = Image.open(BytesIO(screenshot))  # uses PIL library to open image in memory

    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']

    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('im.png')  # saves new cropped image'''

    #  for checking gender
    revird = webdriver.Chrome("J:\\Chromedriver.exe")
    revird.get("https://gender.toolpie.com")
    time.sleep(5)
    element = revird.find_element_by_id('validatedCustomFile')
    element.send_keys(r"D:\untitled\screenshot.png")
    time.sleep(1)
    revird.find_element_by_id('inputSubmit').click()
    time.sleep(5)

    if (r"female" in revird.page_source):
        driver.find_element_by_xpath("//button[@aria-label='Like']").click()
    else :
        driver.find_element_by_xpath("//button[@aria-label='Nope']").click()
    revird.close()
driver.close()

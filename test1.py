import unittest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
# driver.close()
# driver.get("http://ruban.febinosolutions.com")
# time.sleep(1)


#
def dashboard():# To check sign in with url & check add button 
    driver.get("http://ruban.febinosolutions.com")
    driver.maximi 
    time.sleep(1)
    driver.find_element(By.ID,'email').send_keys("user@gmail.com")
    driver.find_element(By.ID,'password').send_keys("Qwerty@123")
    driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/button[1]').click()
    time.sleep(3)
    driver.find_element(By.XPATH,'/html/body/div/div[2]/section[1]/div/div/div/div/div[1]/div/button').click()
    time.sleep(1)
    expected_title="Dashboard"
    actual_title=driver.title
    #assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}")

if __name__ == "__main__":
   # unittest.main() 
    dashboard()
import unittest
import calc
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.get("http://www.google.com") 
class TestCalc(unittest.TestCase):

    def test_01_add(self):
        print("\nTestCase-1")
        calc.add()
        

    # def test_02_ad(self):
    #     print("\nTestCase-2")
    #     result=calc.add(10,5)
    #     self.assertEqual(result,15)
        

    # def test_03_sub(self):
    #     print("\nTestCase-3")
    #     result=calc.subtract(10,5)
    #     self.assertEqual(result,5)
        
   

    # def test_04_div(self):
    #     print("\nTestCase-4")
    #     result=calc.divide(10,5)
    #     self.assertEqual(result,2)
        
        #self.assertRaises(ValueError,calc.divide,10,0)
        #with self.assertRaises(ValueError):
        # calc.divide(20,0)

    # def test_05_Webpage(self):
    #     print("\nTestCase-5")
    #     driver = webdriver.Chrome()
    #     driver.get("http://www.google.com") 
    #     #driver.find_element(By.ID, 'APjFqb').send_keys('Elon Musk')
    #     print("\n Hiii...")
    #     expected_title="Google"
    #     actual_title=driver.title
    #     self.assertEqual(actual_title,expected_title)
    #     print(f"{expected_title}but{actual_title}")
        

    # def test_06_FindId(self):
    #     print("\nTestCase-6")
    #     driver = webdriver.Chrome()
    #     driver.get("http://www.google.com") 
    #     driver.maximize_window()
    #     driver.find_element(By.ID, 'APjFqb').send_keys('Elon Musk')
    #     print(driver.current_url)
    #     driver.find_element(By.CLASS_NAME,"gNO89b").click()
    #     time.sleep(4)
        

    """def test_title(self):
        print("\nTestCase-7")
        driver = webdriver.Chrome()
        driver.get("http://www.google.com") 
        print("\nHello")
        driver.find_element(By.ID, 'APjFqb').send_keys('Elon Musk')
        driver.find_element(By.CLASS_NAME,"gNO89b").click()
        time.sleep(4)
        expected_title = "Google"
        print("\n",expected_title)
        actual_title = driver.title
        print("actual_title",actual_title)
        self.assertEqual(actual_title, expected_title, f"Expected title: {expected_title}, but got: {actual_title}")
        print(f"Expected title: {expected_title}, but got: {actual_title}")"""
       

if __name__ =='__main__':
    unittest.main()
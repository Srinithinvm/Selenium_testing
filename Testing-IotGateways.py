import unittest
import test1
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.close()


class Testing(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome()
        self.driver.close()

    # def test_01_loginpg(self):# To check login page title
    #     self.driver.get("http://ruban.febinosolutions.com:5000")
    #     time.sleep(1)
    #     expected_title="Login"
    #     actual_title=self.driver.title
    #     self.assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}")

    # def test_02_signup(self):#to check the signup butn to redirect Register page
    #     self.driver.get("http://ruban.febinosolutions.com:5000")
    #     time.sleep(1) 
    #     self.driver.find_element(By.ID,'signup').click()
    #     expected_title="Register"
    #     actual_title=self.driver.title
    #     self.assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}")
    #     self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/div/p/a').click()
    #     expected_title="Login"
    #     actual_title=self.driver.title
    #     self.assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}")

    # def test_03_register_01(self):  # to check registration page with(Empty form )
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"username").send_keys("")
    #     self.driver.find_element(By.ID,"email").send_keys("")
    #     self.driver.find_element(By.ID,"password").send_keys("")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(10)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Email format wrong EX:ruban@gmail.com!"  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_03_register_02(self):  # to check registration page with( space )
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"username").send_keys(" ")
    #     self.driver.find_element(By.ID,"email").send_keys(" ")
    #     self.driver.find_element(By.ID,"password").send_keys(" ")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(10)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Email format wrong EX:ruban@gmail.com!"  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_03_register_03(self):  # to check registration page with( Invalid datas )
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"username").send_keys(" ")
    #     self.driver.find_element(By.ID,"email").send_keys("user@")
    #     self.driver.find_element(By.ID,"password").send_keys("sds")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(10)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Email format wrong EX:ruban@gmail.com!"  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_03_register_04(self):  # to check registration page with( Invalid username  )
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"username").send_keys(" ")
    #     self.driver.find_element(By.ID,"email").send_keys("user@gmail.com")
    #     self.driver.find_element(By.ID,"password").send_keys("Qwerty@123")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(10)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Space Not allowed!"  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_03_register_05(self):  # to check registration page with( Invalid email  )
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"username").send_keys("1")
    #     self.driver.find_element(By.ID,"email").send_keys("user1gmail.com")
    #     self.driver.find_element(By.ID,"password").send_keys("Qwerty@123")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(10)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Email format wrong EX:ruban@gmail.com!"  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_03_register_06(self):  # to check registration page with( Invalid email  )
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"username").send_keys("1")
    #     self.driver.find_element(By.ID,"email").send_keys("user1@")
    #     self.driver.find_element(By.ID,"password").send_keys("Qwerty@123")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(10)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Email format wrong EX:ruban@gmail.com!"  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_03_register_07(self):  # to check registration page with( Invalid password without numbers  )
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"username").send_keys("1")
    #     self.driver.find_element(By.ID,"email").send_keys("user1@gmail.com")
    #     self.driver.find_element(By.ID,"password").send_keys("Qwerty@")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(10)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Password must contain at least one Digit."  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_03_register_08(self):  # to check registration page with( Invalid password without Uppercase   )
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"username").send_keys("1")
    #     self.driver.find_element(By.ID,"email").send_keys("user1@gmail.com")
    #     self.driver.find_element(By.ID,"password").send_keys("353@")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(10)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Password must have at least one Uppercase Character."  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")


    # def test_03_register_09(self):  # to check registration page with( Invalid password without Lowercase  )
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"username").send_keys("1")
    #     self.driver.find_element(By.ID,"email").send_keys("user1@gmail.com")
    #     self.driver.find_element(By.ID,"password").send_keys("Q353@")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(10)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Password must have at least one Lowercase Character."  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_03_register_10(self):  # to check registration page with( Invalid password without Spl char  )
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,"username").send_keys("1")
    #     self.driver.find_element(By.ID,"email").send_keys("user1@gmail.com")
    #     self.driver.find_element(By.ID,"password").send_keys("Qwerty123")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(3)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Password must contain at least one Special Symbol."  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_03_register_11(self): #to create new User in the registration page
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     expected_title="Register"
    #     actual_title=self.driver.title
    #     self.assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}")
    #     self.driver.find_element(By.ID,"username").send_keys("USER")
    #     self.driver.find_element(By.ID,"email").send_keys("user@gmail.com")
    #     self.driver.find_element(By.ID,"password").send_keys("Qwerty@123")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(10)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Successfully Created!"  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_04_register_duplicate(self):# To Register the already existing User
    #     self.driver.get("http://ruban.febinosolutions.com:5000/register")
    #     time.sleep(1)
    #     expected_title="Register"
    #     actual_title=self.driver.title
    #     self.assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}")
    #     self.driver.find_element(By.ID,"username").send_keys("USER")
    #     self.driver.find_element(By.ID,"email").send_keys("user@gmail.com")
    #     self.driver.find_element(By.ID,"password").send_keys("Qwerty@123")
    #     self.driver.find_element(By.ID,"submit").click()
    #     self.driver.implicitly_wait(10)
    #     actual_text=self.driver.find_element(By.ID,"div").get_attribute('innerHTML')
    #     expected_text="Email already exists!"  
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")


    # def test_05_signin_01(self):#Invalid EmailID & Valid Password 
    #     self.driver.get("http://ruban.febinosolutions.com")
    #     time.sleep(1)
    #     emailText = self.driver.find_element(By.ID,'email')
    #     emailText.send_keys("user3")
    #     self.driver.find_element(By.ID,'password').send_keys("Qwerty@123")
    #     self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/button[1]').click()
    #     actual_text = emailText.get_attribute("validationMessage")
    #     time.sleep(1)
    #     self.assertTrue
    #     expected_text="Please include an '@' in the email address. 'user3' is missing an '@'."
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_05_signin_02(self):#Valid ID & Invalid Password
    #     self.driver.get("http://ruban.febinosolutions.com")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,'email').send_keys("user@gmail.com")
    #     self.driver.find_element(By.ID,'password').send_keys("123dsfs6789")
    #     self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/button[1]').click()
    #     time.sleep(3)
    #     expected_text="Wrong Password"
    #     actual_text=self.driver.find_element(By.ID,"alert").text
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_05_signin_03(self):#Invalid ID & Invalid Password 
    #     self.driver.get("http://ruban.febinosolutions.com")
    #     time.sleep(1)
    #     emailText = self.driver.find_element(By.ID,'email')
    #     emailText.send_keys("user3")
    #     self.driver.find_element(By.ID,'password').send_keys("Qw23sewdsw")
    #     self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/button[1]').click()
    #     actual_text = emailText.get_attribute("validationMessage")
    #     time.sleep(1)
    #     self.assertTrue
    #     expected_text="Please include an '@' in the email address. 'user3' is missing an '@'."
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_05_signin_04(self):#Valid Id & Valid Password 
    #     self.driver.get("http://ruban.febinosolutions.com")
    #     time.sleep(1)        
    #     self.driver.find_element(By.ID,'email').send_keys("user@gmail.com")
    #     self.driver.find_element(By.ID,'password').send_keys("Qwerty@123")
    #     self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/button[1]').click()
    #     time.sleep(3)
    #     expected_title="Dashboard"
    #     actual_title=self.driver.title
    #     self.assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}")

   
    # def test_07_dashboard(self):# To check sign in with url & check add button 

    #     self.driver.get("http://ruban.febinosolutions.com")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,'email').send_keys("user@gmail.com")
    #     self.driver.find_element(By.ID,'password').send_keys("Qwerty@123")
    #     self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/button[1]').click()
    #     time.sleep(3)
    #     expected_title="Dashboard"
    #     actual_title=self.driver.title
    #     actual_URL = self.driver.current_url
    #     self.assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}")
    #     self.driver.find_element(By.XPATH,'/html/body/div/div[2]/section[1]/div/div/div/div/div[1]/div/button').click()
    #     time.sleep(1)
    #     expected_title="Device Details"
    #     actual_title=self.driver.title
    #     expected_URL="http://ruban.febinosolutions.com/dashboard/4"
        
    #     self.assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}") 
    #     #self.assertEqual(expected_URL,actual_URL,f"expected title is {expected_URL} but got {actual_URL}")

    # def test_08_DevDetails(self):# To check device Details form page
    #     self.driver.get("http://ruban.febinosolutions.com/formEdited.html")  
    #     time.sleep(1)
    #     expected_title="Device Details"
    #     actual_title=self.driver.title
    #     self.assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}")           
        
    def test_08_DevDetails_validation_01(self):
        # self.driver.get("http://ruban.febinosolutions.com/formEdited.html")
        test1.dashboard()
        

        driver.find_element(By.ID,'cc-pament').send_keys("dfdgdgdgd")
        driver.find_element(By.ID,'cc-name').send_keys("")
        driver.find_element(By.ID,'cc-number').send_keys("")
        driver.find_element(By.ID,'cc-exp').send_keys("")
        driver.find_element(By.ID,'x_card_code').send_keys("")
        driver.find_element(By.XPATH,'//*[@id="payment-button"]').click()
        time.sleep(3)
        actual_text=driver.find_element(By.XPATH,'//*[@id="Alerts"]/div').text
        expected_text="Space is Not allowed!"
        assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")

    # def test_08_DevDetails_validation_02(self):
    #     self.driver.get("http://ruban.febinosolutions.com/formEdited.html")
    #     zoom_level = 0.75

    #     # Execute JavaScript to set the zoom level
    #     self.driver.execute_script(f"document.body.style.zoom='{zoom_level}'")
    #     time.sleep(3)
    #     self.driver.find_element(By.ID,'cc-pament').send_keys("     ")
    #     self.driver.find_element(By.ID,'cc-name').send_keys("   ")
    #     self.driver.find_element(By.ID,'cc-number').send_keys("   ")
    #     self.driver.find_element(By.ID,'cc-exp').send_keys("   ")
    #     self.driver.find_element(By.ID,'x_card_code').send_keys("   ")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,'payment-button').click()
    #     # self.driver.find_element(By.XPATH,'//*[@id="payment-button"]').click()
    #     time.sleep(3)
    #     self.assertTrue
    #     actual_text=self.driver.find_element(By.XPATH,'//*[@id="Alerts"]/div/a').get_attribute('innerHTML')
    #     expected_text="Please Fill form!"
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")
    #     print (self.driver.find_element(By.XPATH,'//*[@id="Alerts"]/div/a').get_attribute('innerHTML'))

    # def test_08_DevDetails_validation_03(self):
    #     self.driver.find_element(By.ID,'cc-pament').send_keys("534589")
    #     self.driver.find_element(By.ID,'cc-name').send_keys("354345")
    #     self.driver.find_element(By.ID,'cc-number').send_keys("456")
    #     self.driver.find_element(By.ID,'cc-exp').send_keys("456")
    #     self.driver.find_element(By.ID,'x_card_code').send_keys("4564")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,'payment-button').click()
    #     # self.driver.find_element(By.XPATH,'//*[@id="payment-button"]').click()
    #     time.sleep(3)
    #     self.assertTrue
    #     actual_text=self.driver.find_element(By.XPATH,'//*[@id="Alerts"]/div/a').get_attribute('innerHTML')
    #     expected_text="Device Successfully Added! If you want to redirect dashboard"
    #     self.assertEqual(expected_text,actual_text,f"expected alert is {expected_text} but got: {actual_text}")
    #     print (self.driver.find_element(By.XPATH,'//*[@id="Alerts"]/div/a').get_attribute('innerHTML'))
    #     self.find_element(By.XPATH,'//*[@id="Alerts"]/div/a').click()
    #     time.sleep(3)
    #     expected_title="Dashboard"
    #     actual_title=self.driver.title
    #     self.assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}")

    # def test_09_module(self):
    #     self.driver.get("http://ruban.febinosolutions.com")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,'email').send_keys("user@513")
    #     self.driver.find_element(By.ID,'password').send_keys("513")
    #     self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/button[1]').click()
    #     time.sleep(3)
    #     DeviceName="34"
    #     actual_name=self.driver.find_element(By.XPATH,'//*[@id="row"]/div[2]/div/h2').get_attribute('innerHTML')
    #     self.assertEqual(DeviceName,actual_name,f"expected name is {DeviceName} but got {actual_name}")
    
    # def test_10_details(self):
    #     self.driver.get("http://ruban.febinosolutions.com")
    #     time.sleep(1)
    #     self.driver.find_element(By.ID,'email').send_keys("user@gmail.com")
    #     self.driver.find_element(By.ID,'password').send_keys("Qwerty@123")
    #     self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div/div/div/button[1]').click()
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH,'//*[@id="row"]/div[2]/div/div[1]/a').click()
    #     time.sleep(1)
    #     expected_title="DeviceName"
    #     actual_title=self.driver.title
    #     self.assertEqual(expected_title,actual_title,f"expected title is {expected_title} but got {actual_title}") 

    # def test_10_details_01(self):
    #     actual_name=self.driver.find_element(By.XPATH,'/html/body/div/header[1]/div/div/div[2]/h2').get_attribute('innerHTML')
    #     DeviceName="34"
    #     self.assertEqual(actual_name,DeviceName,f"expected name is {DeviceName} but got {actual_name}")


    # def test_10_details_02(self):
    #     actual_id=self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div[1]/div/div[2]/div/table/tbody/tr[1]/td[3]').get_attribute('innerHTML')
    #     expected_id="43"
    #     self.assertEqual(actual_id,expected_id,f"expected title is {expected_id} but got: {actual_id}")
    #     actual_model=self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div[1]/div/div[2]/div/table/tbody/tr[2]/td[3]').get_attribute('innerHTML')
    #     expected_model="34"
    #     self.assertEqual(actual_model,expected_model,f"expected title is {expected_model} but got: {actual_model}")
    #     actual_hw=self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div[1]/div/div[2]/div/table/tbody/tr[3]/td[3]').get_attribute('innerHTML')
    #     expected_hw="34"
    #     self.assertEqual(actual_hw,expected_hw,f"expected title is {expected_hw} but got: {actual_hw}")
    #     actual_sw=self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div[1]/div/div[2]/div/table/tbody/tr[4]/td[3]').get_attribute('innerHTML')
    #     expected_sw="34"
    #     self.assertEqual(actual_sw,expected_sw,f"expected title is {expected_sw} but got: {actual_sw}")


    # def test_10_details_02(self):
    #     datatable = self.driver.find_element(By.XPATH,'//*[@id="datatable"]/tbody/tr[2]/td[1]').text
    # #     datatable = self.driver.find_element(By.XPATH,'//*[@id="datatable"]/tbody/tr[2]/td[2]').text
    #     # datatable = self.driver.find_element(By.XPATH,'/tbody/tr[2]/td[3]').text
        
    #     print(datatable)
    #     self.assertTrue

    # def test_10_details_03(self):
    # #     actual_num=self.driver.find_element(By.XPATH,'//*[@id="datatable"]/tbody/tr[1]/td[1]').get_attribute('innerHTML')
    # #     expected_num="1"
    # #     self.assertEqual(actual_num,expected_num,f"expected SNo is {expected_num} but got: {actual_num}")
    #     actual_date=self.driver.find_element(By.XPATH,'//*[@id="datatable"]/tbody/tr[1]/td[2]').get_attribute('innerHTML')
    #     expected_date="12-03-24"
    #     self.assertEqual(actual_date,expected_date,f"expected date is {expected_date} but got: {actual_date}")
    #     actual_data=self.driver.find_element(By.XPATH,'//*[@id="datatable"]/tbody/tr[1]/td[4]').get_attribute('innerHTML')
    #     expected_data="20"
    #     self.assertEqual(actual_data,expected_data,f"expected data is {expected_data} but got: {actual_data}")

    # def test_10_details_04(self):
    #     time.sleep(5)
    #     val=self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[4]/td[2]/label/span').get_attribute('value')
    #     print(val)
    #     # expected_val=False
    #     # self.assertEqual(val,expected_val,f"{expected_val} but got {val}")
    #     val=self.driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[1]/div[3]/div/div[2]/div/table/tbody/tr[2]/td[2]/label/span')
    #     # print(type(val.is_selected()))
    #     # print(val.is_selected())
    #     # if val.get_property("checked"):
    #     #     print("radio is checked")
    #     # else:
    #     #     print("not checked")
    #     #print(val)
    #     print(val.get_property("checked"))

    # def test_10_details_04(self):
    #     time.sleep(3)
    #     val=self.driver.find_element(By.ID,'radio8').is_selected()
    #     expected_val=False
    #     self.assertEqual(val,expected_val,f"{expected_val} but got {val}")
    #     val=self.driver.find_element(By.ID,'radio7').is_selected()
    #     expected_val=False
    #     self.assertEqual(val,expected_val,f"{expected_val} but got {val}")
    #     val=self.driver.find_element(By.ID,'radio6').is_selected()
    #     expected_val=True
    #     self.assertEqual(val,expected_val,f"{expected_val} but got {val}")               
    #     val=self.driver.find_element(By.ID,'radio5').is_selected()
    #     expected_val=False
    #     self.assertEqual(val,expected_val,f"{expected_val} but got {val}")
    #     val=self.driver.find_element(By.ID,'radio4').is_selected()
    #     expected_val=True
    #     self.assertEqual(val,expected_val,f"{expected_val} but got {val}")
    #     val=self.driver.find_element(By.ID,'radio3').is_selected()
    #     expected_val=False
    #     self.assertEqual(val,expected_val,f"{expected_val} but got {val}")
    #     val=self.driver.find_element(By.ID,'radio2').is_selected()
    #     expected_val=False
    #     self.assertEqual(val,expected_val,f"{expected_val} but got {val}")
    #     val=self.driver.find_element(By.ID,'radio1').is_selected()
    #     expected_val=False
    #     self.assertEqual(val,expected_val,f"{expected_val} but got {val}")        

    # def test_11_z(self):
    #     self.driver.get("http://ruban.febinosolutions.com/deleteuser?email_id=user@gmail.com") #//*[@id="datatable"]  /tbody/tr[2]/td[3]

if __name__ == "__main__":
    unittest.main(verbosity=2)
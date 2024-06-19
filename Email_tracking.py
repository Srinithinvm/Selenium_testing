import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Testing(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()  # Maximize the browser window
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
    # def test_TS_01_header(self):
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(5)
        
    #     expected_title = "Andon System"
    #     actual_title = self.driver.title
    #     self.assertEqual(expected_title, actual_title, f"Expected title is '{expected_title}' but got '{actual_title}'")
    #     print("Test TS_01_header passed...")
        
    # def test_TS_01_header_001(self):
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(5)
        
    #     logout_button = self.driver.find_element(By.CLASS_NAME, 'header-nav ms-3')
    #     logout_button.click()
    #     self.driver.implicitly_wait(5)
    #     logout_link = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[1]/ul[3]/li/ul/li/a')
    #     logout_link.click()
    #     time.sleep(3)
    #     expected_url = "http://do.febinosolutions.com:3000/#/login"
    #     actual_url = self.driver.current_url
    #     self.assertEqual(expected_url, actual_url, f"Expected URL is '{expected_url}' but got '{actual_url}'")
    #     print(expected_url,actual_url)
    #     print("Test TS_header_001 passed...")

    # def test_TS_01_header_002(self):
    #     home_button = self.driver.find_element(By.CLASS_NAME, 'breadcrumb-item').click()
    #     expected_url="http://do.febinosolutions.com:3000/#/dashboard"
    #     actual_url = self.driver.current_url
    #     self.assertEqual(expected_url, actual_url, f"Expected URL is '{expected_url}' but got '{actual_url}'")
    #     # print({expected_url},{actual_url})
    #     # print("Test TS_header_002 passed...") if expected_url == actual_url else print("Failed")

    # def test_TS_02_dashboard(self):#to verify dashboard page
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(5)
        
    # def test_TS_02_dashboard_001(self):# to check weather the mail box count increases or not after receiving mail
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(5)
    #     count_value=self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]').get_attribute('innerHTML')
    #     print(count_value)
    #     count_value=int(count_value)+1
    #     self.driver.quit()
        
    #     #Send a mail...

    #     self.driver = webdriver.Chrome() 
    #     time.sleep(13)
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(5)
    #     current_value=self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]').get_attribute('innerHTML')
    #     print(current_value)
        
    #     if current_value == count_value:
    #         print("test_TS_02_dashboard_001 - Passed...")
    #     else:
    #         print("test_TS_02_dashboard_001 - Failed...")
    #     self.driver.quit()
    
    # def test_TS_02_dashboard_002(self):#to check weather the mail count decreases or not after deleting inbox mail
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(3)
    #     count_value=self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]').get_attribute('innerHTML')
    #     print(count_value)
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/emailtable")
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/button').click()
    #     time.sleep(3)
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(3)
    #     current_value=self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div[1]').get_attribute('innerHTML')
    #     print(current_value)
    #     if int(current_value) == int(count_value)-1:
    #         print("test_TS_02_dashboard_002 - Passed...")
    #     else:
    #         print("test_TS_02_dashboard_002 - Failed...")
    #     self.driver.quit()

    # def test_TS_02_dashboard_003(self):#to check the count of ticket box increases or not
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(3)
    #     ticket_value=self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]').get_attribute('innerHTML')
    #     print(ticket_value)
    #     self.driver.quit()

    #     #SEND MAIL WITH TICKET

    #     self.driver = webdriver.Chrome()
    #     time.sleep(13)
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(5)
    #     current_value=self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]').get_attribute('innerHTML')
    #     print(current_value)
    #     if int(current_value) == int(ticket_value)+1:
    #         print("test_TS_02_dashboard_003 - Passed...")
    #     else:
    #         print("test_TS_02_dashboard_003 - Failed...")
    #     self.driver.quit()
        
    # def test_TS_02_dashboard_004(self):#to check the count of ticket box when there's no ticket in a mail
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(3)
    #     ticket_value=self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]').get_attribute('innerHTML')
    #     print(ticket_value)
    #     self.driver.quit()

    #     #SEND MAIL  WITHOUT TICKET

    #     self.driver = webdriver.Chrome()
    #     time.sleep(13)
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(5)
    #     current_value=self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]').get_attribute('innerHTML')
    #     print(current_value)
    #     if current_value == ticket_value:
    #         print("test_TS_02_dashboard_004 - Passed...")
    #     else:
    #         print("test_TS_02_dashboard_004 - Failed...")
    #     self.driver.quit() 
        
    # def test_TS_02_dashboard_005(self):#to check weather the count of the ticket box decreases or not after deleting a ticket
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(3)
    #     ticket_value=self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]').get_attribute('innerHTML')
    #     print(ticket_value)
    #     self.driver.quit()
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/emailtable")
    #     time.sleep(3)
    #     self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/button').click()
    #     time.sleep(3)
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(3)
    #     current_value=self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/div[1]').get_attribute('innerHTML')
    #     print(current_value)
    #     if int(current_value) == int(ticket_value)-1:
    #         print("test_TS_02_dashboard_005 - Passed...")
    #     else:
    #         print("test_TS_02_dashboard_005 - Failed...")
    #     self.driver.quit()

    # def test_TS_02_dashboard_006(self):#to check the ticket table when there is no ticket in the mail its adding or not
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(3)
    #     ticket = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div/table/tbody/tr[1]/td[1]').get_attribute('innerHTML')
    #     print(ticket)
    #     self.driver.quit()

    #     #Send mail without ticket

    #     self.driver = webdriver.Chrome()
    #     time.sleep(5)
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(3)
    #     ticketnum = self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div/table/tbody/tr[1]/td[1]').get_attribute('innerHTML')
    #     print(ticketnum)
    #     if ticket == ticketnum:
    #         print("test_TS_02_dashboard_006 - Passed...")
    #     else:
    #         print("test_TS_02_dashboard_006 - Failed...")
    #     self.driver.quit()

    # def test_TS_02_dashboard_007(self):#to check the ticket table delete button
    #     #send mail
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/dashboard")
    #     time.sleep(3)
    #     before_action = self.driver.find_element(By,'//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]').get_attribute('innerHTML')
    #     time.sleep(3)
    #     print(before_action)
    #     self.driver.find_element(By,'//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/button').click()
    #     time.sleep(3)
    #     after_action = self.driver.find_element(By,'//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]').get_attribute('innerHTML')
    #     print(after_action)
    #     if before_action == after_action:
    #         print("test_TS_02_dashboard_007 - Passed...")
    #     else:
    #         print("test_TS_02_dashboard_007 - Failed...")
    #     self.driver.quit()

    # ###def test_TS_02_dashboard_008(self):#to check weather the field is adding or not after creating it
    #     self.driver.get("http://do.febinosolutions.com:3000/#/emailtracking/parameter")
    #     time.sleep(3)
    #     self.driver.find_element(By,'//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]/button').click()
    #     self.driver.implicitly_wait(10)
    #     time.sleep(5)
    #     self.driver.find_element(By,'//*[@id="alias"]').send_keys("sample")
    #     self.driver.find_element(By,'//*[@id="field"]').send_keys("color")
    #     self.driver.find_element(By,'//*[@id="datatype"]').click()
    #     self.driver.find_element(By,'//*[@id="datatype"]/option[2]').click()
    #     self.driver.find_element(By,'//*[@id="groups"]/option[2]').click()


    # ##def test_TS_02_dashboard_009(self):#to check weather the field is adding according to its field or not
    #     self.driver.get('http://do.febinosolutions.com:3000/#/emailtracking/dashboard')
    #     time.sleep(3)
    #     trigger_value = self.driver.find_element(By,'//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div/table/tbody/tr[1]/td[3]').get_attribute('innerHTML')
    #     print(trigger_value)
    #     self.driver.quit()
    #     #send MAIL
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('http://do.febinosolutions.com:3000/#/emailtracking/dashboard')
    #     time.sleep(3)
    #     ntrigger_value = send.driver.find_element(By,'//*[@id="root"]/div/div[2]/div[2]/div/div[3]/div/div/div[2]/div/table/tbody/tr[1]/td[3]').get_attribute('innerHTML')
    #     print(ntrigger_value)
        

    # def test_08_group_001(self):# to check the search box without inputs
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     time.sleep(3)
    #     search_input = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/input')
    #     search_input.send_keys("")
    #     time.sleep(3)
    #     search_button = self.driver.find_element(By.XPATH, '//*[@id="button-addon2"]')
    #     search_button.click()
    #     time.sleep(3)

    # def test_08_group_002(self):#to search with valid datas
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     time.sleep(3)
    #     search_input = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/input')
    #     search_input.send_keys("Group - 1")
    #     time.sleep(3)
    #     search_button = self.driver.find_element(By.XPATH, '//*[@id="button-addon2"]')
    #     search_button.click()
    #     time.sleep(3)
    #     search_result_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]')
    #     search_result_text = search_result_element.get_attribute('innerHTML')
    #     print( search_result_text)
    #     expected_search_text = "Group - 1"
    #     self.assertEqual(search_result_text, expected_search_text, f"Expected '{expected_search_text}' but got '{search_result_text}'")
    #     if search_result_text == expected_search_text:
    #         print("test_08_group_002 - Passed...")
    #     else:
    #         print("test_08_group_002 - Failed...")

    
    # def test_08_group_003(self):#to search with valid datas(user ID)
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     time.sleep(3)
    #     search_input = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/input')
    #     search_input.send_keys("karthik202m@gmail.com")
    #     time.sleep(3)
    #     search_button = self.driver.find_element(By.XPATH, '//*[@id="button-addon2"]')
    #     search_button.click()
    #     time.sleep(3)
    #     search_result_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]')
    #     search_result_text = search_result_element.get_attribute('innerHTML')
    #     print( search_result_text)
    #     expected_search_text = "karthik202m@gmail.com"
    #     self.assertEqual(search_result_text, expected_search_text, f"Expected '{expected_search_text}' but got '{search_result_text}'")
    #     if search_result_text == expected_search_text:
    #         print("test_08_group_003 - Passed...")
    #     else:
    #         print("test_08_group_003 - Failed...")

   ### def test_08_group_004(self):#to search with Invalid datas(user ID)
        # self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
        # time.sleep(3)
        # search_input = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/input')
        # search_input.send_keys("srin@gmail.com")
        # time.sleep(3)
        # try:
        #     browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]')
        # except NoSuchElementException as e:
        #     print('No Such Element has occurred')
        #     pass
        # search_button = self.driver.find_element(By.XPATH, '//*[@id="button-addon2"]')
        # search_button.click()
        # time.sleep(3)
        # search_result_element = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]')
        # search_result_text = search_result_element.get_attribute('innerHTML')
        # print( search_result_text)
        # expected_search_text = "srin@gmail.com"
        # self.assertEqual(search_result_text, expected_search_text, f"Expected '{expected_search_text}' but got '{search_result_text}'")
        # if search_result_text != expected_search_text:
        #     print("test_08_group_004 - Passed...")
        # else:
        #     print("test_08_group_004 - Failed...")

    # def test_08_group_005(self):#to check the edit button
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[4]/div/button[1]')))
    #     edit_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[4]/div/button[1]')
    #     edit_button.click()
    #     WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[1]/h5')))
    #     module = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/h5')
    #     actual_text = module.get_attribute('innerHTML').strip()
    #     expected_text = "Groups Details"
    #     self.assertEqual(actual_text, expected_text, f"Expected '{expected_text}' but got '{actual_text}'")
    #     print(actual_text,expected_text)
    #     if actual_text == expected_text:
    #         print("test_08_group_005 - Passed...")
    #     else:
    #         print("test_08_group_005 - Failed...")

    # def test_08_groups_006(self):#to check weather the create button brings create module or not
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     create_button = WebDriverWait(self.driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/button')))
    #     create_button.click()
    #     WebDriverWait(self.driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[1]/h5')))
    #     module = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[1]/h5')
    #     actual_text = module.get_attribute('innerHTML').strip()  # Use strip() to remove any leading/trailing whitespace
    #     expected_text = "Create New Group"
    #     self.assertEqual(actual_text, expected_text, f"Expected '{expected_text}' but got '{actual_text}'")
    #     if actual_text == expected_text:
    #         print("test_08_groups_006 - Passed...")
    #     else:
    #         print("test_08_groups_006 - Failed...")


    # def test_08_groups_007(self):# to check  weather is group is creating with empty space or not
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     create_button = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/button'))
    #     )
    #     create_button.click()
    #     group_name_input = self.driver.find_element(By.XPATH, '//*[@id="newGroupName"]')
    #     group_name_input.send_keys("")  # Group name with  spaces
    #     user_option = self.driver.find_element(By.XPATH, '//*[@id="newUserList"]/option[3]')
    #     user_option.click()
    #     try:
    #         submit_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[3]/div'))
    #         )
    #         submit_button.click()
    #     except NoSuchElementException as e:
    #         print("Element not found:", e)
    #         raise
    #     self.driver.quit()

    #     self.driver=webdriver.Chrome()
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]'))
    #     )
    #     check = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]').get_attribute('innerHTML')
    #     print("Inner HTML:", check)
    #     if check != "":
    #         print("test_08_groups_007 - Passed...")
    #     else:
    #         print("test_08_groups_007 - Failed...")


    # def test_08_groups_008(self):# to check  weather is group is creating with empty space or not
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     create_button = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/button'))
    #     )
    #     create_button.click()
    #     group_name_input = self.driver.find_element(By.XPATH, '//*[@id="newGroupName"]')
    #     group_name_input.send_keys("  ")  # Group name with  spaces
    #     user_option = self.driver.find_element(By.XPATH, '//*[@id="newUserList"]/option[3]')
    #     user_option.click()
    #     try:
    #         submit_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[3]/div'))
    #         )
    #         submit_button.click()
    #     except NoSuchElementException as e:
    #         print("Element not found:", e)
    #         raise
    #     self.driver.quit()

    #     self.driver=webdriver.Chrome()
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]'))
    #     )
    #     check = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]').get_attribute('innerHTML')
    #     print("Inner HTML:", check)
    #     if check != " ":
    #         print("test_08_groups_008 - Passed...")
    #     else:
    #         print("test_08_groups_008 - Failed...")

    # def test_08_groups_009(self):#to check weather the created field is displayed on the table or not
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     create_button = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/button'))
    #     )
    #     create_button.click()
    #     group_name_input = self.driver.find_element(By.XPATH, '//*[@id="newGroupName"]')
    #     group_name_input.send_keys("CSK")  # Group name with  spaces
    #     user_option = self.driver.find_element(By.XPATH, '//*[@id="newUserList"]/option[3]')
    #     user_option.click()
    #     try:
    #         submit_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[3]/div'))
    #         )
    #         submit_button.click()
    #     except NoSuchElementException as e:
    #         print("Element not found:", e)
    #         raise
    #     self.driver.quit()
    #     self.driver=webdriver.Chrome()
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]'))
    #     )
    #     check = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]').get_attribute('innerHTML')
    #     print("Inner HTML:", check)
    #     if check == "CSK":
    #         print("test_08_groups_009 - Passed...")
    #     else:
    #         print("test_08_groups_009 - Failed...")

    # def test_08_groups_010(self):#to check weather the delete option deletes the group or not
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]'))
    #     )
    #     check1 = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]').get_attribute('innerHTML')
    #     print("Inner HTML[Before_deletion]:", check1)
    #     delete_button = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[4]/div/button[2]'))
    #     )
    #     delete_button.click()
    #     self.driver.quit()
    #     self.driver=webdriver.Chrome()
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]'))
    #     )
    #     check2 = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]').get_attribute('innerHTML')
    #     print("Inner HTML[After_deletion]:", check2)
    #     if check1 != check2:
    #         print("test_08_groups_010 - Passed...")
    #     else:
    #         print("test_08_groups_010 - Failed...")

    # def test_08_groups_011(self):#to check Is the group is creating when no user is selected for group 
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     create_button = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/button'))
    #     )
    #     create_button.click()
    #     group_name_input = self.driver.find_element(By.XPATH, '//*[@id="newGroupName"]')
    #     group_name_input.send_keys("RCB")
    #     try:
    #         submit_button = WebDriverWait(self.driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div/div/div[2]/form/div[3]/div'))
    #         )
    #         submit_button.click()
    #     except NoSuchElementException as e:
    #         print("Element not found:", e)
    #         raise
    #     self.driver.quit()

    #     self.driver=webdriver.Chrome()
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]'))
    #     )
    #     check = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody/tr[1]/td[1]').get_attribute('innerHTML')
    #     print("Inner HTML:", check)
    #     if check == "RCB":
    #         print("test_08_groups_011 - Failed[Group without members cannot be created]")
    #     else:
    #         print("test_08_groups_011 - Passed")

    # ###def test_08_groups_012(self):
    #     self.driver.get("http://do.febinosolutions.com:3000/#/users/groups")
    #     search_input = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/input'))
    #     )
    #     search_input.send_keys("RCB")
    #     time.sleep(3)
    #     # search_button = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div/button')
    #     # search_button.click()
    #     WebDriverWait(self.driver, 10).until(
    #         EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody'))
    #     )
    #     search_results = self.driver.find_elements(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[2]/table/tbody')
    #     self.assertGreater(len(search_results), 0, "Search did not return any results")
    #     print(search_results)
    #     print("Test case TS_group_012 passed: Search functionality verified successfully.")


if __name__ == "__main__":
    unittest.main(verbosity=2)

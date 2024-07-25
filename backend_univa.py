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
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_TS_01_login_to_site(self):
        self.driver.get("https://productionb.univa.cloud/admin/")

        username = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/form/div[1]/input"))
        )
        username.send_keys("admin")

        password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/div[2]/div/form/div[2]/input"))
        )
        password.send_keys("admin")

        login = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div/form/div[3]/div/button"))
        )
        login.click()
        time.sleep(3)
        Expected_result="Django administration"
        Actual_result=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-logo"]/span'))
        ).get_attribute("innerHTML")
        self.assertEqual(Expected_result,Actual_result,f"Expected result is {Expected_result} but got {Actual_result}")
       
        print("Element found, Test TS_01_Admin_panel_login_to_site passed...")
        
        
    def test_TS_02_Device_details_001(self):#to check weather the device details page is locating...

        self.driver.get("https://productionb.univa.cloud/admin/")
        time .sleep(3)
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-sidebar"]/div/nav/ul/li[16]/a'))
        ).click()
        Expected_result=" Device detailss "
        Actual_result=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div[1]/h1'))
        ).get_attribute('innerHTML')
        self.assertEqual(Expected_result,Actual_result,f"Expected result is {Expected_result} but got {Actual_result}")
        print("Element found, Test TS_01_Device_details_001 passed...")

    def test_TS_02_Device_details_002(self):#to check add device page
        self.driver.get("https://productionb.univa.cloud/admin/devices/devicedetails/")
        time.sleep(3)
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div/div[1]/div[1]/div/div/div[2]/a"))
        ).click()
        Expected_page="Add device details"
        Actual_page=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[4]'))
        ).text
        self.assertEqual(Expected_page,Actual_page,f"Expected result is {Expected_page} but got {Actual_page}")
        print("TS_02_Device_details_002...Passed")

    def test_TS_02_Device_details_003(self):# to check the error message for each req field
        self.driver.get("https://productionb.univa.cloud/admin/devices/devicedetails/add/")
        save_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[1]/input'))
        ).click()
        popup_error=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="devicedetails_form"]/div[1]'))
        ).get_attribute('innerHTML')
        Expected_msg="Please correct the errors below."
        Actual_msg=popup_error
        # self.assertEqual(Expected_msg,Actual_msg,f"Expected message is {Expected_msg} but got {Actual_msg}")
        error1=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="devicedetails_form"]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/ul/li'))
        ).get_attribute('innerHTML')
        error2=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="devicedetails_form"]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/ul/li'))
        ).get_attribute('innerHTML')
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="devicedetails_form"]/div[2]/div[1]/div/div/div[5]/div/div/div[2]/ul/li'))
        ).get_attribute('innerHTML')
        Expected_error="This field is required."
        if(Expected_error==error1==error2):
            print("TS_02_Device_details_003....Passed")
        
        else:
            print("TS_02_Device_details_003....Failed")





    def test_TS_02_Device_details_004(self):#to check adding device

        self.driver.get("https://productionb.univa.cloud/admin/devices/devicedetails/add/")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_device_name"]'))
        ).send_keys("Device10")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_device_token"]'))
        ).send_keys("device-token-10")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_hardware_version"]'))
        ).send_keys("1.2")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_software_version"]'))
        ).send_keys("1.2")

        dropdown_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-id_protocol-container"]'))
        )
        dropdown_btn.click()
        time.sleep(3)

        protocol_options_locator = (By.ID, "select2-id_protocol-results")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(protocol_options_locator)
        )

        # Retry logic for stale elements
        for _ in range(3):  # Retry up to 3 times
            # try:
                protocol_options = self.driver.find_element(*protocol_options_locator)
                options = protocol_options.find_elements(By.TAG_NAME, 'li')

                protocol_selected = False  # Flag to track if the desired protocol is selected

                for option in options:
                    option_text = option.text  # Use `text` instead of `innerHTML`
                    # print(option_text)
                    if option_text == "MQTT":
                        option.click()
                        protocol_selected = True
                        break

                if protocol_selected:
                    break  # Exit retry loop if successful



        pub_topic=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="id_pub_topic"]'))
        ).send_keys("device1response")
        sub_topic=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="id_sub_topic"]'))
        ).send_keys("device1request")
        save_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[1]/input'))
        ).click()
        #to check pop up for successfully added..
        popup_msg=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/div[1]'))
        ).get_attribute('innerHTML')
        Actual_popup=popup_msg
        Expected_popup="The device details “Device10” was added successfully."
        # self.assertEqual(Expected_popup,Actual_popup,f"Expected message is {Expected_popup} but got {Actual_popup}")
        #to check the device is added to the table...
        self.driver.get("https://productionb.univa.cloud/admin/devices/devicedetails/")
        time.sleep(3)
        device_at_table=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th'))
        ).text
        self.assertEqual("Device10",device_at_table,f"Expected result is Device10 but got {device_at_table}")
        print("Device is added to the table...")
        print("TS_02_Device_details_004...Passed")



        
    def test_TS_02_Device_details_005(self):#to check adding device with the existiting device token  
        self.driver.get("https://productionb.univa.cloud/admin/devices/devicedetails/add/")
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_device_token"]'))
        ).send_keys("device-token-10")
        save_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[1]/input'))
        ).click()
        Actual_error=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="devicedetails_form"]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/ul/li'))
        ).get_attribute('innerHTML')
        Expected_error="Device details with this Device token already exists."
        self.assertEqual(Expected_error,Actual_error,f"Expected error is {Expected_error} but got {Actual_error}")
        print("TS_02_Device_details_005...passed")
    
    def test_TS_02_Device_details_006(self):# to check the working of save and add another button
        self.driver.get("https://productionb.univa.cloud/admin/devices/devicedetails/add/")
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_device_name"]'))
        ).send_keys("Device11")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_device_token"]'))
        ).send_keys("device-token-11")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_hardware_version"]'))
        ).send_keys("1.2")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_software_version"]'))
        ).send_keys("1.2")

        dropdown_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-id_protocol-container"]'))
        )
        dropdown_btn.click()
        time.sleep(3)

        protocol_options_locator = (By.ID, "select2-id_protocol-results")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(protocol_options_locator)
        )

        # Retry logic for stale elements
        for _ in range(3):  # Retry up to 3 times
            # try:
                protocol_options = self.driver.find_element(*protocol_options_locator)
                options = protocol_options.find_elements(By.TAG_NAME, 'li')

                protocol_selected = False  # Flag to track if the desired protocol is selected

                for option in options:
                    option_text = option.text  # Use `text` instead of `innerHTML`
                    # print(option_text)
                    if option_text == "MQTT":
                        option.click()
                        protocol_selected = True
                        break

                if protocol_selected:
                    break  # Exit retry loop if successful






        pub_topic=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="id_pub_topic"]'))
        ).send_keys("device1response")
        sub_topic=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="id_sub_topic"]'))
        ).send_keys("device1request")
        save_and_addanother=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[2]/input'))
        ).click()
        #to check weather it shows the add device page for adding another device
        Expected_url="https://productionb.univa.cloud/admin/devices/devicedetails/add/"
        Actual_url=self.driver.current_url
        self.assertEqual(Expected_url,Actual_url,f"Expected url is {Expected_url} but got {Actual_url}")
        #to check weather the device is added in the table
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[3]/a'))
            ).click()
        device_at_table=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th'))
        ).text
        self.assertEqual("Device11",device_at_table,f"Expected result is Device10 but got {device_at_table}")
        print("Device is added to the table...")
        print("TS_02_Device_details_006...passed")

    def test_TS_02_Device_details_007(self):# to check the working of save and add another button
        self.driver.get("https://productionb.univa.cloud/admin/devices/devicedetails/add/")
        time.sleep(3)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_device_name"]'))
        ).send_keys("Device12")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_device_token"]'))
        ).send_keys("device-token-12")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_hardware_version"]'))
        ).send_keys("1.2")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_software_version"]'))
        ).send_keys("1.2")

        dropdown_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="select2-id_protocol-container"]'))
        )
        dropdown_btn.click()
        time.sleep(3)

        protocol_options_locator = (By.ID, "select2-id_protocol-results")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(protocol_options_locator)
        )

        # Retry logic for stale elements
        for _ in range(3):  # Retry up to 3 times
            # try:
                protocol_options = self.driver.find_element(*protocol_options_locator)
                options = protocol_options.find_elements(By.TAG_NAME, 'li')

                protocol_selected = False  # Flag to track if the desired protocol is selected

                for option in options:
                    option_text = option.text  # Use `text` instead of `innerHTML`
                    # print(option_text)
                    if option_text == "MQTT":
                        option.click()
                        protocol_selected = True
                        break

                if protocol_selected:
                    break  # Exit retry loop if successful

        pub_topic=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="id_pub_topic"]'))
        ).send_keys("device1response")
        sub_topic=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="id_sub_topic"]'))
        ).send_keys("device1request")
        save_and_editing=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[3]/input'))
        ).click()
        
        #to check weather the device is added in the table
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[3]/a'))
            ).click()
        device_at_table=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th'))
        ).text
        self.assertEqual("Device12",device_at_table,f"Expected result is Device10 but got {device_at_table}")
        print("Device is added to the table...")

        #to check edit the device page
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th/a'))
        ).click()
        Expected_devicepg="Device12"
        Actual_devicepg=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[4]'))
        ).text
        self.assertEqual(Expected_devicepg,Actual_devicepg,f"Expected page is {Expected_devicepg} but got {Actual_devicepg}")

        Device_name=WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_device_name"]'))
        )
        Device_name.clear()
        Device_name.send_keys("Device12(new)")

        Device_token=WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_device_token"]'))
        )
        Device_token.clear()
        Device_token.send_keys("device-token-12(new)")

        Hardware=WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_hardware_version"]'))
        )
        Hardware.clear()
        Hardware.send_keys("1.2(new)")

        Software=WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_software_version"]'))
        )
        Software.clear()
        Software.send_keys("1.2(new)")
        save_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[1]/input'))
        ).click()
        device_at_table=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th'))
        ).text
        self.assertEqual("Device12(new)",device_at_table,f"Expected result is Device10 but got {device_at_table}")
        print("Device is added to the table...")

        print("TS_02_Device_details_007...passed")

    def test_TS_02_Device_details_008(self):#to delete the device
        self.driver.get("https://productionb.univa.cloud/admin/devices/devicedetails")
        time.sleep(3)   
        device_at_table=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th'))
        )
        Expected_device=device_at_table.text
        device_at_table.click()
        Actual_device=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[4]'))
        ).text
        self.assertEqual(Expected_device,Actual_device,f"Expected device is {Expected_device} but got {Actual_device}")
        #to check the delete page is shown
        delete_btn=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div[1]/div[2]/a'))
        )
        delete_btn.click()
        Actual_page=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[5]'))
        ).text
        Expected_page="Delete"
        self.assertEqual(Expected_page,Actual_page,f"Expected page is {Expected_page} but got {Actual_page}")

        device_name=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="content-main"]/div/div[1]/ol/li/a'))
        ).text
        self.assertEqual(Expected_device,device_name,f"Expected device at delete page is {Expected_device} but got {device_name}")
        delete_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="content-main"]/div/div[2]/form/div[1]/input'))
        )
        delete_button.click()
        device_at_table=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th'))
        )
        self.assertNotEqual(device_at_table,device_name)
        print("TS_02_Device_details_008...passed")
    

    def test_TS_02_Device_details_009(self):#to check the history section
        # Navigate to the device details page
        self.driver.get("https://productionb.univa.cloud/admin/devices/devicedetails")

        # Wait for the device table to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result_list"]'))
        )

        # Click on the first device in the table
        device_at_table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result_list"]/tbody/tr[1]/th/a'))
        )

        Expected_device = device_at_table.text
        device_at_table.click()

        # Wait for the history button to be visible and click it
        history_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jazzy-actions"]/div[2]/a'))
        )
        history_btn.click()

        # Wait for the history page elements to be present and get their text
        # device_chk = WebDriverWait(self.driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/ol/li[4]/a'))
        # ).text


        # history_chk = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/ol/li[5]'))
        # ).text
        # print(history_chk)

        # Assertions to verify the expected results
        # self.assertEqual(Expected_device, device_chk, f"Expected device {Expected_device} but got {device_chk}")
        # self.assertEqual("History", history_chk, f"Expected page is 'History' but got {history_chk}")

        print("TS_02_Device_details_009... Passed")


    def test_TS_02_Device_details_010(self):#to check the search results
        self.driver.get("https://productionb.univa.cloud/admin/devices/devicedetails/")
        time.sleep(3)
        searchbox=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="searchbar"]'))
        )
        searchbox.send_keys("Device1")
        search_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="search_group"]/button'))
        )
        search_button.click()
        time.sleep(3)
        search_results=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th'))
        )
        Actual_result=search_results.text
        Expected_result="Device1"
        print("Currently its low priority..")
        self.assertEqual(Expected_result,Actual_result,f"Expected result is {Expected_result} but got {Actual_result}")
        
        print("TS_02_Device_details_010...Passed")
        

    def test_TS_03_Machine_details_001(self):#to check add machine details weather unwanted text at the Machine name
        self.driver.get("https://productionb.univa.cloud/admin/devices/machinedetails/")
        time.sleep(3)
        #to check the machine details page
        page=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div[1]/ol/li[3]'))).text
        self.assertEqual("Machine detailss",page,f"Expected page is Machine detailss but got {page}")
        add_machine=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div[2]/a')))
        add_machine.click()
        #to check the add machine device page
        page2=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[4]'))).text
        self.assertEqual("Add machine details",page2,f"Expected page is Add machine details but got {page2}")
        Machine_name=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="id_machine_name"]'))) 
        Actual_result=Machine_name.get_attribute("value")       
        self.assertEqual("",Actual_result,f"Expected value is empty space but got some text like {Actual_result}")
        print("TS_03_Machine_details_001...Passed")
        
    def test_TS_03_Machine_details_002(self):#to check add machine details without any input datas and for error message in req field
        self.driver.get("https://productionb.univa.cloud/admin/devices/machinedetails/add/")
        time.sleep(3)
        save_button=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="jazzy-actions"]/div/div[1]/input')))
        save_button.click()
        #check for error message
        error1=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="machinedetails_form"]/div[2]/div[1]/div/div/div[1]/div/div/div[2]/ul/li')))
        error2=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="machinedetails_form"]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/ul/li')))
        error3=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="machinedetails_form"]/div[2]/div[1]/div/div/div[6]/div/div/div[3]/ul/li')))
        result=False
        if  error1.text=="This field is required." and error2.text=="This field is required." and error3.text=="This field is required.":
            result=True
        self.assertEqual("True",str(result),f"Expected error message is not appeared")
        #to check error popup
        Actual_popup=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="machinedetails_form"]/div[1]'))).text
        Expected_popup="Please correct the errors below."
        self.assertEqual(Expected_popup,Actual_popup,f"Expected error message is {Expected_popup} but got {Actual_popup} ")
        print("TS_03_Machine_details_002...Passed")

    def test_TS_03_Machine_details_003(self):#to check add machine details and weather it displayed at the table
        self.driver.get("https://productionb.univa.cloud/admin/devices/machinedetails/")
        time.sleep(3)
        add_machine=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div[2]/a')))
        add_machine.click()
        machine_name=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_machine_name"]')))
        machine_id=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_machine_id"]')))
        line=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_line"]')))
        manufacture=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_manufacture"]')))
        year=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_year"]')))
        device=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="select2-id_device-container"]')))
        machine_name.send_keys("Machine1")
        machine_id.send_keys("machineid-1")
        line.send_keys("one")
        manufacture.send_keys("manufact")
        year.send_keys("2024")
        device.click()
        options=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="select2-id_device-results"]')))
        option=options.find_elements(By.TAG_NAME,"li")

        for opt in option:
            opt_text=opt.text
            
            if opt_text=="Device11":
                print(opt_text)
                path=opt.get_attribute('id')
                print(path)
                opt.click()
                break
            time.sleep(3)
        res=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="select2-id_device-container"]'))).text
        print(res)  
        time.sleep(5)      
        production=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="id_production_per_hour"]')))
        production.send_keys("10")
        save_button=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[1]/input')))
        save_button.click()
        machine_at_table=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th')))
        machine_line=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/td[2]')))
        machine_manuf=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/td[3]')))
        machine_year=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/td[4]')))
        machine_device=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/td[5]')))
        self.assertEqual(machine_at_table.text,"machineid-1",f"Expected machine ID is not displayed at the table")
        self.assertEqual(machine_line.text,"one",f"Expected machine line is not displayed at the table")
        self.assertEqual(machine_manuf.text,"manufact",f"Expected machine manufacture is not displayed at the table")
        self.assertEqual(machine_year.text,"2024",f"Expected machine year is not displayed at the table")
        self.assertEqual(machine_device.text,"Device11",f"Expected machine device is not displayed at the table")
        print("TS_03_Machine_details_003...Passed")

    def test_TS_03_Machine_details_004(self):#to check with existing machine id
        self.driver.get("https://productionb.univa.cloud/admin/devices/machinedetails/add/")
        time.sleep(3)
        machine_id=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_machine_id"]')))
        machine_id.send_keys("machineid-1")
        save_button=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[1]/input')))
        save_button.click()
        error=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="machinedetails_form"]/div[2]/div[1]/div/div/div[2]/div/div/div[2]/ul/li')))
        Expected_msg="Machine details with this Machine id already exists." 
        Actual_msg=error.text
        self.assertEqual(Expected_msg,Actual_msg,f"Expected message is {Expected_msg} but got {Actual_msg}")
        print("test_TS_03_Machine_details_004...Passed")

    def test_TS_03_Machine_details_005(self):#to check weather the functions of save and add another
        self.driver.get("https://productionb.univa.cloud/admin/devices/machinedetails/add/")
        time.sleep(3)
        machine_name=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_machine_name"]')))
        machine_id=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_machine_id"]')))
        line=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_line"]')))
        manufacture=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_manufacture"]')))
        year=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_year"]')))
        device=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="select2-id_device-container"]')))
        machine_name.send_keys("Machine2")
        machine_id.send_keys("machineid-2")
        line.send_keys("one")
        manufacture.send_keys("manufact")
        year.send_keys("2024")
        device.click()
        options=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="select2-id_device-results"]')))
        option=options.find_elements(By.TAG_NAME,"li")

        for opt in option:
            opt_text=opt.text
            
            if opt_text=="Device1":
                print(opt_text)
                path=opt.get_attribute('id')
                print(path)
                opt.click()
                break
            time.sleep(3)
        res=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="select2-id_device-container"]'))).text
        print(res)  
        time.sleep(5)      
        production=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="id_production_per_hour"]')))
        production.send_keys("10")
        save_and_addanother=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[2]/input')))
        save_and_addanother.click()
        Expected_url="https://productionb.univa.cloud/admin/devices/machinedetails/add/"
        Actual_url=self.driver.current_url
        self.assertEqual(Expected_url,Actual_url,f"Expected page url is not matching to the actual page url")
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[3]/a'))).click()
        
        machine_at_table=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th')))
        machine_line=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/td[2]')))
        machine_manuf=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/td[3]')))
        machine_year=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/td[4]')))
        machine_device=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/td[5]')))
        self.assertEqual(machine_at_table.text,"machineid-2",f"Expected machine ID is not displayed at the table")
        self.assertEqual(machine_line.text,"one",f"Expected machine line is not displayed at the table")
        self.assertEqual(machine_manuf.text,"manufact",f"Expected machine manufacture is not displayed at the table")
        self.assertEqual(machine_year.text,"2024",f"Expected machine year is not displayed at the table")
        self.assertEqual(machine_device.text,"Device1",f"Expected machine device is not displayed at the table")
        print("TS_03_Machine_details_005...Passed")

    def test_TS_03_Machine_details_006(self):#to check the save and editing function
        self.driver.get("https://productionb.univa.cloud/admin/devices/machinedetails/")
        time.sleep(3)
        WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th/a'))
            ).click()
        time.sleep(3)
        save_and_edit=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.NAME,'_continue')))
        save_and_edit.click()
        time.sleep(3)
        Actual_page= WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[4]')))
        print(Actual_page.text)       
        Expected_page="machineid-2"
        self.assertEqual(Expected_page,Actual_page.text,f"Expected page is {Expected_page} but got {Actual_page.text}")
        machine_id=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_machine_id"]')))
        machine_id.clear()
        machine_id.send_keys("machineid-2.0")
        production=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="id_production_per_hour"]')))
        production.send_keys("150")
        save_button=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[1]/input')))
        save_button.click()
        machine_at_table=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th/a')))
        print(machine_at_table.text)
        self.assertEqual(machine_at_table.text,"machineid-2.0",f"Expected machine is machineid-2.0  but got {machine_at_table.text}")
        print("TS_03_Machine_details_006...Passed")

    def test_TS_03_Machine_details_007(self):#to check the functions of history and the delete buttons
        self.driver.get("https://productionb.univa.cloud/admin/devices/machinedetails/")
        time.sleep(3)
        add_machine=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div[2]/a')))
        add_machine.click()
        machine_name=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_machine_name"]')))
        machine_id=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_machine_id"]')))
        line=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_line"]')))
        manufacture=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_manufacture"]')))
        year=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="id_year"]')))
        device=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="select2-id_device-container"]')))
        machine_name.send_keys("Dummy_Machine1")
        machine_id.send_keys("dummyid-1")
        line.send_keys("one")
        manufacture.send_keys("manufact")
        year.send_keys("2024")
        device.click()
        options=WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="select2-id_device-results"]')))
        option=options.find_elements(By.TAG_NAME,"li")

        for opt in option:
            opt_text=opt.text
            
            if opt_text=="Device11":
                print(opt_text)
                path=opt.get_attribute('id')
                print(path)
                opt.click()
                break
            time.sleep(3)
        res=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="select2-id_device-container"]'))).text
        print(res)  
        time.sleep(5)      
        production=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="id_production_per_hour"]')))
        production.send_keys("10")
        save_button=WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[1]/input')))
        save_button.click()
        device_at_table=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th/a'))
        )
        device_at_table.click()
        delete_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div[1]/div[2]/a'))
        )
        self.assertEqual("Delete",delete_button.text,f"Expected is Delete button but got {delete_button.text}")
        history_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div[2]/a'))
        )
        self.assertEqual("History",history_button.text,f"Expected is History button but got {history_button.text}")
        history_button.click()
        page=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[5]'))
        )
        self.assertEqual("History",page.text,f"Expected history page is not displayed")
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[4]/a'))
        ).click()
        time.sleep(3)
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div[1]/div[2]/a'))
        ).click()

        # delete_button.click()
        page2=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[5]'))
        )
        self.assertEqual("Delete",page2.text,f"Expected Delete page is not displayed")
        WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="content-main"]/div/div[2]/form/div[1]/input'))
        ).click()
        res=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th/a'))
        ).text
        self.assertNotEqual(res,"dummyid-1")
        print("TS_03_Machine_details_007...Passed")
        
    def test_TS_03_Machine_details_008(self):
        self.driver.get("https://productionb.univa.cloud/admin/devices/machinedetails/")
        time.sleep(3)
        searchbox=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="searchbar"]'))
        )
        searchbox.send_keys("machineid-1")
        search_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="search_group"]/button'))
        )
        search_button.click()
        time.sleep(3)
        search_results=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th'))
        )
        Actual_result=search_results.text
        Expected_result="machineid-1"
        self.assertEqual(Expected_result,Actual_result,f"Expected result is {Expected_result} but got {Actual_result}")
        print("TS_03_Machine_details_008...Passed")

    def test_TS_05_Shift_001(self):#to check the adding shift,editing shift
        self.driver.get("https://productionb.univa.cloud/admin/devices/shifttimings/")
        time.sleep(3)
        add_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div[2]/a'))
        )
        add_button.click()
        page=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div/div/ol/li[4]'))
        )
        Actual_page=page.text
        Expected_page="Add shift timings"
        self.assertEqual(Expected_page,Actual_page,f"Expected page is {Expected_page} but got {Actual_page} ")
        start_time=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="id_start_time"]'))
        )
        end_time=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="id_end_time"]'))
        )
        shift_name=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="id_shift_name"]'))
        )
        save_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div/div[1]/input'))
        )
        start_time.send_keys("00:00:00")
        end_time.send_keys("2:00:00")
        shift_name.send_keys("Nyt_Shift")
        save_button.click()
        shift_at_table=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th/a'))
        )
        Actual_result=shift_at_table.text
        Expected_result="Nyt_Shift"
        self.assertEqual(Expected_result,Actual_result,f"Expected result is {Expected_result} but got {Actual_result}")
        print("Shift has been sucessfully added...")
        #to edit the shift
        shift_at_table.click()
        save_edit=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div[1]/div[4]/input'))
        )
        save_edit.click()
        start_time.clear()
        start_time.send_keys("01:00:00")
        end_time.clear()
        end_time.send_keys("02:00:00")
        shift_name.clear()
        shift_name.send_keys("EARLY_MORNING")
        save_button.click()
        new_name=shift_at_table.text
        new_time=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/td[2]'))
        ).text
        new_end_time=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/td[2]'))
        ).text
        self.assertEqual("EARLY_MORNING",new_name,f"Expected name is EARLY_MORNING but got {new_name}")
        self.assertEqual("01:00:00",new_time,f"Expected name is 01:00:00 but got {new_time}")
        self.assertEqual("02:00:00",new_end_time,f"Expected name is 02:00:00 but got {new_end_time}")
        #to delete shift
        shift_at_table.click()
        Delete_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="jazzy-actions"]/div[1]/div[2]/a'))
        )
        Delete_button.click()
        delete_page=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'/html/body/div/div[1]/div[1]/div/div/div/ol/li[5]'))
        )
        self.assertEqual("Delete",delete_page.text,f"Expected page is Delete but got {delete_page.text}")
        im_sure=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="content-main"]/div/div[2]/form/div[1]/input'))
        )
        im_sure.click()
        self.assertNotEqual(shift_at_table.text,"EARLY_MORNING")
        print("test_TS_05_Shift_001...Passed")

    def test_TS_05_Shift_001(self):
        
        self.driver.get("https://productionb.univa.cloud/admin/devices/shifttimings/")
        
        # Wait and click the Add button
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div[2]/a'))
        )
        add_button.click()
        
        # Verify navigation to Add Shift Timings page
        page = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/ol/li[4]'))
        )
        actual_page = page.text
        expected_page = "Add shift timings"
        self.assertEqual(expected_page, actual_page, f"Expected page is {expected_page} but got {actual_page}")
        
        # Fill in the form and save
        start_time = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_start_time"]'))
        )
        end_time = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_end_time"]'))
        )
        shift_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_shift_name"]'))
        )
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jazzy-actions"]/div/div[1]/input'))
        )
        start_time.send_keys("00:00:00")
        end_time.send_keys("02:00:00")
        shift_name.send_keys("Nyt_Shift")
        save_button.click()
        
        # Verify shift has been added
        shift_at_table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result_list"]/tbody/tr[1]/th/a'))
        )
        actual_result = shift_at_table.text
        expected_result = "Nyt_Shift"
        self.assertEqual(expected_result, actual_result, f"Expected result is {expected_result} but got {actual_result}")
        print("Shift has been successfully added...")

        # Edit the shift
        shift_at_table.click()
        save_edit = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jazzy-actions"]/div[1]/div[4]/input'))
        )
        save_edit.click()
        self.driver.get("https://productionb.univa.cloud/admin/devices/shifttimings/")
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result_list"]/tbody/tr[1]/th/a'))
        ).click()
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_start_time"]'))
        ).clear()
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_start_time"]'))
        ).send_keys("01:00:00")
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_end_time"]'))
        ).clear()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_end_time"]'))
        ).send_keys("02:00:00")
        shift_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_shift_name"]'))
        )
        save_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jazzy-actions"]/div/div[1]/input'))
        )
        shift_name.clear()
        shift_name.send_keys("EARLY_MORNING")
        save_button.click()
        
        # Verify the shift has been edited
        updated_shift = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result_list"]/tbody/tr[1]/th/a'))
        )
        updated_name = updated_shift.text
        updated_time = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result_list"]/tbody/tr[1]/td[2]'))
        ).text
        updated_end_time = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result_list"]/tbody/tr[1]/td[3]'))
        ).text
        
        self.assertEqual("EARLY_MORNING", updated_name, f"Expected name is EARLY_MORNING but got {updated_name}")
        self.assertEqual("1 a.m.", updated_time, f"Expected start time is 1 a.m. but got {updated_time}")
        self.assertEqual("2 a.m.", updated_end_time, f"Expected end time is 2 a.m. but got {updated_end_time}")
        print("Shift has been successfully edited...")
        # Delete the shift
        updated_shift.click()
        delete_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jazzy-actions"]/div[1]/div[2]/a'))
        )
        delete_button.click()
        delete_page = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div/ol/li[5]'))
        )
        self.assertEqual("Delete", delete_page.text, f"Expected page is Delete but got {delete_page.text}")
        im_sure = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="content-main"]/div/div[2]/form/div[1]/input'))
        )
        im_sure.click()
        print("shift has been successfully deleted...")
        
        print("test_TS_05_Shift_001...Passed")  

    def test_TS_05_Shift_002(self):#to check errors in the shift adding page
        self.driver.get("https://productionb.univa.cloud/admin/devices/shifttimings/")
        time.sleep(3)
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div[2]/a'))
        )
        add_button.click()
        save_button=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jazzy-actions"]/div/div[1]/input'))
        )
        save_button.click()
        error1=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="shifttimings_form"]/div/div[1]/div/div/div[1]/div/div/div[2]'))
        )
        error2=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="shifttimings_form"]/div/div[1]/div/div/div[2]/div/div/div[2]'))
        )
        error3=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="shifttimings_form"]/div/div[1]/div/div/div[3]/div/div/div[2]'))
        )
        result=False
        if  error1.text=="This field is required." and error2.text=="This field is required." and error3.text=="This field is required.":
            result=True
        self.assertEqual("True",str(result),f"Expected error message is not appeared")
        print("TS_05_Shift_002...Passed")

    def test_TS_05_Shift_003(self):
        self.driver.get("https://productionb.univa.cloud/admin/devices/shifttimings/")
        time.sleep(3)
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/div[2]/a'))
        )
        add_button.click()
        page=WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/ol/li[4]'))
        )
        self.assertEqual("Add shift timings",page.text,f"Expected result is Add shift timings but got {page.text}")
        start_time = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_start_time"]'))
        )
        end_time = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_end_time"]'))
        )
        shift_name = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_shift_name"]'))
        )
        start_time.send_keys("10:15:00")
        end_time.send_keys("13:30:00")
        shift_name.send_keys("Mornin_shift")
        save_another=WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="jazzy-actions"]/div/div[2]/input'))
        )
        save_another.click()
        Actual_url=self.driver.current_url
        Expected_url="https://productionb.univa.cloud/admin/devices/shifttimings/add/"
        self.assertEqual(Expected_url,Actual_url,f"Expected is {Expected_url} but got {Actual_url}")
        self.driver.get("https://productionb.univa.cloud/admin/devices/shifttimings/")
        shift_at_table = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result_list"]/tbody/tr[1]/th/a'))
        )
        Expected_result="Mornin_shift"
        Actual_result=shift_at_table.text
        self.assertEqual(Expected_result,Actual_result,f"Expected is {Expected_result} but got {Actual_result}")
        print("TS_05_Shift_003...Passed")
        

    def test_TS_05_Shift_004(self):# to check the search result
        self.driver.get("https://productionb.univa.cloud/admin/devices/shifttimings/")
        time.sleep(3)
        searchbox=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="searchbar"]'))
        )
        searchbox.send_keys("Mornin_shift")
        search_button=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="search_group"]/button'))
        )
        search_button.click()
        time.sleep(3)
        search_results=WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="result_list"]/tbody/tr[1]/th'))
        )
        Actual_result=search_results.text
        Expected_result="Mornin_shift"
        print("Currently its low priority..")
        self.assertEqual(Expected_result,Actual_result,f"Expected result is {Expected_result} but got {Actual_result}")
        
        print("TS_05_Shift_04...Passed")


        
        
        


          


        
        
            

        

        
        

        
        

if __name__ == "__main__":
    unittest.main(verbosity=2)



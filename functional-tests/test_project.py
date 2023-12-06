# Selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# Django
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

class TestProjectGiftStore(StaticLiveServerTestCase):
    
    """Dummy Test"""
    # def test_foo(self):
    #     self.assertEquals(0, 1)

    def setUp(self):
        service = Service(executable_path='./functional-tests/chromedriver.exe')
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        self.driver = driver

    def test_main_page_is_displayed(self):
        self.driver.get(self.live_server_url)
        print(self.live_server_url)

    def test_button_create_account_redirects_to_signin_page(self):
        self.driver.get(self.live_server_url)
        create_account_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'CREAR CUENTA!')))
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        self.assertEqual('Crea tu cuenta', self.driver.title)

    def test_button_sign_in_redirects_to_signing_page(self):
        self.driver.get(self.live_server_url)
        sign_in_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "TENGO CUENTA!")))
        self.assertTrue(sign_in_button.is_displayed() and sign_in_button.is_enabled())
        sign_in_button.click()
        self.assertEqual('Ingresar', self.driver.title)
        
    def test_create_new_account_and_login(self):
        self.driver.get(self.live_server_url)
        create_account_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'CREAR CUENTA!')))
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Crea tu cuenta', self.driver.title)

        email = self.driver.find_element(By.NAME, 'email')
        first_name = self.driver.find_element(By.NAME, 'first_name')
        last_name = self.driver.find_element(By.NAME, 'last_name')
        username = self.driver.find_element(By.NAME, 'username')
        age = self.driver.find_element(By.NAME, 'age')
        phone = self.driver.find_element(By.NAME, 'phone')
        password = self.driver.find_element(By.NAME, 'password')
        password_confirmation = self.driver.find_element(By.NAME, 'password_confirmation')
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        self.assertTrue(email.is_enabled()
        and first_name.is_enabled()
        and last_name.is_enabled()
        and username.is_enabled()
        and age.is_enabled()
        and phone.is_enabled()
        and password.is_enabled()
        and password_confirmation.is_enabled())

        email.send_keys("test@test.com")
        first_name.send_keys("Test")
        last_name.send_keys("Test")
        username.send_keys("tester")
        age.send_keys(19)
        phone.send_keys(5511223344)
        password.send_keys("test1234")
        password_confirmation.send_keys("test1234")
        submit_button.click()

        self.assertEqual("Ingresar", self.driver.title)

        email = self.driver.find_element(By.NAME, "email")
        password = self.driver.find_element(By.NAME, 'password')
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        self.assertTrue(email.is_enabled() and password.is_enabled())

        email.send_keys("test@test.com")
        password.send_keys("test1234")
        submit_button.click()

        self.assertEqual("Regalos.mx", self.driver.title)

    def tearDown(self):
            self.driver.close()

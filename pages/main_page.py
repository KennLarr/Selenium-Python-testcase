from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://automationexercise.com/"

    # ✅ FIXED: Add missing open() method
    def open(self):
        self.driver.get(self.url)

    # --- Locators ---
    signup_login_btn = (By.XPATH, "//a[contains(text(),'Signup / Login')]")
    
    # Signup locators
    signup_first_name = (By.NAME, "first_name")
    signup_last_name = (By.NAME, "last_name")
    signup_company_name = (By.NAME, "company")
    signup_address = (By.NAME, "address1")
    signup_address2 = (By.NAME, "address2") 
    signup_country = (By.NAME, "country")
    signup_state = (By.NAME, "state")
    signup_city = (By.NAME, "city") 
    signup_zipcode = (By.NAME, "zipcode")
    signup_mobile_number = (By.NAME, "mobile_number")

    signup_name = (By.NAME, "name")
    
    signup_email = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = (By.XPATH, "//button[@data-qa='signup-button']")
    signup_password = (By.ID, "password")
    create_account_button = (By.XPATH, "//button[@data-qa='create-account']")
    account_created_text = (By.XPATH, "//h2[@data-qa='account-created']")
    
    # Login locators
    login_email = (By.XPATH, "//input[@data-qa='login-email']")
    login_password = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")
    logout_button = (By.XPATH, "//a[contains(text(),'Logout')]")

    # Contact Us
    contact_us_button = (By.XPATH,"//a[normalize-space()='Contact us']")
    get_in_touch = (By.XPATH, "//h2[normalize-space()='Get In Touch']")
    contact_us_name = (By.NAME, "name")
    contact_us_email = (By.NAME, "email")
    subject = (By.NAME,"subject")
    message = (By.NAME,"message")

    # --- Methods ---
    def contact_us_trans(self, name, email, subject, message):
        self.open()  # ✅ always open page first
        self.driver.find_element(*self.contact_us_button).click()
        element = self.driver.find_element(*self.get_in_touch)
        assert element.is_displayed(), "❌ 'GET IN TOUCH' section is not visible."
        print("✅ 'GET IN TOUCH' section is visible successfully.")

        self.driver.find_element(*self.contact_us_name).send_keys(name)
        self.driver.find_element(*self.contact_us_email).send_keys(email)
        self.driver.find_element(*self.subject).send_keys(subject)
        self.driver.find_element(*self.message).send_keys(message)

    def select_gender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(By.ID, "id_gender1").click()
        elif gender.lower() == "female":
            self.driver.find_element(By.ID, "id_gender2").click()

    # --- Signup Methods ---
    def open_signup_page(self):
        self.open()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.signup_login_btn)
        ).click()

    def select_by_value(self, element, value):
        Select(element).select_by_value(str(value))

    def start_signup(self, name, email):
        self.driver.find_element(*self.signup_name).send_keys(name)
        self.driver.find_element(*self.signup_email).send_keys(email)
        self.driver.find_element(*self.signup_button).click()

    def fill_signup_form(self, password):
        self.driver.find_element(*self.signup_password).send_keys(password)
        self.driver.find_element(*self.create_account_button).click()

    def select_date_of_birth(self, day, month, year):
        self.select_by_value(self.driver.find_element(By.ID, "days"), str(day))
        self.select_by_value(self.driver.find_element(By.ID, "months"), month)
        self.select_by_value(self.driver.find_element(By.ID, "years"), str(year))

    def is_account_created(self):
        try:
            text = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.account_created_text)
            ).text
            return "ACCOUNT CREATED!" in text.upper()
        except:
            return False

    # --- Login Methods ---
    def open_login_page(self):
        self.open()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.signup_login_btn)
        ).click()

    def login(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.login_email)
        ).send_keys(email)
    
        self.driver.find_element(*self.login_password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def is_logged_in(self):
        try:
            return self.driver.find_element(*self.logout_button).is_displayed()
        except:
            return False

    # --- Newsletter Subscription ---
    def newsletter_subscription(self, subscribe: bool):
        newsletter_checkbox = self.driver.find_element(By.ID, "newsletter")
        optin_checkbox = self.driver.find_element(By.ID, "optin")

        for checkbox in [newsletter_checkbox, optin_checkbox]:
            if subscribe and not checkbox.is_selected():
                checkbox.click()
            elif not subscribe and checkbox.is_selected():
                checkbox.click()

    def information_required(self, first_name, last_name, company_name, address, address2, country, state, city, zipcode, mobile_number):
        self.driver.find_element(*self.signup_first_name).send_keys(first_name)
        self.driver.find_element(*self.signup_last_name).send_keys(last_name)
        self.driver.find_element(*self.signup_company_name).send_keys(company_name)
        self.driver.find_element(*self.signup_address).send_keys(address)
        self.driver.find_element(*self.signup_address2).send_keys(address2)
        self.select_by_value(self.driver.find_element(*self.signup_country), country)
        self.driver.find_element(*self.signup_state).send_keys(state)
        self.driver.find_element(*self.signup_city).send_keys(city)
        self.driver.find_element(*self.signup_zipcode).send_keys(zipcode)
        self.driver.find_element(*self.signup_mobile_number).send_keys(mobile_number)
        self.driver.find_element(*self.create_account_button).click()

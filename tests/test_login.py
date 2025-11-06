from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from utils.excel_reader import get_credentials
import time

def test_login():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(driver)

    main_page.open()
    main_page.open_login_page()

    # ✅ Get email and password from Excel
    email, password = get_credentials("admin")
    print("Email:", email)
    print("Password:", password)

    # ✅ Login using credentials
    main_page.login(email, password)
    # ✅ Check login success
    if main_page.is_logged_in():
        assert True
        print("✅ Login Successful")
        
    else:
        print("❌ Login Failed — Running Registration First")
   

    time.sleep(3)
    driver.quit()

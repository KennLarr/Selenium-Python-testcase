from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from utils.excel_reader import get_register_data
import pytest
import time

def test_register():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()   # ✅ Make browser fullscreen
    main_page = MainPage(driver)

    user = get_register_data("admin")  # dict returned from Excel

    main_page.open_signup_page()
    main_page.start_signup(user["name"], user["email"])
    time.sleep(3)
    main_page.select_gender(user["gender"])
    time.sleep(3)
    main_page.fill_signup_form(user["password"])
    time.sleep(3)
    main_page.select_date_of_birth(user["day"], user["month"], user["year"])
    time.sleep(3)
    main_page.newsletter_subscription(True)

    main_page.information_required(
        "Roseann", "Smith", "TechCorp", "123 Main St", "Apt 4B",
        "Canada", "Ontario", "Toronto", "M4B1B3", "1234567890"
    )

    time.sleep(3)  # optional pause to see result

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
import pytest
import time


def test_contactus():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    main_page = MainPage(driver)

    main_page.contact_us_trans("John Doe","john@example.com","Test Subject","Hello!")


    time.sleep(3)

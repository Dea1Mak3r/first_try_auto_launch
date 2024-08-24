import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions


@pytest.fixture()
def browser():
    options = ChromeOptions()
    options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    return browser


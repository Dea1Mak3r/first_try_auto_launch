import pytest
from selenium.webdriver.common.by import By



def test_button_exists(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    browser.implicitly_wait(10)
    assert browser.find_element(By.CLASS_NAME, "btn-primary").is_displayed()


def test_button_click(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    assert browser.find_element(By.ID, "result-text").text == "Submitted"
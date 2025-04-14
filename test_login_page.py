from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

def test_login_page():
    driver = webdriver.Chrome()
    driver.get("https://practicetestautomation.com/practice-test-login/")

    driver.find_element(By.XPATH, ("//input[@id='username']")).send_keys("student")
    driver.find_element(By.XPATH, ("//input[@id='password']")).send_keys("Password123")
    driver.find_element(By.XPATH, ("//button[@id='submit']")).click()
    driver.quit()
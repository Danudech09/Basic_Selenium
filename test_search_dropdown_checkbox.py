from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as conditions

def test_search_dropdown_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://www.nike.com/th/")
    wait = WebDriverWait(driver, 50)
    driver.maximize_window()
    driver.find_element(By.XPATH, ("//button[@id='nav-search-icon']")).click()
    driver.find_element(By.XPATH, ("//input[@id='gn-search-input']")).send_keys("air force 1")
    ActionChains(driver)\
        .key_down(Keys.ENTER)\
        .perform()
    driver.find_element(By.XPATH, ("//div[contains(@class,'css-lrxey8')]")).click()
    driver.find_element(By.XPATH, ("//button[contains(text(),'ใหม่ล่าสุด')]")).click()
    wait.until(conditions.element_to_be_clickable((By.XPATH, '//img[contains(@alt, "Nike Air Force 1 \'07 Next Nature รองเท้าผู้หญิง")]'))).click()
    wait.until(conditions.element_to_be_clickable((By.ID, "colorway-chip-DV3808-110"))).click()
    wait.until(conditions.element_to_be_clickable((By.XPATH, "//label[normalize-space()='US 6']"))).click()

    driver.quit()
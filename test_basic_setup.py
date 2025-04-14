from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest

#Test without UI
def test_basic():
    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.selenium.dev/")

    driver.current_url
    title = driver.title

    assert "Selenium" in title
    
    driver.find_element(By.CLASS_NAME, "navbar-brand")
    driver.find_element(By.CSS_SELECTOR, "#navbarDropdown")
    driver.find_element(By.ID, "Layer_1")
    driver.find_element(By.LINK_TEXT, "Join us!")
    driver.find_element(By.XPATH ,"//a[@id='navbarDropdown']")



    #Open new tab
    #driver.execute_script("window.open('URL')")
    #Switch tab
    #driver.switch_to.window(driver.window_handles[1]) 
    driver.quit()
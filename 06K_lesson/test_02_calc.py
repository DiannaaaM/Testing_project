from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_slow_calculator():
    driver = webdriver.Chrome()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_field = driver.find_element(By.ID, "delay")
    delay_field.clear()
    delay_field.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    time.sleep(45)
    result_element = driver.find_element(By.CLASS_NAME, "screen")
    assert result_element.text == '15'

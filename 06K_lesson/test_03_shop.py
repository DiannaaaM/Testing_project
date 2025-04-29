from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By



def test_online_shop():
    driver = webdriver.Chrome()

    driver.get('https://www.saucedemo.com/')
    driver.find_element('id', 'user-name').send_keys('standard_user')
    driver.find_element('id', 'password').send_keys('secret_sauce')
    driver.find_element('name', 'login-button').click()
    sleep(2)
    driver.find_element('id', 'add-to-cart-sauce-labs-backpack').click()
    driver.find_element('id', 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element('id', 'add-to-cart-sauce-labs-onesie').click()
    driver.find_element('id', 'shopping_cart_container').click()
    sleep(2)
    driver.find_element(By.XPATH, "//button[text()='Checkout']").click()
    sleep(2)
    driver.find_element('id', 'first-name').send_keys('Diana')
    driver.find_element('id', 'last-name').send_keys('Murlaeva')
    driver.find_element('id', 'postal-code').send_keys('427018')
    driver.find_element('id', 'continue').click()
    sleep(5)
    result = driver.find_element('class name', 'summary_total_label').text
    assert result == 'Total: $58.29'

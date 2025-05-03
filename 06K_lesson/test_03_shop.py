from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_online_shop():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get('https://www.saucedemo.com/')

    wait.until(EC.presence_of_element_located((By.ID, 'user-name'))).send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.NAME, 'login-button').click()

    wait.until(EC.element_to_be_clickable((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()

    driver.find_element(By.ID, 'shopping_cart_container').click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))).click()

    wait.until(EC.presence_of_element_located((By.ID, 'first-name'))).send_keys('Diana')
    driver.find_element(By.ID, 'last-name').send_keys('Murlaeva')
    driver.find_element(By.ID, 'postal-code').send_keys('427018')
    driver.find_element(By.ID, 'continue').click()

    total_text = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'summary_total_label'))).text
    assert total_text == 'Total: $58.29', f"Unexpected total: {total_text}"

    driver.quit()

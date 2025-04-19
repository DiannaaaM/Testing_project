from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    input_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "t1"))
    )
    input_field.clear()
    input_field.send_keys("SkyPro")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    button_text = button.text
    print(f'"{button_text}"')
finally:
    driver.quit()

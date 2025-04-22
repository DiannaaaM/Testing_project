from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    button.click()

    content_div = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "content"))
    )

    WebDriverWait(driver, 20).until(
        lambda d: "Data loaded with AJAX get request." in content_div.text
    )

    print("Data loaded with AJAX get request.")

except Exception as e:
    print("Ошибка:", e)

finally:
    driver.quit()

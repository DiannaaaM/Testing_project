from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")
    
    # Ждем загрузки страницы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary"))
    )
    button.click()

    content_div = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "content"))
    )

    # Явная проверка текста
    expected_text = "Data loaded with AJAX get request."
    WebDriverWait(driver, 20).until(
        lambda d: expected_text in content_div.text
    )
    
    assert expected_text in content_div.text, f"Ожидался текст '{expected_text}', получен '{content_div.text}'"
    print("Тест успешно пройден: данные загружены через AJAX")

except Exception as e:
    print("Ошибка:", e)
    driver.save_screenshot("error_screenshot.png")
    raise

finally:
    driver.quit()
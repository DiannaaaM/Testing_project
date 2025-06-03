from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")
    
    # Ждем загрузки страницы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )

    input_field.clear()
    input_field.send_keys("SkyPro")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    button.click()

    # Явная проверка текста кнопки
    expected_text = "SkyPro"
    WebDriverWait(driver, 5).until(lambda d: button.text == expected_text)
    assert button.text == expected_text, f"Ожидался текст '{expected_text}', получен '{button.text}'"
    
    print(f"Тест успешно пройден: кнопка изменила текст на '{button.text}'")

except Exception as e:
    print("Произошла ошибка:", e)
    driver.save_screenshot("error_screenshot.png")
    raise

finally:
    driver.quit()

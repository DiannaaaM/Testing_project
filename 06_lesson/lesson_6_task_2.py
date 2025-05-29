from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    try:
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "newButtonName"))
        )
    except Exception as e:
        print("Не удалось найти поле ввода:", e)
        driver.save_screenshot("error_screenshot.png")
        raise

    input_field.clear()
    input_field.send_keys("SkyPro")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    button.click()

    WebDriverWait(driver, 5).until(lambda d: button.text == "SkyPro")

    print(f"Кнопка изменила текст на: {button.text}")

except Exception as e:
    print("Произошла ошибка:", e)

finally:
    driver.quit()

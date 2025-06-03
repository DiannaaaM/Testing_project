from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    # Ждем загрузки страницы
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    images = WebDriverWait(driver, 40).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    third_image = images[2]

    # Ждем загрузки изображения и проверяем его атрибуты
    WebDriverWait(driver, 40).until(
        lambda d: third_image.get_attribute("src") and 
                 third_image.get_attribute("src") != "" and
                 third_image.get_attribute("naturalWidth") != "0"
    )

    src_value = third_image.get_attribute("src")
    assert src_value, "URL изображения не найден"
    
    print(f"Тест успешно пройден: URL третьего изображения - {src_value}")

except Exception as e:
    print("Произошла ошибка:", e)
    driver.save_screenshot("error_screenshot.png")
    raise

finally:
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    images = WebDriverWait(driver, 40).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    third_image = images[2]

    WebDriverWait(driver, 40).until(
        lambda d: third_image.get_attribute("src") and third_image.get_attribute("src") != ""
    )

    src_value = third_image.get_attribute("src")

    print(src_value)

except Exception as e:
    print("Произошла ошибка:", e)
finally:
    driver.quit()

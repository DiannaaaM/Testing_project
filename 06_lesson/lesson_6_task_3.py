from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    images = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    if len(images) >= 3:
        src_value = images[2].get_attribute("src")
        print(src_value)
    else:
        print("Меньше 3 изображений на странице.")
finally:
    driver.quit()

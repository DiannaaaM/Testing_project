from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Создание драйвера с помощью webdriver_manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

sleep(2)  # Небольшая пауза, чтобы страница подгрузилась

driver.get("http://uitestingplayground.com/dynamicid")
sleep(2)

# Fix: Use correct selector (CSS selector instead of class name)
add_element_button = driver.find_element(By.TAG_NAME, '.button')

delete_buttons = driver.find_elements(By.CSS_SELECTOR, '.added-manually')
print(delete_buttons)

# Конец скрипта по умолчанию, чтобы посмотреть результат
sleep(10)

# Закрытие браузера по окончании работы
driver.quit()
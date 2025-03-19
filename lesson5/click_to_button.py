from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Создание драйвера с помощью webdriver_manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

sleep(2)  # Небольшая пауза, чтобы страница подгрузилась

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(2)

add_element_button = driver.find_element(By.CSS_SELECTOR, 'div > button')
lst_element = []
for _ in range(5):
    add_element_button.click()
    sleep(1)
    lst_element.append(driver.find_element(By.CSS_SELECTOR, '.added-manually').text)
[print(i) for i in lst_element]

# Конец скрипта по умолчанию, чтобы посмотреть результат
sleep(10)

# Закрытие браузера по окончании работы
driver.quit()
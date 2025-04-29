from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
field = driver.find_element('name', 'first-name')
field.send_keys("Иван")
sleep(2)
field = driver.find_element('name', 'last-name')
field.send_keys("Петров")
sleep(2)
field = driver.find_element('name', 'address')
field.send_keys("Ленина, 55-3")
sleep(2)
field = driver.find_element('name', 'e-mail')
field.send_keys("test@skypro.com")
sleep(2)
field = driver.find_element('name', 'phone')
field.send_keys("+7985899998787")
sleep(2)
field = driver.find_element('name', 'city')
field.send_keys("Москва")
sleep(2)
field = driver.find_element('name', 'country')
field.send_keys("Россия")
sleep(2)
field = driver.find_element('name', 'job-position')
field.send_keys("QA")
sleep(2)
field = driver.find_element('name', 'company')
field.send_keys("SkyPro")
sleep(2)
driver.find_element(By.TAG_NAME, 'button').click()

'''alert py-2 alert-danger

alert py-2 alert-success'''

def test_zip_field():
    # Проверка подсветки поля Zip code
    pole_z = driver.find_element(By.ID, "zip-code").get_attribute("class")
    assert pole_z == "alert py-2 alert-danger"

def test_full_fields():
    # Проверка подсветки остальных полей
    poles = ["#first-name", "#last-name", "#address", "#city", "#country", "#e-mail", "#phone", "#company"]
    for pole in poles:
        pole_class = driver.find_element(By.CSS_SELECTOR, pole).get_attribute("class")
        assert pole_class == "alert py-2 alert-success"

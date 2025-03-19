from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# Создание драйвера с помощью webdriver_manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Переход на сайт "Яндекс"
driver.get("https://ya.ru/")
sleep(2)  # Небольшая пауза, чтобы страница подгрузилась

# Переход на сайт "ВКонтакте"
driver.get("https://vk.com/")
sleep(2)  # Небольшая пауза, чтобы страница подгрузилась

# Установка размера окна браузера
driver.set_window_size(600, 800)

# Навигация назад и вперед несколько раз
for x in range(1, 10):
    driver.back()
    sleep(1)  # Пауза, чтобы не перегружать браузер
    driver.forward()
    sleep(1)  # Пауза, чтобы не перегружать браузер

# Обновление страницы
driver.refresh()
sleep(2)  # Небольшая пауза после обновления

# Конец скрипта по умолчанию, чтобы посмотреть результат
sleep(50)

# Закрытие браузера по окончании работы
driver.quit()


driver.maximize_window #открыть окно по размеру экрана
driver.minimize_window #свернуть окно браузера
driver.fullscreen_window #развернуть окно на весь экран, аналог F11

driver.get("https://ya.ru/")
driver.get("https://vk.com/")
driver.set_window_size(640, 460)

sleep(10)

driver.save_screenshot("./ya.png")
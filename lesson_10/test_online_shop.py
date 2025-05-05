from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import allure


class PageObject:
    @allure.step('Открытие ссылки')
    def open_site(self, driver, link):
        driver.get(link)

    @allure.step('Заполнение поля для логина')
    def add_login(self, driver):
        return self.search_element(driver, 'id', 'user-name')

    @allure.step('Заполнение поля для пароля')
    def add_password(self, driver):
        return self.search_element(driver, 'id', 'password')

    @allure.step('Нажатие на заданную кнопку')
    def click_to_button(self, btn):
        btn.click()

    @allure.step('Путь до элемента - 8')
    def eight_num(self, driver):
        return self.search_element(driver, By.XPATH, "//span[text()='8']")

    @allure.step('Добавление товара в корзину')
    def add_to_buscket(self, driver, by, name):
        return self.search_element(driver, by, name).click()

    @allure.step('Поиск заданного элемента по определенным критериям')
    def search_element(self, driver, by, value):
        return driver.find_element(by, value)

    @allure.step('Заполнение необходимых полей')
    def send_keys(self, element, data):
        element.send_keys(str(data))

    @allure.step('Получение содержимого элемента')
    def text_data(self, element):
        return element.text

@allure.title('Test online-shop')
@allure.description('Тестирование работоспособности онлайн-магазина')
@allure.epic("Онлайн-магазин")
@allure.severity("Critical")
@allure.feature("READ")
@allure.id(2)
def test_calculator():
    driver = webdriver.Chrome()
    page = PageObject()

    page.open_site(driver, ' https://www.saucedemo.com/')

    sleep(1)

    page.send_keys(page.search_element(driver, 'id', 'user-name'), 'standard_user')
    page.send_keys(page.search_element(driver, 'id', 'password'), 'secret_sauce')
    page.click_to_button(page.search_element(driver, 'name', 'login-button'))

    sleep(2)

    page.add_to_buscket(driver, 'id', 'add-to-cart-sauce-labs-backpack')
    page.add_to_buscket(driver, 'id', 'add-to-cart-sauce-labs-bolt-t-shirt')
    page.add_to_buscket(driver, 'id', 'add-to-cart-sauce-labs-onesie')
    page.click_to_button(page.search_element(driver, 'id', 'shopping_cart_container'))

    sleep(2)

    page.click_to_button(page.search_element(driver, By.XPATH, "//button[text()='Checkout']"))

    sleep(1)

    page.send_keys(page.search_element(driver, 'id', 'first-name'), 'Diana')
    page.send_keys(page.search_element(driver, 'id', 'last-name'), 'Murlaeva')
    page.send_keys(page.search_element(driver, 'id', 'postal-code'), '427018')
    page.click_to_button(page.search_element(driver, 'id', 'continue'))

    sleep(2)

    result = page.text_data(page.search_element(driver, 'class name', 'summary_total_label'))
    assert result == 'Total: $58.29'
    driver.quit()


if __name__ == "__main__":
    test_calculator()

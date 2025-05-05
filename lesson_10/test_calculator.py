from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class PageObject:
    """
    Класс, созданный для работы с элементами сайта
    """

    def open_site(self, driver: webdriver, link: str) -> Any:
        """
        Метод для открытия переданной ссылки
        :return команда для открытия заданного сайта.
        Отобржение открытого сайта в браузере
        """
        return driver.get(link)

    def plus_symbol(self, driver: webdriver) -> Any:
        """
        Метод для поиска определенного элемента - цифры + на поле
        :return расположение элемента "+", готового для дальнейшей обработки
        """
        return self.search_element(driver, By.XPATH, "//span[text()='+']")

    def equals_symbol(self, driver: webdriver) -> Any:
        """
        Метод для поиска определенного элемента - цифры = на поле
        :return расположение элемента "=", готового для дальнейшей обработки
        """
        return self.search_element(driver, By.XPATH, "//span[text()='=']")

    def seven_num(self, driver: webdriver) -> Any:
        """
        Метод для поиска определенного элемента - цифры 7 на поле
        :return расположение элемента "7", готового для дальнейшей обработки
        """
        return self.search_element(driver, By.XPATH, "//span[text()='7']")

    def eight_num(self, driver: webdriver) -> Any:
        """
        Метод для поиска определенного элемента - цифры 8 на поле
        :return расположение элемента "8", готового для дальнейшей обработки
        """
        return self.search_element(driver, By.XPATH, "//span[text()='8']")

    def delay_num(self, driver: webdriver) -> Any:
        """
        Метод для поиска определенного элемента - поле ввода для задержки
        :return расположение элемента для ввода задержки ответа, готового для дальнейшей обработки
        """
        return self.search_element(driver, By.ID, "delay")

    def search_element(self, driver: webdriver, by: Any, value: str) -> Any:
        """
        Метод для поиска любого элемента
        :return расположение переданного элемента по переданным атрибутам, готового для дальнейшей обработки
        """
        return driver.find_element(by, value)

    def send_keys(self, element: webdriver, data: str) -> Any:
        """
        Метод для заполнения поля
        :return заполненое поле и его отображение в браузере
        """
        return element.send_keys(str(data))

    def click_to_element(self, element: webdriver) -> Any:
        """
        Метод для нажатия на кнопку
        :return отклик сайта после нажатия на кнопку
        """
        return element.click()

    def text_data(self, element: webdriver) -> str:
        """
         Метод для получения текста элемента
        :return текст, содержимый в элементе
        """
        return element.text



@allure.title('Test online-shop')
@allure.description('Тестирование работоспособности калькулятора')
@allure.epic("Калькулятор")
@allure.severity("Critical")
@allure.feature("COUNT")
@allure.id(1)
def test_calculator() -> None:
    with allure.step('Инициализация и настройка'):
        driver = webdriver.Chrome()
        page = PageObject()

    with allure.step('открытие сайта'):
        page.open_site(driver, 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "delay"))
        )

    with allure.step('Настройка поля задержки'):
        delay_element = page.search_element(driver, By.ID, "delay")
        delay_element.clear()
        page.send_keys(delay_element, 45)

    with allure.step('Клик по кнопкам калькулятора'):
        page.click_to_element(page.seven_num(driver))
        page.click_to_element(page.plus_symbol(driver))
        page.click_to_element(page.eight_num(driver))
        page.click_to_element(page.equals_symbol(driver))

    with allure.step('Ожидание результата'):
        result_element = WebDriverWait(driver, 45).until(
            EC.presence_of_element_located((By.CLASS_NAME, "screen"))
        )
        WebDriverWait(driver, 45).until(
            lambda d: result_element.text == '15'
        )
        result_text = page.text_data(result_element)

    with allure.step('Проверка результата'):
        assert result_text == '15'


if __name__ == "__main__":
    test_calculator()

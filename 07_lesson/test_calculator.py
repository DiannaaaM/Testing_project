from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_site(self, link):
        self.driver.get(link)

    def search_element(self, by, value):
        return self.driver.find_element(by, value)

    def send_keys(self, element, data):
        element.send_keys(str(data))

    def click_to_element(self, element):
        element.click()

    def text_data(self, element):
        return element.text


class CalculatorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'

    def open(self):
        self.open_site(self.url)

    def plus_symbol(self):
        return self.search_element(By.XPATH, "//span[text()='+']")

    def equals_symbol(self):
        return self.search_element(By.XPATH, "//span[text()='=']")

    def seven_num(self):
        return self.search_element(By.XPATH, "//span[text()='7']")

    def eight_num(self):
        return self.search_element(By.XPATH, "//span[text()='8']")

    def delay_input(self):
        return self.search_element(By.ID, "delay")

    def result_screen(self):
        return self.search_element(By.CLASS_NAME, "screen")

    def set_delay(self, delay):
        delay_element = self.delay_input()
        delay_element.clear()
        self.send_keys(delay_element, delay)

    def perform_calculation(self, num1, operation, num2):
        self.click_to_element(getattr(self, f"{num1}_num")())
        self.click_to_element(getattr(self, f"{operation}_symbol")())
        self.click_to_element(getattr(self, f"{num2}_num")())
        self.click_to_element(self.equals_symbol())

    def get_result(self):
        return self.text_data(self.result_screen())


def test_calculator():
    driver = webdriver.Chrome()
    calculator_page = CalculatorPage(driver)

    try:
        calculator_page.open()
        sleep(1)

        calculator_page.set_delay(45)
        calculator_page.perform_calculation('seven', 'plus', 'eight')

        sleep(45)

        result = calculator_page.get_result()
        assert result == '15', f"Expected result: 15, Actual result: {result}"

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator()
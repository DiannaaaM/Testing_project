from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class PageObject:

    def open_site(self, driver, link):
        driver.get(link)

    def plus_symbol(self, driver):
        return self.search_element(driver, By.XPATH, "//span[text()='+']")

    def equals_symbol(self, driver):
        return self.search_element(driver, By.XPATH, "//span[text()='=']")

    def seven_num(self, driver):
        return self.search_element(driver, By.XPATH, "//span[text()='7']")

    def eight_num(self, driver):
        return self.search_element(driver, By.XPATH, "//span[text()='8']")

    def delay_num(self, driver):
        # возвращает элемент с id='delay'
        return self.search_element(driver, By.ID, "delay")

    def search_element(self, driver, by, value):
        return driver.find_element(by, value)

    def send_keys(self, element, data):
        element.send_keys(str(data))

    def click_to_element(self, element):
        element.click()

    def text_data(self, element):
        return element.text


def test_calculator():
    driver = webdriver.Chrome()
    page = PageObject()

    page.open_site(driver, 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    sleep(1)

    delay_element = page.search_element(driver, By.ID, "delay")
    delay_element.clear()
    page.send_keys(delay_element, 45)

    page.click_to_element(page.seven_num(driver))

    page.click_to_element(page.plus_symbol(driver))

    page.click_to_element(page.eight_num(driver))

    page.click_to_element(page.equals_symbol(driver))

    sleep(45)

    result_element = page.search_element(driver, By.CLASS_NAME, "screen")
    result_text = page.text_data(result_element)

    assert result_text == '15'

    driver.quit()


if __name__ == "__main__":
    test_calculator()

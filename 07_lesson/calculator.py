from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class PageObject:

    def open_site(self, driver, link):
        driver.get(link)

    def plus_symbol(self, driver):
        return self.search_element(driver,By.XPATH, "//span[text()='+']")

    def equals_symbol(self, driver):
        return self.search_element(driver,By.XPATH, "//span[text()='=']")

    def seven_num(self, driver):
        return self.search_element(driver,By.XPATH, "//span[text()='7']")

    def eight_num(self, driver):
        return self.search_element(driver,By.XPATH, "//span[text()='8']")

    def delay_num(self, driver):
        return self.search_element(driver, By.ID, "delay")

    def search_element(self, driver, by, value):
        return driver.find_element(by, value)

    def send_fields(self, data):
        field = self.search_element.send_key(data)

    def click_to_element(self, element):
        element.click()

    def text_data(self, data):
        return data.text


def test_calculator():
    driver = webdriver.Chrome()
    PageObject.open_site(driver, 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.htm')
    PageObject.click_to_element(PageObject.delay_num(driver))
    PageObject.click_to_element(PageObject.seven_num(driver))
    PageObject.click_to_element(PageObject.plus_symbol(driver))
    PageObject.click_to_element(PageObject.eight_num(driver))
    PageObject.click_to_element(PageObject.equals_symbol(driver))
    sleep(45)
    result = PageObject.text_data(PageObject.search_element(driver, By.CLASS_NAME, "screen"))
    assert result == '45'
    driver.quit()
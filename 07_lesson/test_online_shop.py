from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        username_field = self.driver.find_element(By.ID, 'user-name')
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.driver.find_element(By.NAME, 'login-button')
        login_button.click()


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_id):
        add_to_cart_button = self.driver.find_element(By.ID, product_id)
        add_to_cart_button.click()

    def go_to_cart(self):
        cart_button = self.driver.find_element(By.ID, 'shopping_cart_container')
        cart_button.click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        first_name_field = self.driver.find_element(By.ID, 'first-name')
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name):
        last_name_field = self.driver.find_element(By.ID, 'last-name')
        last_name_field.send_keys(last_name)

    def enter_postal_code(self, postal_code):
        postal_code_field = self.driver.find_element(By.ID, 'postal-code')
        postal_code_field.send_keys(postal_code)

    def click_continue(self):
        continue_button = self.driver.find_element(By.ID, 'continue')
        continue_button.click()

    def get_total(self):
        total_label = self.driver.find_element(By.CLASS_NAME, 'summary_total_label')
        return total_label.text



def test_calculator():
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    login_page = LoginPage(driver)
    login_page.enter_username('standard_user')
    login_page.enter_password('secret_sauce')
    login_page.click_login()

    sleep(2)

    product_page = ProductPage(driver)
    product_page.add_to_cart('add-to-cart-sauce-labs-backpack')
    product_page.add_to_cart('add-to-cart-sauce-labs-bolt-t-shirt')
    product_page.add_to_cart('add-to-cart-sauce-labs-onesie')
    product_page.go_to_cart()

    sleep(2)

    checkout_page = CheckoutPage(driver)
    checkout_page.enter_first_name('Diana')
    checkout_page.enter_last_name('Murlaeva')
    checkout_page.enter_postal_code('427018')
    checkout_page.click_continue()

    sleep(2)

    result = checkout_page.get_total()
    assert result == 'Total: $58.29'
    driver.quit()

if __name__ == "__main__":
    test_calculator()
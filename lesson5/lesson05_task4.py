from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://the-internet.herokuapp.com/login')

driver.find_element_by_id('username').send_keys('tomsmith')
driver.find_element_by_id('password').send_keys('SuperSecretPassword!')

driver.find_element_by_tag_name('button').click()

flash_message = driver.find_element_by_class_name('flash').text
print(flash_message)
driver.quit()

driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/login')

driver.find_element_by_id('username').send_keys('tomsmith')
driver.find_element_by_id('password').send_keys('SuperSecretPassword!')

driver.find_element_by_tag_name('button').click()

flash_message = driver.find_element_by_class_name('flash').text
print(flash_message)
driver.quit()

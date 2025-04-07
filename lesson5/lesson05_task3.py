from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://the-internet.herokuapp.com/inputs')

input_field = driver.find_elements_by_tag_name('input')[0]
input_field.send_keys('Sky')

input_field.clear()

input_field.send_keys('Pro')

driver.quit()
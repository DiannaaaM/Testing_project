from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/classattr')

driver.find_element_by_class_name('btn-primary').click()

driver.quit()

for _ in range(2):
    driver = webdriver.Chrome()
    driver.get('http://uitestingplayground.com/classattr')
    driver.find_element_by_class_name('btn-primary').click()
    driver.quit()

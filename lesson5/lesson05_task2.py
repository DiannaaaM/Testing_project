from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://uitestingplayground.com/dynamicid')

driver.find_element_by_id('btn').click()

driver.quit()

for _ in range(2):
    driver = webdriver.Chrome()
    driver.get('http://uitestingplayground.com/dynamicid')
    driver.find_element_by_id('btn').click()
    driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from time import sleep
from math import *
try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(browser,13).until(ec.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_id('book').click()
    x = int(browser.find_element_by_id('input_value').text)
    result = str(log(abs(12*sin(x))))
    browser.find_element_by_id('answer').send_keys(result)
    browser.find_element_by_id('solve').click()
finally:
    sleep(5)
    browser.quit()

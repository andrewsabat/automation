from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    element_num1 = browser.find_element_by_id("num1")
    num1 = element_num1.text
    element_num2 = browser.find_element_by_id("num2")
    num2 = element_num2.text
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(int(num1) + int(num2)))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

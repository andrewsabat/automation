import math

from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(0.5)
    browser.switch_to.window(browser.window_handles[1])
    value_x = browser.find_element_by_id("input_value").text
    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(calc(value_x))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
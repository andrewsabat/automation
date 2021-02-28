from selenium import webdriver
import time
import math
import os


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    path = os.path.join(os.getcwd(), "my_file.txt")
    inputs = browser.find_elements_by_css_selector(".form-group [required]")
    for input in inputs:
        input.send_keys(" ")
    input_file = browser.find_element_by_css_selector("[type='file']")
    input_file.send_keys(path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link_part', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, link_part):
    link = f"https://stepik.org/lesson/{link_part}/step/1"
    browser.get(link)
    answer = str(math.log(int(time.time())))
    textarea = browser.find_element_by_css_selector('textarea')
    textarea.send_keys(answer)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    feedback = browser.find_element_by_class_name("smart-hints__hint").text
    assert feedback == "Correct!", f"Answer is {feedback}"
    time.sleep(5)




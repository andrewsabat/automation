import time


def test_guest_should_see_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert browser.find_element_by_class_name("btn-add-to-basket") is not True, "Can't find your element, sry :("
    time.sleep(5)

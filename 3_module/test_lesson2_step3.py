from selenium import webdriver
import unittest


class TestInputsInLinks(unittest.TestCase):
    def test_inputs_first_link(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        self.assertTrue(browser.find_element_by_css_selector('[placeholder="Input your first name"]'))
        self.assertTrue(browser.find_element_by_css_selector('[placeholder="Input your last name"]'))
        self.assertTrue(browser.find_element_by_css_selector('[placeholder="Input your email"]'))
        browser.quit()

    def test_inputs_second_link(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        self.assertTrue(browser.find_element_by_css_selector('[placeholder="Input your first name"]'))
        self.assertTrue(browser.find_element_by_css_selector('[placeholder="Input your last name"]'))
        self.assertTrue(browser.find_element_by_css_selector('[placeholder="Input your email"]'))
        browser.quit()


if __name__ == "__main__":
    unittest.main()

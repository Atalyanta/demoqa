from selenium.webdriver.common.by import By
import time


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url   #'https://demoqa.ru'

    def visit(self):
        return self.driver.get(self.base_url)

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):
        if self.get_url() == self.base_url:
            return True
        return False

    #def find_element(self):
    #    time.sleep(3)
    #    return self.driver.find_element()
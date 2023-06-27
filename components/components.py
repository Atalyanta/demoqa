from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class WebElement:
    def __init__(self, driver, locator=''):
        self.driver = driver
        self.locator = locator

    def click(self):            # метод который кликает по элементу, работает только если элеент виден на странице
        self.find_element().click()

    def find_element(self):         # метод ищет элемент
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def find_elements(self):         # метод считает элементы одного типа, выдает их список
        return self.driver.find_elements(By.CSS_SELECTOR, self.locator)

    def check_count_elements(self, count: int): # метод считает элементы одного типа на сатранице
        if len(self.find_elements()) == count:
            return True
        return False

    def exist(self):            # метод, который проверяет существует ли элемент
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True

    def get_text(self):             # метод ищет текст
        return str(self.find_element().text)

    def visible(self):
        return self.find_element().is_displayed()

    def send_keys(self, text: str):         #записать текст в элемент, работает как click
        self.find_element.send_keys(text)




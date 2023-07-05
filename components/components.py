from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class WebElement:
    def __init__(self, driver, locator='', locator_type='css'):
        self.driver = driver
        self.locator = locator
        self.locator_type = locator_type

    def click(self):            # метод который кликает по элементу, работает только если элемент виден на странице
        self.find_element().click()

    def click_force(self):          # принудительно кликает на элемент
        self.driver.execute_script("arguments[0].click();", self.find_element())

    def find_element(self):         # метод ищет элемент
        return self.driver.find_element(self.get_by_type(), self.locator)

    def find_elements(self):         # метод считает элементы одного типа, выдает их список
        return self.driver.find_elements(self.get_by_type(), self.locator)

    def check_count_elements(self, count: int):     # метод считает элементы одного типа на сатранице
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

    def visible(self):              # проверяет видимость элемента
        return self.find_element().is_displayed()

    def send_keys(self, text: str):         # метод добавляет текст в поле
        self.find_element().send_keys(text)

    def clear(self):                        # метод удаляет введенное из поля
        self.find_element().send_keys(Keys.CONTROL + 'a')
        self.find_element().send_keys(Keys.DELETE)

    def get_dom_attribute(self, name: str):             #
        value = self.find_element().get_dom_attribute(name)

        if value is None:
            return False
        if len(value) > 0:
            return value
        return True             #атрибут есть, но значения нет

    def get_by_type(self):
        if self.locator_type == 'id':
            return By.ID
        elif self.locator_type == 'name':
            return By.NAME
        elif self.locator_type == 'xpath':
            return By.XPATH
        elif self.locator_type == 'css':
            return By.CSS_SELECTOR
        elif self.locator_type == 'class':
            return By.CLASS_NAME
        elif self.locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('Locator type ' + self.locator_type + ' not correct')
        return False

    def scroll_to_element(self):
        self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);",
            self.find_element()
        )

    def check_css(self, style, value=''):
        return self.find_element().value_of_css_property(style) == value


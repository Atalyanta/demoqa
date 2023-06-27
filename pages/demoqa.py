from pages.base_page import BasePage
from components.components import WebElement


class Demoqa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')

    #def exist_icon(self):
    #    try:
    #        self.icon.find_element()
    #    except NoSuchElementException:
    #        return False
    #    return True
    # если произошла ошибка "нет элемента на странице", выполняется блок except false

    #def click_on_the_icon(self):
    #    return self.find_element(locator='#app > header > a').click()

    # перенесли в base_page.py
    #def equal_url(self):
    #    if self.get_url() == self.base_url:
    #        return True
    #    return False
from selenium.webdriver.common.by import By
import time


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url   #'https://demoqa.ru'

    def visit(self):            #заходит на страницу
        return self.driver.get(self.base_url)

    def get_url(self):
        return self.driver.current_url

    def equal_url(self):        # проверяет соответствие урл
        if self.get_url() == self.base_url:
            return True
        return False

    def back(self):         #всегда после visit, кнопка "назад" в браузере
        self.driver.back()

    def forward(self):      #всегда после visit, кнопка "вперед" в браузере
        self.driver.forward()

    def refresh(self):      #всегда после visit, обновить в браузере
        self.driver.refresh()

    def get_title(self):    #всегда после visit, тайтл в браузере
        return self.driver.title



    #def find_element(self):
    #    time.sleep(3)
    #    return self.driver.find_element()
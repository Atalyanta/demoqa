from selenium.webdriver.common.by import By
import time
import logging


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

    def back(self):         #всегда после visit, кнопка "назад" в браузере. можно вызывать и от browser, и от страницы, но лучше писать от страницы, чтобы понятно, где мы находимся
        self.driver.back()

    def forward(self):      #всегда после visit, кнопка "вперед" в браузере. +см. коммент выше
        self.driver.forward()

    def refresh(self):      #всегда после visit, обновить в браузере. + см. коммент выше
        self.driver.refresh()

    def get_title(self):    #всегда после visit, тайтл в браузере
        return self.driver.title

    def alert(self):        # возвращает вслывающее окно, можно проверить, что окно отсутствует
        try:                # чтобы проверить, что нет всплыв окна, надо вызвать этот метод с assert not
            return self.driver.switch_to.alert  # лучше в конце каждого теста делать проверку на это
        except Exception as ex:
            logging.log(1, ex)      #лог - это вывести в консоль False
            return False

    #def find_element(self):
    #    time.sleep(3)
    #    return self.driver.find_element()
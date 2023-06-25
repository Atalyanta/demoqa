from pages.elements_page import ElementsPage
from pages.base_page import BasePage
import time


def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)       #создаем объект страницы

    elements_page.visit()                       #от объекта вызываем метод входа на страницу
 #  elements_page.btn_sidebar_first.click()
 #  time.sleep(3)
 #  assert elements_page.btn_sidebar_first_textbox.exist()
    assert elements_page.btn_sidebar_first_textbox.visible()

def test_of_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_page.btn_sidebar_first_checkbox.visible()
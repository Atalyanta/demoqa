from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage
from components.components import WebElement
from pages.base_page import BasePage


def get_text(self):
    return str(self.find_element('.© 2013 - 2020 TOOLSQA.COM | ALL RIGHTS RESERVED.').text)

def test_page_elements(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.text_elements.get_text() == 'Elements'
    assert elements_page.icon.exist()
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()









# driver это то же, что и browser
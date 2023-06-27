from pages.demoqa import Demoqa
from pages.elements_page import ElementsPage


def test_navigation(browser):
    demo_qa_page = Demoqa(browser)
    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    demo_qa_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()

    elements_page = ElementsPage(browser)
    assert elements_page.equal_url()

from pages.demoqa import Demoqa


def test_check_text1(browser):
    demo_qa_page = Demoqa(browser)

    demo_qa_page.visit()

    browser.find_element(‘© 2013 - 2020 TOOLSQA.COM | ALL RIGHTS RESERVED.’, '#app > footer > a')

def test_check_text2(browser):
    demo_qa_page = Demoqa(browser)

    demo_qa_page.visit()
    demo_qa_page.btn_elements.click()
    browser.find_element('Please select an item from left to start practice.')


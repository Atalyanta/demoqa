from pages.demoqa import Demoqa

def test_check_title_demo(browser):
    demo_qa_page = Demoqa(browser)

    demo_qa_page.visit()
    assert browser.title == "DEMOQA"        #тест проверки соответствия title значению DEMOQA

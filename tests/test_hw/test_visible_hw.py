from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accordion = Accordion(browser)
    accordion.visit()
    assert accordion.section1.visible()
    accordion.section1_heading.click()
    time.sleep(2)
    assert not accordion.section1.visible()

def test_visible_accordion_default(browser):
    accordion = Accordion(browser)

    accordion.visit()
    assert not accordion.section2_1.visible()

    accordion.visit()
    assert not accordion.section2_2.visible()

    accordion.visit()
    assert not accordion.section3.visible()

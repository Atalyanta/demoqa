from pages.textbox import TextBox
import time


def test_clear(browser):
    textbox = TextBox(browser)

    textbox.visit()
    textbox.user_name.send_keys('abcd')
    time.sleep(2)
    textbox.user_name.clear()
    time.sleep(2)
    assert textbox.user_name.get_text() == ""

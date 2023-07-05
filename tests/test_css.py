from pages.textbox import TextBox
from components.components import WebElement

def test_text_box_submit(browser):
    textbox = TextBox(browser)
    textbox.visit()

    assert textbox.submit_btn.check_css('color','rgba(255, 255, 255, 1)')
    assert textbox.submit_btn.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    assert textbox.submit_btn.check_css('borderColor', 'rgb(0, 123, 255)')

from pages.textbox import TextBox


def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.full_name.send_keys('abcd')
    text_box.current_address.send_keys('right here')
    text_box.submit_btn.click()
    assert text_box.output.get_text == 'abcd'
 #   assert text_box.output.get_text() == 'right here'

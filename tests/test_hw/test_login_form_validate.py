from pages.form_page import FormPage


def test_log_form_valid(browser):
    formpage = FormPage(browser)

    formpage.visit()
    assert formpage.first_name.get_dom_attribute('placeholder')
    assert formpage.last_name.get_dom_attribute('placeholder')
    assert formpage.user_email.get_dom_attribute('placeholder')
    assert formpage.first_name.get_dom_attribute('pattern')
    assert formpage.last_name.get_dom_attribute('pattern')
    assert formpage.user_email.get_dom_attribute('pattern')
    formpage.btn_submit.click()
    assert formpage.user_form.get_dom_attribute('class') == 'was-validated'

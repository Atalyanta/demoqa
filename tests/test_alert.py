from pages.alerts import Alert
import time


def test_alert(browser):
    alert_page = Alert(browser)
    alert_page.visit()

    alert_page.alert()
    assert not alert_page.alert()
    alert_page.alert_btn.click()
    time.sleep(2)
    assert alert_page.alert()
    alert_page.alert().accept()         # обязательная строка в конце теста, чтобы алерт закрылся


def test_alert_text(browser):           # открыть алерт, проверить текст
    alert_page = Alert(browser)
    alert_page.visit()

    alert_page.alert_btn.click()
    time.sleep(2)
    assert alert_page.alert().text == "You clicked a button"        # здесь text, а не get_text, потому что алертово окно
    alert_page.alert().accept()
    assert not alert_page.alert()


def test_confirm(browser):
    alert_page = Alert(browser)
    alert_page.visit()

    alert_page.confirm_btn.click()
    time.sleep(2)
    alert_page.alert().dismiss()        # нажать "отмена" в окне
    assert alert_page.confirm_result.get_text() == "You selected Cancel"   #сравниваем текст с сайта с эталоном


def test_prompt(browser):
    alert_page = Alert(browser)
    alert_page.visit()

    alert_page.promt_btn.click()
    time.sleep(2)
    alert_page.alert().send_keys('abcd')        #в откывшемся окне пишем в поле текст
    alert_page.alert().accept()
    assert alert_page.prompt_result.get_text() == "You entered abcd"
    time.sleep(2)

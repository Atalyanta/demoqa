from pages.alerts import Alert
import time


def test_alert(browser):
    alert_page = Alert(browser)
    alert_page.visit()
    alert_page.timer_alert_btn.click()
    time.sleep(7)
    assert alert_page.alert()
    alert_page.alert().accept()

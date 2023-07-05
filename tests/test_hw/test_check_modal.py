from pages.modal_dialogs import ModalDialogs
import time


def test_check_modal(browser):
    modal_page = ModalDialogs(browser)

    modal_page.visit()
    modal_page.small_modal.click()
    modal_page.small_modal_close.click()
    assert not modal_page.alert()
    modal_page.large_modal.click()
    modal_page.large_modal_close.click()
    assert not modal_page.alert()

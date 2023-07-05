from pages.browser_tab import BrowserTab
import time


def test_browser_tab(browser):
    browser_tab = BrowserTab(browser)
    browser_tab.visit()

    assert len(browser.window_handles) == 1     # проверяем, что открыта 1 вкладка
    browser_tab.new_tab.click()
    time.sleep(2)
    assert len(browser.window_handles) == 2      # проверяем, что открыто 2 вкладки

    browser.switch_to.window(browser.window_handles[0])     # перейти на 1-ую вкладку
    time.sleep(2)

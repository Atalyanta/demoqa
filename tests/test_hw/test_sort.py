from pages.webtables import Tables
import time


def test_sort(browser):
    tables_page = Tables(browser)
    tables_page.visit()


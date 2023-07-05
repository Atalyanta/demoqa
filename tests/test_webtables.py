import time
from pages.webtables import Tables


def test_webtables(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    assert not page_tables.no_data.exist()

    while page_tables.btn_delete_row.exist():
        page_tables.btn_delete_row.click()

    time.sleep(2)
    assert page_tables.no_data.exist()




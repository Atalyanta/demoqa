import time
from pages.webtables import Tables


def test_webtables(browser):
    page_tables = Tables(browser)
    page_tables.visit()

    page_tables.add_btn.click()

    browser.switch_to.alert.exist()         #проверка на то, что окно открыто
    assert browser.switch_to.alert.no_data.exist() #проверка на то, что поля в окне пустые
    page_tables.submit_btn.btn.click()
    browser.switch_to.alert.exist()
    #проверка на то, что окно не закрылось, что выдает ошибку
                        #заполнить поля
                 #сабмит
                        #открытого окна нет, в таблице на исходной странице новая запись
                        #карандаш на строке записи клик #edit-record-1 > svg
                        #открытая модалка с новые данные exist?
                        #изменить имя и сохранить
                        #в исходном в таблице обновления
                        #нажать на корзину в строке #delete-record-1 > svg > path
                        #данные изменились



from pages.test_koup import Koup
from pages.test_koup2 import Add_remove_el
import time


def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = Add_remove_el(browser)
    koup_page.visit()

    assert koup_page.link_add.exist()    #проверка есть ли на странице ссылка, другой вариант проверки
                                         #assert koup_page.link_add.get_text() == "Add/Remove Elements" (текст на ссылке)


    koup_page.link_add.click()
    assert link_add.equal_url()
    assert koup_add.btn_add.exist()         #проверка есть ли на странице кнопка, другой вариант проверки
                                         #assert koup_add.btn_add.get_text() == "Add Element" (текст на кнопке)

    assert koup_add.btn_add.get_dom_attribute('onclick') == 'addElement()'

    for 1 in range(4):
        koup_add.btn_add.click()
                                                                # проверка для всех элементов
    assert koup_add.btns_delete.check_count_elements(4)   # btns delete не уникальный локатор, подобрать по xpath

    for element in koup_add.btns_delete.find_elements():       # проверка текста на каждой кнопке, что он delete
        assert element.text == "Delete"

  #  проверка только для первого элемента/ строка ошибочная!
  #  assert koup_add.btns_delete.get_text() == 'Delete'


    while koup_add.btns_delete.exist():            #кликнуть на каждую кнопку delete
        koup_add.btns_delete.click()

    assert not koup_add.btns_delete.exist()

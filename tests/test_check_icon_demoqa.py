from pages.demoqa import Demoqa
            # все элементы лежат в basepage

def test_icon_exist(browser):
    demo_qa_page = Demoqa(browser)      # создаем объект, передаем демока
    demo_qa_page.visit()                #  метод есть в  Basepage. действие входа
    demo_qa_page.icon.click()           #страница - элемент - метод
    assert demo_qa_page.equal_url()     #ассерт=проверка, возвращает тру или фолс, проверка урл (что остался тот же)
    assert demo_qa_page.icon.exist()       #ассерт=зайди на страницу, проверь наличие иконки

    # browser.get("https://demoqa.com/")
    # icon = browser.find_element(By.CSS_SELECTOR, "#app > header > a")
    #
    # if icon is None:
    #     print("Элемент не найден")
    # else:
    #     print("Элемент найден")
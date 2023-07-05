from pages.droppable import Drop
import time
from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):
    drag_drop = Drop(browser)
    action_chains = ActionChains(browser)

    drag_drop.visit()

    assert drag_drop.drop.check_css('backgroundColor', 'rgba(0, 0, 0)')  # цвета фона у таргет по умолчанию не было

    action_chains.drag_and_drop(            # в скобках пишем элемент который тащим, потом куда
        drag_drop.drag.find_element(),      # element
        drag_drop.drop.find_element()       # target
    ).perform()

    time.sleep(1)

    assert drag_drop.drop.check_css_new('backgroundColor', 'rgba(70, 130, 180, 1)')   # цвет фона тарг после перемещения

    time.sleep(1)

    action_chains.drag_and_drop(        # перемещаем обратно по тому же принципу
        drag_drop.drag.find_element(),  # element
        -200, 0                         # target - сюда любые координаты
    ).perform()

    time.sleep(1)

    assert drag_drop.drop.check_css_new('backgroundColor', 'rgba(70, 130, 180, 1)')  # цвет фона таргет после возврата
                                                                                 # элемента в исходное положение

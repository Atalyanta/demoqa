import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 1000)     #меняем размер окна, меняет и обратно не возвращает, надо в тест добавлять обратную
    yield driver
    driver.quit()

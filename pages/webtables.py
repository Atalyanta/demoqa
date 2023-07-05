from pages.base_page import BasePage
from components.components import WebElement


class Tables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_rows_found = WebElement(driver, 'div.rt-noData')
        self.trash_btns = WebElement(driver, '#delete-record-1 > svg > path')
        self.add_btn = WebElement(driver, '#addNewRecordButton')
#модальное окно
        self.submit_btn = WebElement(driver, '#submit')
        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')





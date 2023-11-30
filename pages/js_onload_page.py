from pages.locators import JSOnloadLocators, BasePageLocators
from pages.base.base_page import BasePage


class JSOnload(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*JSOnloadLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*JSOnloadLocators.PAGE_NAME)
        correct_text = 'onload event.'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_correct_console_log(self):
        log = self.get_browser_console_log()
        text = "xyz"
        new_log = [i['message'] for i in log if text in i['message']]
        print(new_log)
        assert len(new_log) == 1, f"should be {text} in {new_log}, but not"
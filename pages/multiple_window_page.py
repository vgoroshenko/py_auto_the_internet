from pages.locators import MultipleWindowLocators, BasePageLocators
from pages.base.base_page import BasePage


class MultipleWindow(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*MultipleWindowLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Opening a new window'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_correct_new_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'New Window'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def go_to_new_page(self):
        button = self.browser.find_element(*MultipleWindowLocators.BUTTON)
        button.click()

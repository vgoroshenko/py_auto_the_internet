from pages.locators import ShadowDOMLocators, BasePageLocators
from pages.base.base_page import BasePage
import os


class Shadowdom(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*ShadowDOMLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*ShadowDOMLocators.PAGE_NAME)
        correct_text = 'Simple template'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_correct_all_text(self):
        self.should_be_correct_first_text()
        self.should_be_correct_second_text()
        self.should_be_correct_third_text()

    def should_be_correct_first_text(self):
        text = self.get_text(*ShadowDOMLocators.FIRST_TEXT)
        correct_text = 'different text!'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_correct_second_text(self):
        text = self.get_text(*ShadowDOMLocators.SECOND_TEXT)
        correct_text = 'different text!'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_correct_third_text(self):
        text = self.get_text(*ShadowDOMLocators.THIRD_TEXT)
        correct_text = 'In a list!'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'


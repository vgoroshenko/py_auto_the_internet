from pages.locators import RedirectLinkLocators, BasePageLocators
from pages.base.base_page import BasePage
import requests


class RedirectLink(BasePage):


    def go_to_page(self):
        link = self.browser.find_element(*RedirectLinkLocators.LOADED_PAGE)
        link.click()

    def go_to_page_status_code(self):
        link = self.browser.find_element(*RedirectLinkLocators.BUTTON_REDIRECT)
        link.click()

    def should_be_redirection_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Redirection'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_status_code_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Status Codes'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

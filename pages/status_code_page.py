from pages.locators import StatusCodeLocators, BasePageLocators
from pages.base.base_page import BasePage
import requests


class StatusCode(BasePage):


    def go_to_page(self):
        link = self.browser.find_element(*StatusCodeLocators.LOADED_PAGE)
        link.click()

    def go_to_page_200(self):
        link = self.browser.find_element(*StatusCodeLocators.BUTTON_200)
        link.click()

    def go_to_page_301(self):
        link = self.browser.find_element(*StatusCodeLocators.BUTTON_301)
        link.click()

    def go_to_page_404(self):
        link = self.browser.find_element(*StatusCodeLocators.BUTTON_404)
        link.click()

    def go_to_page_501(self):
        link = self.browser.find_element(*StatusCodeLocators.BUTTON_501)
        link.click()

    def return_to_status_code_page(self):
        link = self.browser.find_element(*StatusCodeLocators.BUTTON_RETURN)
        link.click()

    def should_be_redirection_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Redirection'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_status_code_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Status Codes'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_page_with_code_text(self, code):
        text = self.get_text(*StatusCodeLocators.STATUS_CODE_TEXT)
        correct_text = str(code)
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_correct_status_code(self, code):
        # status_code = self.browser.execute_script("return window.performance.timing.responseEnd - window.performance.timing.requestStart;")
        response = requests.get(self.browser.current_url)
        status_code = response.status_code
        assert code in status_code, f'should be {code}, but "{status_code}"'
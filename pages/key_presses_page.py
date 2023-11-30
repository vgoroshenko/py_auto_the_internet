from pages.locators import KeyPressesLocators, BasePageLocators
from pages.base.base_page import BasePage


class KeyPresses(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*KeyPressesLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Key Presses'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_correct_entered_chars_with_text(self,text):
        input = self.browser.find_element(*KeyPressesLocators.INPUT_TEXT)
        for char in text:
            input.send_keys(char)
            result = self.browser.find_element(*KeyPressesLocators.INPUT_TEXT_RESULT).text
            assert char.upper() in result, f'should be {char}, but "{result}"'

    def should_be_result_dont_present(self):
        result = self.is_element_displayed(self.browser.find_element(*KeyPressesLocators.INPUT_TEXT_RESULT))
        assert result == False, 'should be result dont present, but not'

from pages.locators import HoverLocators, BasePageLocators
from pages.base.base_page import BasePage


class Hover(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*HoverLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Hovers'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'
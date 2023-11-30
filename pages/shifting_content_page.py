import time

from pages.locators import ShiftingContentLocators, BasePageLocators
from pages.base.base_page import BasePage
import os


class ShiftingContent(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*ShiftingContentLocators.LOADED_PAGE)
        link.click()

    def go_to_example_1_page(self):
        button = self.browser.find_element(*ShiftingContentLocators.BUTTON_EXAMPLE_1)
        button.click()

    def go_to_example_2_page(self):
        button = self.browser.find_element(*ShiftingContentLocators.BUTTON_EXAMPLE_2)
        button.click()

    def go_to_example_3_page(self):
        button = self.browser.find_element(*ShiftingContentLocators.BUTTON_EXAMPLE_3)
        button.click()

    def use_mode_random(self):
        button = self.browser.find_element(*ShiftingContentLocators.BUTTON_MODE_RANDOM)
        button.click()

    def use_mode_pixel_shift(self):
        button = self.browser.find_element(*ShiftingContentLocators.BUTTON_MODE_PIXEL_SHIFT)
        button.click()

    def use_mode_random_pixel_shift(self):
        button = self.browser.find_element(*ShiftingContentLocators.BUTTON_MODE_RANDOM_PIXEL_SHIFT)
        button.click()

    def use_mode_image_type(self):
        button = self.browser.find_element(*ShiftingContentLocators.BUTTON_IMAGE_TYPE)
        button.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Shifting Content'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_change_text_after_refresh(self):
        text = self.get_text(*ShiftingContentLocators.LIST_TEXT)
        self.browser.refresh()
        text_after = self.get_text(*ShiftingContentLocators.LIST_TEXT)
        assert text != text_after, 'text should be changed, but not'

    def should_be_100_pixel_shift(self):
        initial_location = self.browser.find_element(*ShiftingContentLocators.BUTTON_MOVED).location
        button_pixel_shift = self.browser.find_element(*ShiftingContentLocators.BUTTON_MODE_PIXEL_SHIFT)
        button_pixel_shift.click()
        assert initial_location['x'] != initial_location['x']-100, f'should be update location {initial_location} - 100'

    def should_be_image_100_pixel_shift(self):
        initial_location = self.browser.find_element(*ShiftingContentLocators.BUTTON_MOVED).location
        button_pixel_shift = self.browser.find_element(*ShiftingContentLocators.BUTTON_MODE_IMAGE_PIXEL_SHIFT)
        button_pixel_shift.click()
        assert initial_location['x'] != initial_location['x']-100, f'should be update location {initial_location} - 100'

    def should_be_text_shift(self):
        text = self.get_text(*ShiftingContentLocators.LIST_TEXT)
        self.browser.refresh()
        text_after = self.get_text(*ShiftingContentLocators.LIST_TEXT)
        assert text != text_after, f'should be {text} not in {text_after}'

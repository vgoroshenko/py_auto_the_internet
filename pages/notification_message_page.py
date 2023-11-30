import time

from pages.locators import NotificationMessagesLocators, BasePageLocators
from pages.base.base_page import BasePage


class NotificationMessages(BasePage):

    def click_load_new_message(self):
        button = self.browser.find_element(*NotificationMessagesLocators.BUTTON_ACTION)
        button.click()

    def click_close_notif(self):
        button = self.browser.find_element(*NotificationMessagesLocators.BUTTON_CLOSE_NOTIF)
        button.click()

    def go_to_page(self):
        link = self.browser.find_element(*NotificationMessagesLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Notification Message'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_success_notif(self):
        text = self.get_text(*NotificationMessagesLocators.NOTIFICATION)
        correct_text = 'Action successful'
        while correct_text not in text:
            self.click_load_new_message()
            text = self.get_text(*NotificationMessagesLocators.NOTIFICATION)
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_unsuccess_notif(self):
        text = self.get_text(*NotificationMessagesLocators.NOTIFICATION)
        correct_text = 'Action unsuccesful'
        while correct_text not in text:
            self.click_load_new_message()
            text = self.get_text(*NotificationMessagesLocators.NOTIFICATION)
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_dont_present_notif(self):
        notif = self.is_disappeared(*NotificationMessagesLocators.NOTIFICATION)
        assert notif == True, f'should be dont present notification, but not"'

    def should_be_present_notif(self):
        notif = self.is_element_present(*NotificationMessagesLocators.NOTIFICATION)
        assert notif == True, f'should be present notification, but not"'


from pages.locators import JSAlertsLocators, BasePageLocators
from pages.base.base_page import BasePage


class JSAlerts(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*JSAlertsLocators.LOADED_PAGE)
        link.click()

    def click_js_alert(self):
        button = self.browser.find_element(*JSAlertsLocators.JS_ALERT)
        button.click()

    def click_js_alert_confirm(self):
        button = self.browser.find_element(*JSAlertsLocators.JS_ALERT_CONFIRM)
        button.click()

    def click_js_alert_promt(self):
        button = self.browser.find_element(*JSAlertsLocators.JS_ALERT_PROMT)
        button.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'JavaScript Alerts'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_js_alert_text(self):
        text = self.get_alert_text()
        correct_text = 'I am a JS Alert'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_confirm_alert_text(self):
        text = self.get_alert_text()
        correct_text = 'I am a JS Confirm'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_prompt_alert_text(self):
        text = self.get_alert_text()
        correct_text = 'I am a JS prompt'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_js_result(self):
        text = self.browser.find_element(*JSAlertsLocators.RESULT_TEXT).text
        correct_text = 'You successfully clicked an alert'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_js_alert_result(self):
        text = self.browser.find_element(*JSAlertsLocators.RESULT_TEXT).text
        correct_text = 'You successfully clicked an alert'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_js_confirm_success_result(self):
        text = self.browser.find_element(*JSAlertsLocators.RESULT_TEXT).text
        correct_text = 'You clicked: Ok'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_js_confirm_cancel_result(self):
        text = self.browser.find_element(*JSAlertsLocators.RESULT_TEXT).text
        correct_text = 'You clicked: Cancel'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_js_prompt_cancel_result(self):
        text = self.browser.find_element(*JSAlertsLocators.RESULT_TEXT).text
        correct_text = 'You entered: null'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def should_be_js_prompt_success_result(self):
        text = self.browser.find_element(*JSAlertsLocators.RESULT_TEXT).text
        correct_text = 'You entered: test'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def set_text_in_promt(self):
        text = 'test'
        self.alert_set_text(text)
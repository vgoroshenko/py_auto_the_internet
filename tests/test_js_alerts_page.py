from pages.js_alrerts_page import JSAlerts


def test_go_to_page(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_js_alert_present(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.click_js_alert()
    page.should_be_js_alert_text()

def test_js_confirm_alert_present(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.click_js_alert_confirm()
    page.should_be_confirm_alert_text()

def test_js_prompt_alert_present(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.click_js_alert_promt()
    page.should_be_prompt_alert_text()

def test_js_alert_dont_present(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.click_js_alert()
    page.alert_accept()
    page.alert_is_not_present()

def test_js_confirm_alert_dont_present(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.click_js_alert_confirm()
    page.alert_accept()
    page.alert_is_not_present()

def test_js_prompt_alert_dont_present(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.click_js_alert_promt()
    page.alert_accept()

def test_js_alert_result(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.click_js_alert()
    page.alert_accept()
    page.should_be_js_alert_result()

def test_js_confirm_alert_result(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.click_js_alert_confirm()
    page.alert_accept()
    page.should_be_js_confirm_success_result()

def test_js_confirm_alert_cancel_result(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.click_js_alert_confirm()
    page.alert_dismiss()
    page.should_be_js_confirm_cancel_result()

def test_js_prompt_alert_result(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.click_js_alert_promt()
    page.set_text_in_promt()
    page.alert_accept()
    page.should_be_js_prompt_success_result()

def test_js_prompt_cancel_alert_result(browser):
    page = JSAlerts(browser)
    page.go_to_page()
    page.click_js_alert_promt()
    page.alert_dismiss()
    page.should_be_js_prompt_cancel_result()
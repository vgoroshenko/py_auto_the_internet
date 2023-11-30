from pages.notification_message_page import NotificationMessages


def test_go_to_page(browser):
    page = NotificationMessages(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_present_notification(browser):
    page = NotificationMessages(browser)
    page.go_to_page()
    page.click_load_new_message()
    page.should_be_present_notif()

def test_success_notification(browser):
    page = NotificationMessages(browser)
    page.go_to_page()
    page.click_load_new_message()
    page.should_be_success_notif()

def test_unsuccess_notification(browser):
    page = NotificationMessages(browser)
    page.go_to_page()
    page.click_load_new_message()
    page.click_load_new_message()
    page.should_be_unsuccess_notif()

def test_close_notification(browser):
    page = NotificationMessages(browser)
    page.go_to_page()
    page.click_load_new_message()
    page.click_close_notif()
    page.should_be_dont_present_notif()



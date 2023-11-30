from pages.js_onload_page import JSOnload


def test_go_to_page(browser):
    page = JSOnload(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_error_in_console(browser):
    page = JSOnload(browser)
    page.go_to_page()
    page.should_be_correct_console_log()




from pages.key_presses_page import KeyPresses


def test_go_to_page(browser):
    page = KeyPresses(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_dont_present_result(browser):
    page = KeyPresses(browser)
    page.go_to_page()
    page.should_be_result_dont_present()

def test_result_entered_text(browser):
    page = KeyPresses(browser)
    page.go_to_page()
    page.should_be_correct_entered_chars_with_text('test')




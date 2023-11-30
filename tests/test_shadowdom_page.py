from pages.shadowdom_page import Shadowdom


def test_go_to_page(browser):
    page = Shadowdom(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_correct_text_page(browser):
    page = Shadowdom(browser)
    page.go_to_page()
    page.should_be_correct_all_text()


from pages.hovers_page import Hover


def test_go_to_page(browser):
    page = Hover(browser)
    page.go_to_page()
    page.should_be_correct_page()
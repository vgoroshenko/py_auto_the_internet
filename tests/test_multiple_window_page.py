from pages.multiple_window_page import MultipleWindow


def test_go_to_page(browser):
    page = MultipleWindow(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_go_to_new_page(browser):
    page = MultipleWindow(browser)
    page.go_to_page()
    page.go_to_new_page()
    page.switch_window()
    page.should_be_correct_new_page()




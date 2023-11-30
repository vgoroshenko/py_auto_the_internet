from pages.redirect_link_page import RedirectLink


def test_go_to_page(browser):
    page = RedirectLink(browser)
    page.go_to_page()
    page.should_be_redirection_page()

def test_go_to_redirect_page(browser):
    page = RedirectLink(browser)
    page.go_to_page()
    page.go_to_page_status_code()
    page.should_be_status_code_page()


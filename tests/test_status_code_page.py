from pages.status_code_page import StatusCode


def test_go_to_page(browser):
    page = StatusCode(browser)
    page.go_to_page()
    page.should_be_status_code_page()

def test_go_to_status_200_page(browser):
    page = StatusCode(browser)
    page.go_to_page()
    page.go_to_page_200()
    page.should_be_page_with_code_text(200)

def test_go_to_status_301_page(browser):
    page = StatusCode(browser)
    page.go_to_page()
    page.go_to_page_301()
    page.should_be_page_with_code_text(301)

def test_go_to_status_404_page(browser):
    page = StatusCode(browser)
    page.go_to_page()
    page.go_to_page_404()
    page.should_be_page_with_code_text(404)

def test_go_to_status_501_page(browser):
    page = StatusCode(browser)
    page.go_to_page()
    page.go_to_page_501()
    page.should_be_page_with_code_text(500)

# def test_status_200_page(browser):
#     page = StatusCode(browser)
#     page.go_to_page()
#     page.go_to_page_status_code()
#     page.go_to_page_200()
#     page.should_be_correct_status_code(200)


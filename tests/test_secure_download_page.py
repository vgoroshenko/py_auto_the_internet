from pages.secure_download_page import SecureFileDownload


def test_success_login(browser):
    page = SecureFileDownload(browser)
    page.go_to_auth()
    page.should_be_correct_page()

def test_fail_login(browser):
    page = SecureFileDownload(browser)
    page.go_to_fail_auth()
    page.should_be_present_failed_message()

def test_download(browser):
    page = SecureFileDownload(browser)
    page.go_to_auth()
    page.download_file()
    page.should_be_downloaded_file()


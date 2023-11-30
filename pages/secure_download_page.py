from pages.locators import SecureFileDownloadLinkLocators,BasicAuthLocators, BasePageLocators
from pages.base.base_page import BasePage
import os


class SecureFileDownload(BasePage):

    def download_file(self):
        button = self.browser.find_element(*SecureFileDownloadLinkLocators.BUTTON_DOWNLOAD)
        button.click()


    def go_to_page(self):
        link = self.browser.find_element(*SecureFileDownloadLinkLocators.LOADED_PAGE)
        link.click()

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'Secure File Downloader'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'

    def go_to_auth(self):
        self.browser.get('http://admin:admin@172.17.0.1:5000/download_secure')

    def go_to_fail_auth(self):
        self.browser.get('http://admin:admin1@172.17.0.1:5000/download_secure')

    def should_be_present_failed_message(self):
        text = self.browser.find_element(*BasicAuthLocators.FAILED_MESSAGE).text
        assert '' in text, f'should be Not authorized, but present {text}'

    def should_be_downloaded_file(self):
        def is_docker():
            return False if os.name == 'nt' else True

        if is_docker():
            user = os.getlogin()
            download_dir = f"/home/{user}/Downloads"
        else:
            download_dir = f"E:\\Downloads"
        file_name = "some-file.txt"
        file_path = os.path.join(download_dir, file_name)
        assert os.path.exists(file_path), f'should be downloaded file, but not'
import os
from pages.locators import FileDownloadLocators, BasePageLocators
from pages.base.base_page import BasePage


class FileDownloader(BasePage):

    def go_to_page(self):
        link = self.browser.find_element(*FileDownloadLocators.LOADED_PAGE)
        link.click()

    def download_file(self):
        button = self.browser.find_element(*FileDownloadLocators.FILE)
        button.click()

    def should_be_downloaded_file(self):
        user = os.getlogin()
        download_dir = f"/home/{user}/Downloads"
        file_name = "some-file.txt"
        file_path = os.path.join(download_dir, file_name)
        assert os.path.exists(file_path), f'should be downloaded file, but not'

    def should_be_correct_page(self):
        text = self.get_text(*BasePageLocators.PAGE_NAME)
        correct_text = 'File Downloader'
        assert correct_text in text, f'should be {correct_text}, but "{text}"'
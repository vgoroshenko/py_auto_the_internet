from pages.shifting_content_page import ShiftingContent


def test_go_to_page(browser):
    page = ShiftingContent(browser)
    page.go_to_page()
    page.should_be_correct_page()

def test_example_1_100_pixel_shift(browser):
    page = ShiftingContent(browser)
    page.go_to_page()
    page.go_to_example_1_page()
    page.should_be_100_pixel_shift()

def test_example_2_100_pixel_shift(browser):
    page = ShiftingContent(browser)
    page.go_to_page()
    page.go_to_example_2_page()
    page.should_be_image_100_pixel_shift()

def test_example_3_100_pixel_shift(browser):
    page = ShiftingContent(browser)
    page.go_to_page()
    page.go_to_example_3_page()
    page.should_be_text_shift()



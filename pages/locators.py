from selenium.webdriver.common.by import By


class ABPageLocators():
    NO_AB_TEXT = (By.CSS_SELECTOR, 'h3')
    AB_PAGE = (By.XPATH, "//a[contains(@href, 'abtest')]")


class AddRemoveLocators():
    ADD_REMOVE_PAGE = (By.XPATH, "//a[contains(@href, '/add_remove_elements/')]")
    ADD_BUTTON = (By.CSS_SELECTOR, "button[onclick='addElement()']")
    DELETE_BUTTON = (By.CSS_SELECTOR, ".added-manually")
    DELETE_BUTTONS = (By.CSS_SELECTOR, "#elements")


class BasicAuthLocators():
    BASIC_AUTH_PAGE = (By.XPATH, "//a[contains(@href, 'basic')]")
    CONGRAT_MESSAGE = (By.CSS_SELECTOR, 'p')
    FAILED_MESSAGE = (By.CSS_SELECTOR, 'body')


class BrokenImagesLocators():
    BROKEN_IMAGE_PAGE = (By.XPATH, "//a[contains(@href, '/broken_images')]")
    PAGE_NAME = (By.CSS_SELECTOR, 'h3')


class ChallengingDomLocators():
    PAGE_NAME = (By.CSS_SELECTOR, 'h3')
    CHALLENGING_DOM_PAGE = (By.XPATH, "//a[@href='/challenging_dom']")
    FIRST_BUTTON = (By.CSS_SELECTOR, "[class='button']")
    SECOND_BUTTON = (By.CSS_SELECTOR, ".button.alert")
    THIRD_BUTTON = (By.CSS_SELECTOR, ".button.success")
    ANSWER = (By.CSS_SELECTOR, '#canvas')

class CheckboxesLocators():
    PAGE_NAME = (By.CSS_SELECTOR, 'h3')
    CHECKBOXES_PAGE = (By.XPATH, "//a[@href='/checkboxes']")
    FIRST_CHECKBOX = (By.CSS_SELECTOR, 'input:nth-of-type(1)')
    SECOND_CHECKBOX = (By.CSS_SELECTOR, 'input:nth-of-type(2)')

class ContextMenuLocators():
    PAGE_NAME = (By.CSS_SELECTOR, 'h3')
    CONTEXT_PAGE = (By.XPATH, "//a[@href='/context_menu']")
    BOX_BUTTON = (By.CSS_SELECTOR, '#hot-spot')

class BasePageLocators():
    PAGE_NAME = (By.CSS_SELECTOR, 'h3')

class DisappearingElementsLocators():
    DISAPPERATING_PAGE = (By.XPATH, "//a[@href='/disappearing_elements']")
    BUTTON_LIST = (By.XPATH, '//li//a')

class DragAndDropLocators():
    DRAG_AND_DROP_PAGE = (By.XPATH, "//a[@href='/drag_and_drop']")
    BOX_A = (By.CSS_SELECTOR, '#column-a')
    BOX_B = (By.CSS_SELECTOR, '#column-b')

class DropdownLocators():
    DROPDOWN_PAGE = (By.XPATH, "//a[@href='/dropdown']")
    DROPDOWN_BUTTON = (By.CSS_SELECTOR, '#dropdown')
    DROPDOWN_FIRST_ELEMENT = (By.CSS_SELECTOR, "option[value='1']")
    DROPDOWN_SECOND_ELEMENT = (By.CSS_SELECTOR, "option[value='2']")

class DynamicContentLocators():
    DYNAMIC_CONTENT_page = (By.XPATH, "//a[@href='/dynamic_content']")
    CHANGE_CONTENT_BUTTON = (By.XPATH, "//a[contains(@href, 'with')]")




class UrlLocators():
    MAIN_URL = "http://172.17.0.1:5000/"
    #MAIN_URL = "http://localhost:5000/"

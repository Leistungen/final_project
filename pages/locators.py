from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    ADDED_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert.alert-success > .alertinner > strong")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > .alert > .alertinner > p > strong")
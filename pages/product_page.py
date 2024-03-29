from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def check_basket(self):
        self.product_should_be_added()
        self.should_be_correct_price()

    def product_should_be_added(self):
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        book_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert success_message.text == book_name.text, "Added wrong book"

    def should_be_correct_price(self):
        price_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        book_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert price_in_basket.text == book_price.text, "Wrong book price in basket"

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
        
    def should_dissapeare_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is not dissapeared, but should"
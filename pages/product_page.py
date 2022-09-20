from .base_page import BasePage
from .locators import BasketPageLocators
import time

class ProductPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_link()
        self.go_to_basket_page()
        self.should_be_code()
        self.check_name_in_basket()
        self.check_price_in_basket()
    
    def should_be_basket_link(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_LINK), "Basket link is not presented"

    def go_to_basket_page(self):
        self.browser.find_element(*BasketPageLocators.BASKET_LINK).click() 

    def should_be_code(self):
        self.solve_quiz_and_get_code()

    def  check_name_in_basket(self):
        product = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME).text
        product_basket = self.browser.find_element(*BasketPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_basket == product, "Product is not present"

    def check_price_in_basket(self):
        price = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE).text
        price_basket = self.browser.find_element(*BasketPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert price_basket == price, "Price is not present"


   
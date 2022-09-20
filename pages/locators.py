from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():    
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_for")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_for")
  
class BasketPageLocators():  
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR,"#messages .alert-success:first-child strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".product_main .price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR,"#messages .alert-info strong")
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
class LoginPageLocators(object):    
    login_form = (By.CSS_SELECTOR, "#login_form.well")
    register_form = (By.CSS_SELECTOR, "#register_form.well")
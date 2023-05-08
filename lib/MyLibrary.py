from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver

# This import does not work yet
from pageobjects.page_objects import *


class MyLibrary:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_browser_and_navigate_to_main_page(self):
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")

    def click_log_in_link_on_navigation_bar(self):
        NavigationBar(self.driver).click_log_in_link()

    # def click_cart_link_on_navigation_bar(self):
    #     NavigationBar(self.driver).click_cart_link()
    #
    # def close_driver(self):
    #     self.driver.quit()
    #
    # def log_in_as_user_with_parameters(self, username: str, password: str):
    #     LogInForm(self.driver).log_in_as_user(User(username, password))
    #
    # def assert_that_user_sees_welcome_label_with_name(self, username: str):
    #     assert NavigationBar(self.driver).get_welcome_label_text() == f'Welcome {username}'
    #
    # def assert_that_user_sees_log_out_link_on_the_main_page(self):
    #     assert NavigationBar(self.driver).is_log_out_link_displayed()
    #
    # def user_clicks_monitor_category(self):
    #     MainPage(self.driver).click_monitors_category()
    #
    # def user_clicks_product_by_title(self, title: str):
    #     MainPage(self.driver).click_product_by_title(title)
    #
    # def get_highest_price_product_title(self):
    #     return MainPage(self.driver).get_product_with_highest_price().title
    #
    # def get_highest_price_product_price(self):
    #     return MainPage(self.driver).get_product_with_highest_price().price
    #
    # def assert_that_user_sees_product_title_on_the_page(self, title: str):
    #     assert ProductPage(self.driver).get_product_title() == title
    #
    # def assert_that_user_sees_product_price_on_the_page(self, price: str):
    #     assert price in ProductPage(self.driver).get_product_price()
    #
    # def user_clicks_add_to_cart_button_and_close_alert_on_product_page(self):
    #     product_page = ProductPage(self.driver)
    #     product_page.click_add_to_cart()
    #     product_page.close_alert()
    #
    # def assert_that_product_with_title_and_price_displayed_in_the_cart(self, title: str, price: str):
    #     assert any(product == Product(title, price)
    #                for product in CartPage(self.driver).get_all_products())

    @keyword("Get Current URL")
    def get_current_url(self):
        return BuiltIn().get_library_instance('SeleniumLibrary').get_location()

    @keyword("Click Element If Present")
    def click_element_if_present(self, locator):
        seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary')
        if seleniumlib.page_should_contain_element(locator):
            seleniumlib.click_element(locator)
            return True
        else:
            return False

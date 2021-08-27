from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_product_name_in_basket(self):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        print("product_name = ", product_name.text)
        print("product_name_in_basket = ", product_name_in_basket.text)
        assert product_name.text == product_name_in_basket.text, "Название продукта отличается от названия в корзине!"

    def check_product_price_in_basket(self):
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert float(product_price_in_basket.text[1:]) >= float(product_price.text[1:]), "Цена товара отличается от " \
                                                                                         "цены в корзине! "

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение отображается, но не " \
                                                                                  "должно было отображаться! "

    def message_is_dissappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение не исчезло, но должно было!"

from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_PRODUCT), "В корзине находится товар, хотя не должен!"

    def should_be_empty_text_in_basket(self):
        empty_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT)
        print("empty_text.text=  ", empty_text.text)
        assert empty_text.text in "Continue shopping", "В корзине находится товар, хотя не должен быть!"
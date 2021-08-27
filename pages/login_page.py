from .base_page import BasePage
from .locators import LoginPageLocators
import random

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "Login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        inp_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        inp_email.send_keys(email)
        inp_pass = self.browser.find_element(*LoginPageLocators.PASS)
        inp_pass.send_keys(password)
        inp_confirm_pass = self.browser.find_element(*LoginPageLocators.CONF_PASS)
        inp_confirm_pass.send_keys(password)
        btn_reg = self.browser.find_element(*LoginPageLocators.BTN_REG)
        btn_reg.click()

    def user_login_to_account(self):
        assert self.is_element_present(*LoginPageLocators.LOGOUT), "Пользователь не зашел в аккаунт, регистрация не " \
                                                                   "проведена! "
    def generate_password(self, lenght):
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        password = ""
        for i in range(lenght):
            password += chars[random.randint(0, len(chars))]
        return password


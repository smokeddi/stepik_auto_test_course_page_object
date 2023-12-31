from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
class MainPage(BasePage):
	def go_to_login_page(self): #клик на кнопку login *-значит что мы передали пару
		login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
		login_link.click()
		# return LoginPage(browser=self.browser, url=self.browser.current_url)
	def should_be_login_link(self): #проверяем что есть ссылка на вход
		assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
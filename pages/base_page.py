from selenium.common.exceptions import NoSuchElementException
class BasePage():
	def __init__(self, browser, url): #объявляем конструктор
		self.browser = browser
		self.url = url

	def open(self): #открываем ссылку в браузере
		self.browser.get(self.url)

	def __init__(self, browser, url, timeout=10):#команда для неявного ожидания со значением по умолчанию в 10
		self.browser = browser
		self.url = url
		self.browser.implicitly_wait(timeout)

	def is_element_present(self, how, what):#Перехват исключения.
		# В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
		# Чтобы перехватывать исключение, нужна конструкция try/except
		try:
			self.browser.find_element(how, what)
		except NoSuchElementException:
			return False
		return True
# *-* coding: utf-8 *-*
from selenium.webdriver.chrome.webdriver import WebDriver
from fixture_admin_console.admin_console.menu_bar import MenuHelper
from fixture_admin_console.admin_console.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.admin_console_session = SessionHelper(self)
        self.admin_console_menu = MenuHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_admin_console_page(self):
        wd = self.wd
        wd.get('http://localhost/litecart/admin')

    def open_home_page(self):
        wd = self.wd
        wd.get('http://localhost/litecart')


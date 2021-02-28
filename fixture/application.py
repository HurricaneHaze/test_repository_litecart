# *-* coding: utf-8 *-*
from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.admin_console.countries_page import CountriesHelper
from fixture.admin_console.menu_bar import MenuHelper
from fixture.admin_console.session import SessionHelper
from fixture.litecart.duck_page import DuckPageHelper
from fixture.litecart.home_page import HomePageHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.ad_session = SessionHelper(self)
        self.ad_menu = MenuHelper(self)
        self.ad_countries = CountriesHelper(self)

        self.home_page = HomePageHelper(self)
        self.duck_page = DuckPageHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_admin_console_page(self):
        wd = self.wd
        wd.get('http://localhost/litecart/admin')

    def open_home_page(self):
        wd = self.wd
        wd.get('http://localhost/litecart')

    def open_previous_page(self):
        wd = self.wd
        wd.back()

    def get_current_url(self) -> str:
        wd = self.wd
        return wd.current_url

# *-* coding: utf-8 *-*
from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.admin_console.countries_page import CountriesHelperAD
from fixture.admin_console.menu_bar import MenuHelperAD
from fixture.admin_console.session import SessionHelperAD
from fixture.litecart.duck_page import DuckPageHelper
from fixture.litecart.home_page import HomePageHelper
from fixture.litecart.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.ad_session = SessionHelperAD(self)
        self.ad_menu = MenuHelperAD(self)
        self.ad_countries = CountriesHelperAD(self)

        self.home_page = HomePageHelper(self)
        self.duck_page = DuckPageHelper(self)
        self.session = SessionHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

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

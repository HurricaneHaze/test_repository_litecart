# *-* coding: utf-8 *-*

class HomePageHelper:

    def __init__(self, app):
        self.app = app

    def find_blue_duck_in_most_popular(self):
        wd = self.app.wd
        blue_duck = wd.find_element_by_css_selector('#box-most-popular .link[title*=Blue]')
        return blue_duck

    def find_green_duck_in_most_popular(self):
        wd = self.app.wd
        green_duck = wd.find_element_by_css_selector('#box-most-popular .link[title*=Green]')
        return green_duck

    def find_yellow_duck_in_most_popular(self):
        wd = self.app.wd
        yellow_duck = wd.find_element_by_css_selector('#box-most-popular .link[title*=Yellow]')
        return yellow_duck

    def find_red_duck_in_most_popular(self):
        wd = self.app.wd
        red_duck = wd.find_element_by_css_selector('#box-most-popular .link[title*=Red]')
        return red_duck

    def find_purple_duck_in_most_popular(self):
        wd = self.app.wd
        purple_duck = wd.find_element_by_css_selector('#box-most-popular .link[title*=Purple]')
        return purple_duck

    def check_sticker(self, duck):
        if len(duck.find_elements_by_css_selector('.sticker')) == 1:
            return True
        else:
            return False

    def find_yellow_duck_in_campains(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector('#box-campaigns .link[title*=Yellow]')

    def get_href(self, web_element) -> str:
        wd = self.app.wd
        return web_element.get_attribute("href")

    def go_to_duck_page(self, web_element):
        wd = self.app.wd
        web_element.click()

    def check_duck_price(self, web_element) -> str:
        wd = self.app.wd
        duck_price = web_element.find_element_by_class_name('regular-price')
        return duck_price.get_attribute("textContent")

    def check_duck_name(self, web_element) -> str:
        wd = self.app.wd
        duck_name = web_element.find_element_by_class_name('name')
        return duck_name.get_attribute("textContent")


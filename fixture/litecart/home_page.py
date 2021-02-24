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

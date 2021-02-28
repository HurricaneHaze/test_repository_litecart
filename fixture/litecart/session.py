# *-* coding: utf-8 *-*


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, email, password):
        wd = self.app.wd
        wd.find_element_by_css_selector('input[name=email]').send_keys(email)
        wd.find_element_by_css_selector('input[name=password]').send_keys(password)
        wd.find_element_by_css_selector('button[name=login]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#box-account [href*=logout]').click()

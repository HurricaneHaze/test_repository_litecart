# *-* coding: utf-8 *-*


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login_admin_console(self, username='admin', password='admin'):
        wd = self.app.wd
        self.app.open_admin_console_page()
        wd.find_element_by_css_selector('[name=username]').send_keys(username)
        wd.find_element_by_css_selector('[name=password]').send_keys(password)
        wd.find_element_by_css_selector('[name=login]').click()

    def logout_admin_console(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('[title=Logout]').click()

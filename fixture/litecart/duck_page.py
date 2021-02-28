class DuckPageHelper:

    def __init__(self, app):
        self.app = app

    def check_duck_price(self) -> str:
        wd = self.app.wd
        duck_price = wd.find_element_by_class_name('regular-price')
        return duck_price.get_attribute("textContent")

    def check_duck_name(self) -> str:
        wd = self.app.wd
        duck_name = wd.find_element_by_css_selector('h1.title')
        return duck_name.get_attribute("textContent")

# *-* coding: utf-8 *-*

class MenuHelper:

    def __init__(self, app):
        self.app = app

    def check_vqumodes_items(self):
        wd = self.app.wd
        vqmodes = wd.find_elements_by_css_selector('#app-')
        vqmodes[16].click()
        wd.find_element_by_css_selector('#doc-vqmods').click()

    def check_users_items(self):
        wd = self.app.wd
        users = wd.find_elements_by_css_selector('#app-')
        users[15].click()

    def check_translations_items(self):
        wd = self.app.wd
        translations = wd.find_elements_by_css_selector('#app-')
        translations[14].click()
        wd.find_element_by_css_selector('#doc-search').click()
        wd.find_element_by_css_selector('#doc-scan').click()
        wd.find_element_by_css_selector('#doc-csv').click()

    def check_tax_items(self):
        wd = self.app.wd
        tax = wd.find_elements_by_css_selector('#app-')
        tax[13].click()
        wd.find_element_by_css_selector('#doc-tax_classes').click()
        wd.find_element_by_css_selector('#doc-tax_rates').click()

    def check_slides_items(self):
        wd = self.app.wd
        slides = wd.find_elements_by_css_selector('#app-')
        slides[12].click()

    def check_settings_items(self):
        wd = self.app.wd
        setting = wd.find_elements_by_css_selector('#app-')
        setting[11].click()
        wd.find_element_by_css_selector('#doc-store_info').click()
        wd.find_element_by_css_selector('#doc-defaults').click()
        wd.find_element_by_css_selector('#doc-general').click()
        wd.find_element_by_css_selector('#doc-listings').click()
        wd.find_element_by_css_selector('#doc-images').click()
        wd.find_element_by_css_selector('#doc-checkout').click()
        wd.find_element_by_css_selector('#doc-advanced').click()
        wd.find_element_by_css_selector('#doc-security').click()

    def check_reports_items(self):
        wd = self.app.wd
        reports = wd.find_elements_by_css_selector('#app-')
        reports[10].click()
        wd.find_element_by_css_selector('#doc-monthly_sales').click()
        wd.find_element_by_css_selector('#doc-most_sold_products').click()
        wd.find_element_by_css_selector('#doc-most_sold_products').click()

    def check_pages_items(self):
        wd = self.app.wd
        pages = wd.find_elements_by_css_selector('#app-')
        pages[9].click()

    def check_orders_items(self):
        wd = self.app.wd
        orders = wd.find_elements_by_css_selector('#app-')
        orders[8].click()
        wd.find_element_by_css_selector("#doc-orders").click()
        wd.find_element_by_css_selector('#doc-order_statuses').click()

    def check_modules_items(self):
        wd = self.app.wd
        modules = wd.find_elements_by_css_selector('#app-')
        modules[7].click()
        wd.find_element_by_css_selector('#doc-jobs').click()
        wd.find_element_by_css_selector('#doc-customer').click()
        wd.find_element_by_css_selector('#doc-shipping').click()
        wd.find_element_by_css_selector('#doc-payment').click()
        wd.find_element_by_css_selector('#doc-order_total').click()
        wd.find_element_by_css_selector('#doc-order_success').click()
        wd.find_element_by_css_selector('#doc-order_action').click()

    def check_language_items(self):
        wd = self.app.wd
        languages = wd.find_elements_by_css_selector('#app-')
        languages[6].click()
        wd.find_element_by_css_selector('#doc-languages').click()
        wd.find_element_by_css_selector('#doc-storage_encoding').click()

    def check_geo_zones_items(self):
        wd = self.app.wd
        geo_zones = wd.find_elements_by_css_selector('#app-')
        geo_zones[5].click()

    def check_customers_items(self):
        wd = self.app.wd
        customers = wd.find_elements_by_css_selector('#app-')
        customers[4].click()
        wd.find_element_by_css_selector('#doc-customers').click()
        wd.find_element_by_css_selector('#doc-csv').click()
        wd.find_element_by_css_selector('#doc-newsletter').click()

    def check_currencies_items(self):
        wd = self.app.wd
        currencies = wd.find_elements_by_css_selector('#app-')
        currencies[3].click()

    def check_countries_items(self):
        wd = self.app.wd
        countries = wd.find_elements_by_css_selector('#app-')
        countries[2].click()

    def check_catalog_items(self):
        wd = self.app.wd
        catalog = wd.find_elements_by_css_selector('#app-')
        catalog[1].click()
        wd.find_element_by_css_selector('#doc-catalog').click()
        wd.find_element_by_css_selector('#doc-product_groups').click()
        wd.find_element_by_css_selector('#doc-option_groups').click()
        wd.find_element_by_css_selector('#doc-manufacturers').click()
        wd.find_element_by_css_selector('#doc-suppliers').click()
        wd.find_element_by_css_selector('#doc-delivery_statuses').click()
        wd.find_element_by_css_selector('#doc-sold_out_statuses').click()
        wd.find_element_by_css_selector('#doc-quantity_units').click()
        wd.find_element_by_css_selector('#doc-csv').click()

    def check_appearance_items(self):
        wd = self.app.wd
        appearance = wd.find_elements_by_css_selector('#app-')
        appearance[0].click()
        wd.find_element_by_css_selector('#doc-template').click()
        wd.find_element_by_css_selector('#doc-logotype').click()

    def check_menu_bar(self):
        wd = self.app.wd
        self.check_appearance_items()
        self.check_catalog_items()
        self.check_countries_items()
        self.check_currencies_items()
        self.check_customers_items()
        self.check_geo_zones_items()
        self.check_language_items()
        self.check_modules_items()
        self.check_orders_items()
        self.check_pages_items()
        self.check_reports_items()
        self.check_settings_items()
        self.check_slides_items()
        self.check_tax_items()
        self.check_translations_items()
        self.check_users_items()
        self.check_vqumodes_items()


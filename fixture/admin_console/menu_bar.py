# *-* coding: utf-8 *-*

class MenuHelperAD:

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
        self.select_modules()
        self.open_jobs_page()
        self.open_customer_page()
        self.open_shipping_page()
        wd.find_element_by_css_selector('#doc-payment').click()
        wd.find_element_by_css_selector('#doc-order_total').click()
        wd.find_element_by_css_selector('#doc-order_success').click()
        wd.find_element_by_css_selector('#doc-order_action').click()

    def open_shipping_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-shipping').click()

    def open_customer_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-customer').click()

    def open_jobs_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-jobs').click()

    def select_modules(self):
        wd = self.app.wd
        modules = wd.find_elements_by_css_selector('#app-')
        modules[7].click()

    def check_language_items(self):
        wd = self.app.wd
        self.select_languages()
        self.open_language_page()
        self.open_storage_encoding_page()

    def open_storage_encoding_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-storage_encoding').click()

    def open_language_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-languages').click()

    def select_languages(self):
        wd = self.app.wd
        languages = wd.find_elements_by_css_selector('#app-')
        languages[6].click()

    def select_geozones(self):
        wd = self.app.wd
        geo_zones = wd.find_elements_by_css_selector('#app-')
        geo_zones[5].click()

    def check_customers_items(self):
        wd = self.app.wd
        self.select_customers()
        self.open_customers_page()
        self.open_customers_csv_page()
        self.open_newsletter_page()

    def open_newsletter_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-newsletter').click()

    def open_customers_csv_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-csv').click()

    def open_customers_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-customers').click()

    def select_customers(self):
        wd = self.app.wd
        customers = wd.find_elements_by_css_selector('#app-')
        customers[4].click()

    def select_currencies(self):
        wd = self.app.wd
        currencies = wd.find_elements_by_css_selector('#app-')
        currencies[3].click()

    def select_countries(self):
        wd = self.app.wd
        countries = wd.find_elements_by_css_selector('#app-')
        countries[2].click()

    def check_catalog_items(self):
        wd = self.app.wd
        self.select_catalog()
        self.open_catalog_page()
        self.open_product_groups_page()
        self.open_option_groups_page()
        self.open_manufacturers_page()
        self.open_suppliers_page()
        self.open_delivery_statuses_page()
        self.open_sold_out_statuses_page()
        self.open_quantity_units_page()
        self.open_csv_page()

    def open_csv_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-csv').click()

    def open_quantity_units_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-quantity_units').click()

    def open_sold_out_statuses_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-sold_out_statuses').click()

    def open_delivery_statuses_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-delivery_statuses').click()

    def open_suppliers_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-suppliers').click()

    def open_manufacturers_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-manufacturers').click()

    def open_option_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-option_groups').click()

    def open_product_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-product_groups').click()

    def open_catalog_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-catalog').click()

    def select_catalog(self):
        wd = self.app.wd
        catalog = wd.find_elements_by_css_selector('#app-')
        catalog[1].click()

    def check_appearance_items(self):
        wd = self.app.wd
        self.select_appearance()
        self.open_template_page()
        self.open_logotype_page()

    def open_logotype_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-logotype').click()

    def open_template_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#doc-template').click()

    def select_appearance(self):
        wd = self.app.wd
        appearance = wd.find_elements_by_css_selector('#app-')
        appearance[0].click()

    def get_page_header(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector('h1').text

    def check_menu_bar(self):
        wd = self.app.wd
        menu_bar_items = len(wd.find_elements_by_css_selector('#app-'))
        for i in range(menu_bar_items):
            wd.find_elements_by_css_selector('#app-')[i].click()
            submenu = wd.find_elements_by_css_selector('#app-')[i]
            items = len(submenu.find_elements_by_css_selector('li'))
            for j in range(items):
                submenu = wd.find_elements_by_css_selector('#app-')[i]
                submenu.find_elements_by_css_selector('li')[j].click()
                if not self.get_page_header():
                    return False
        return True

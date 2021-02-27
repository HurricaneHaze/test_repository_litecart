# *-* coding: utf-8 *-*

class CountriesHelper:

    def __init__(self, app):
        self.app = app

    def get_countries_list(self) -> list:
        wd = self.app.wd
        self.app.ad_menu.select_countries()
        countries = []
        rows = len(wd.find_elements_by_css_selector('.row'))
        for i in range(rows):
            country = wd.find_elements_by_css_selector('.row')[i]
            country_name = country.find_element_by_css_selector('[href]').get_attribute('textContent')
            countries.append(country_name)
        return countries

    def check_zones(self) -> list:
        wd = self.app.wd
        countries_zones_indexes_list = []
        self.app.ad_menu.select_countries()
        rows = len(wd.find_elements_by_css_selector('.row'))
        for i in range(rows):
            country = wd.find_elements_by_css_selector('.row')[i]
            country_zones = country.find_elements_by_css_selector('td')[5].get_attribute('textContent')
            if int(country_zones) > 0:
                countries_zones_indexes_list.append(i)
        return countries_zones_indexes_list

    def get_country_zones_list(self) -> list:
        wd = self.app.wd
        zones = []
        table = wd.find_element_by_css_selector('#table-zones')
        tr = table.find_elements_by_css_selector('tr')
        tr = tr[1:-1]
        rows = len(tr)
        for i in range(rows):
            td = tr[i].find_elements_by_css_selector('td')
            zones.append(td[2].get_attribute('textContent'))
        return zones

    def go_to_country_zone(self, index):
        wd = self.app.wd
        if not wd.current_url.endswith("countries"):
            self.app.ad_menu.select_countries()
        country = wd.find_elements_by_css_selector('.row')[index]
        country.find_element_by_css_selector('[href]').click()

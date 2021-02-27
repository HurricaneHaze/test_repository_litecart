# *-* coding: utf-8 *-*
import pytest


def test_menu_bar_(ad_app):
    assert ad_app.ad_menu.check_menu_bar()


def test_countries_sorted(ad_app):
    countries = ad_app.ad_countries.get_countries_list()
    sorted_countries = sorted(countries)
    assert countries == sorted_countries


def test_geozones(ad_app):
    indexes_list = ad_app.ad_countries.check_zones()
    for country in indexes_list:
        ad_app.ad_countries.go_to_country_zone(country)
        zones = ad_app.ad_countries.get_country_zones_list()
        assert zones == sorted(zones)
        ad_app.open_previous_page()


if __name__ == '__main__':
    pytest.main()

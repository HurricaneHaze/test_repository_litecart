# *-* coding: utf-8 *-*
import pytest


def test_menu_bar(ad_app):
    ad_app.admin_console_menu.select_appearance()
    ad_app.admin_console_menu.open_template_page()
    assert ad_app.admin_console_menu.get_page_header()

    ad_app.admin_console_menu.open_logotype_page()
    assert ad_app.admin_console_menu.get_page_header()

    ad_app.admin_console_menu.select_catalog()
    ad_app.admin_console_menu.open_catalog_page()
    assert ad_app.admin_console_menu.get_page_header()

    ad_app.admin_console_menu.open_product_groups_page()
    assert ad_app.admin_console_menu.get_page_header()

    ad_app.admin_console_menu.open_option_groups_page()
    assert ad_app.admin_console_menu.get_page_header()

    ad_app.admin_console_menu.open_manufacturers_page()
    assert ad_app.admin_console_menu.get_page_header()

    ad_app.admin_console_menu.open_suppliers_page()
    assert ad_app.admin_console_menu.get_page_header()

    ad_app.admin_console_menu.open_delivery_statuses_page()
    assert ad_app.admin_console_menu.get_page_header()

    ad_app.admin_console_menu.open_sold_out_statuses_page()
    assert ad_app.admin_console_menu.get_page_header()

    ad_app.admin_console_menu.open_quantity_units_page()
    assert ad_app.admin_console_menu.get_page_header()

    ad_app.admin_console_menu.open_csv_page()
    assert ad_app.admin_console_menu.get_page_header()

    ad_app.admin_console_menu.open_customers_page()
    assert ad_app.admin_console_menu.get_page_header()


def test_countries_sorted(ad_app):
    pass


def test_geozones(ad_app):
    pass


if __name__ == '__main__':
    pytest.main()

# *-* coding: utf-8 *-*
import pytest


def test_menu_bar(admin_console_app):
    admin_console_app.admin_console_menu.select_appearance()
    admin_console_app.admin_console_menu.open_template_page()
    assert admin_console_app.admin_console_menu.get_page_header()
    admin_console_app.admin_console_menu.open_logotype_page()
    assert admin_console_app.admin_console_menu.get_page_header()
    admin_console_app.admin_console_menu.select_catalog()
    admin_console_app.admin_console_menu.open_catalog_page()
    assert admin_console_app.admin_console_menu.get_page_header()
    admin_console_app.admin_console_menu.open_product_groups_page()
    assert admin_console_app.admin_console_menu.get_page_header()
    admin_console_app.admin_console_menu.open_option_groups_page()
    assert admin_console_app.admin_console_menu.get_page_header()
    admin_console_app.admin_console_menu.open_manufacturers_page()
    assert admin_console_app.admin_console_menu.get_page_header()
    admin_console_app.admin_console_menu.open_suppliers_page()
    assert admin_console_app.admin_console_menu.get_page_header()
    admin_console_app.admin_console_menu.open_delivery_statuses_page()
    assert admin_console_app.admin_console_menu.get_page_header()
    admin_console_app.admin_console_menu.open_sold_out_statuses_page()
    assert admin_console_app.admin_console_menu.get_page_header()
    admin_console_app.admin_console_menu.open_quantity_units_page()
    assert admin_console_app.admin_console_menu.get_page_header()
    admin_console_app.admin_console_menu.open_csv_page()
    assert admin_console_app.admin_console_menu.get_page_header()
    admin_console_app.admin_console_menu.open_customers_page()
    assert admin_console_app.admin_console_menu.get_page_header()


if __name__ == '__main__':
    pytest.main()

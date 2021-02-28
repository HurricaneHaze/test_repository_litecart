# *-* coding: utf-8 *-*
import time

import pytest
from model.model_litecart.customer import Customer


def test_login(app):
    app.home_page.register_new_customer(
        Customer(firstname='firstname', lastname='lastname', address1='address1', postcode='111111', city='city',
                 phone='123', email='email@mail.com', password='password', confirmed_password='password'))
    app.session.logout()
    app.session.login(email='1@1.1', password='1')
    app.session.logout()


def test_stickers(app):
    check_duck_sticker = app.home_page.check_sticker
    assert check_duck_sticker(app.home_page.find_red_duck_in_most_popular()) == 1
    assert check_duck_sticker(app.home_page.find_green_duck_in_most_popular()) == 1
    assert check_duck_sticker(app.home_page.find_blue_duck_in_most_popular()) == 1
    assert check_duck_sticker(app.home_page.find_yellow_duck_in_most_popular()) == 1


def test_yellow_duck_page(app):
    yellow_duck = app.home_page.find_yellow_duck_in_campains()
    duck_page = app.home_page.get_href(yellow_duck)
    app.home_page.go_to_duck_page(yellow_duck)
    new_duck_page = app.get_current_url()
    assert duck_page == new_duck_page


def test_yellow_duck_name(app):
    yellow_duck = app.home_page.find_yellow_duck_in_campains()
    duck_text = app.home_page.check_duck_name(yellow_duck)
    app.home_page.go_to_duck_page(yellow_duck)
    new_duck_text = app.duck_page.check_duck_name()
    assert duck_text == new_duck_text


def test_yellow_duck_price(app):
    yellow_duck = app.home_page.find_yellow_duck_in_campains()
    duck_price = app.home_page.check_duck_price(yellow_duck)
    app.home_page.go_to_duck_page(yellow_duck)
    new_duck_price = app.duck_page.check_duck_price()
    assert duck_price == new_duck_price


if __name__ == '__main__':
    pytest.main()

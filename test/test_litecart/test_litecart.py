# *-* coding: utf-8 *-*
import pytest


def test_stickers(litecart_app):
    check_duck_sticker = litecart_app.home_page.check_sticker
    assert check_duck_sticker(litecart_app.home_page.find_purple_duck_in_most_popular())
    assert check_duck_sticker(litecart_app.home_page.find_red_duck_in_most_popular())
    assert check_duck_sticker(litecart_app.home_page.find_green_duck_in_most_popular())
    assert check_duck_sticker(litecart_app.home_page.find_blue_duck_in_most_popular())
    assert check_duck_sticker(litecart_app.home_page.find_yellow_duck_in_most_popular())


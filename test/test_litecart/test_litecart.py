# *-* coding: utf-8 *-*
import pytest


def test_stickers(litecart_app):
    assert litecart_app.home_page.check_sticker(litecart_app.home_page.find_purple_duck_in_most_popular())

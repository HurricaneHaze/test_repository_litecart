# *-* coding: utf-8 *-*
import pytest
from fixture.application import Application


@pytest.fixture()
def admin_console_app(request):
    fixture = Application()
    fixture.admin_console_session.login_admin_console(username='admin', password='admin')

    def fin():
        fixture.admin_console_session.logout_admin_console()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


@pytest.fixture()
def litecart_app(request):
    fixture = Application()
    fixture.open_home_page()
    request.addfinalizer(fixture.destroy)
    return fixture

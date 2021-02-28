# *-* coding: utf-8 *-*
import pytest
from fixture.application import Application

fixture = None


@pytest.fixture()
def ad_app(request):
    global fixture
    if fixture is None or not fixture.is_valid():
        fixture = Application()
        fixture.ad_session.login_admin_console(username='admin', password='admin')
    return fixture


@pytest.fixture()
def app(request):
    global fixture
    if fixture is None or not fixture.is_valid():
        fixture = Application()
    fixture.open_home_page()
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        # fixture.ad_session.logout_admin_console()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture

# *-* coding: utf-8 *-*
import pytest
from fixture_admin_console.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

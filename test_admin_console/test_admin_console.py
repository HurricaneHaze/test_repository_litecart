# *-* coding: utf-8 *-*
import pytest


def test_menu_bar(app):
    app.admin_console_session.login_admin_console(username='admin', password='admin')
    app.admin_console_menu.check_menu_bar()
    app.admin_console_session.logout_admin_console()


if __name__ == '__main__':
    pytest.main()

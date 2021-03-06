# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(firstname="First", lastname="Last", address="yes", home_phone="no"))
    app.session.logout()

def test_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add_new(Contact(firstname="", lastname="", address="", home_phone=""))
    app.session.logout()

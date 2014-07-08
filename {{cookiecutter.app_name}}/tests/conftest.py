# -*- coding: utf-8 -*-
"""
    tests.conftest
    {{ "~" * "tests.conftest"|count }}

    :author: {{ cookiecutter.author }}
    :copyright: (c) {{ cookiecutter.copyright }}
    :license: {{ cookiecutter.license }}, see LICENSE for more details.
"""
import pytest
from webtest import TestApp

from {{cookiecutter.app_name}}.frontend import create_app
from {{cookiecutter.app_name}}.framework.sql import db as _db

from . import settings as test_settings
from .factories import UserFactory

@pytest.yield_fixture(scope='function')
def app():
    _app = create_app(test_settings)
    ctx = _app.test_request_context()
    ctx.push()
    yield _app
    ctx.pop()

@pytest.fixture(scope='session')
def testapp(app):
    """A Webtest app."""
    return TestApp(app)

@pytest.yield_fixture(scope='function')
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()
    yield _db
    _db.drop_all()

@pytest.fixture
def user(db):
    return UserFactory()

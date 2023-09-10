import pytest

from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application(base_url="https://reqres.in/")
    fixture.open_site()
    request.addfinalizer(fixture.destroy)
    return fixture

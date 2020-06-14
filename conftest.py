import pytest
from fixture.application import Application


@pytest.fixture(scope='session')
def app(request):
    fixture = Application('C:\\Users\\79111\\Desktop\\python_training\\Приложение GUI\\AddressBook.exe')
    request.addfinalizer(fixture.destroy)
    return fixture

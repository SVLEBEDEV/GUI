import pytest
from fixture.application import Application
from comtypes.client import CreateObject
import os
from model.group import Group


@pytest.fixture(scope='session')
def app(request):
    fixture = Application('C:\\Users\\79111\\Desktop\\python_training\\Приложение GUI\\AddressBook.exe')
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith('excel_'):
            TestData = load_from_excel()
            metafunc.parametrize(fixture, TestData, ids=[str(x) for x in TestData])


def load_from_excel():
    project_dir = os.path.dirname(os.path.realpath(__file__)) + '\\groups.xlsx'
    xl = CreateObject("Excel.Application")
    xl.Visible = 0
    wb = xl.Workbooks.open(project_dir)
    i = 1
    list_group = []
    while xl.Range["A%s" % i].Value() is not None:
        list_group.append(Group(name=xl.Range["A%s" % i].Value()))
        i += 1
    xl.Quit()
    return list_group

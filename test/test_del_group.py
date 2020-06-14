import random
from time import sleep


def test_del_group(app):
    name = 'test'
    old_list = app.groups.get_group_list()
    if len(old_list) == 0:
        app.groups.add_new_group(name)
        old_list = app.groups.get_group_list()
    elif old_list.count(name) == 0:
        app.groups.add_new_group(name)
        old_list = app.groups.get_group_list()
        sleep(5)
    app.groups.del_first_group_with_name(name)
    new_list = app.groups.get_group_list()
    old_list.remove(name)
    assert sorted(old_list) == sorted(new_list)
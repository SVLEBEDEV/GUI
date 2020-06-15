from fixture.group import Group


def test_del_group(app):
    group = Group(name='test1')
    old_list = app.groups.get_group_list()
    if len(old_list) == 0:
        app.groups.add_new_group(group)
        old_list = app.groups.get_group_list()
    elif old_list.count(group) == 0:
        app.groups.add_new_group(group)
        old_list = app.groups.get_group_list()
    app.groups.del_first_group_with_name(group)
    new_list = app.groups.get_group_list()
    old_list.remove(group)
    assert sorted(old_list, key=Group.sorted_by_name) == sorted(new_list, key=Group.sorted_by_name)
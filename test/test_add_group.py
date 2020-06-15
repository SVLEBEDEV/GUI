from fixture.group import Group

def test_add_group(app, excel_testdata):
    group = excel_testdata
    old_list = app.groups.get_group_list()
    app.groups.add_new_group(group)
    new_list = app.groups.get_group_list()
    old_list.append(group)
    assert sorted(old_list, key=Group.sorted_by_name) == sorted(new_list, key=Group.sorted_by_name)
from barancev_programmirovanie.model.group import Group
import time


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name='first', header='second', footer='thirth'))
    new_groups = app.group.get_group_list()

    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name='', header='', footer=''))
    new_groups = app.group.get_group_list()

    assert len(old_groups) + 1 == len(new_groups)


if __name__ == "__main__":
    unittest.main()

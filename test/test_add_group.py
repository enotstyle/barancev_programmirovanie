from barancev_programmirovanie.model.group import Group
import time


def test_add_group(app):
    app.group.create(Group(name='first', header='second', footer='thirth'))


def test_add_empty_group(app):
    app.group.create(Group(name='', header='', footer=''))


if __name__ == "__main__":
    unittest.main()

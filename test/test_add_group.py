from barancev_programmirovanie.model.group import Group
import time


def test_add_group(app):
    app.session.login(username='admin', password='secret')
    app.group.create(Group(name='first', header='second', footer='thirth'))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username='admin', password='secret')
    app.group.create(Group(name='', header='', footer=''))
    app.session.logout()


if __name__ == "__main__":
    unittest.main()

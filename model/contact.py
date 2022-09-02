from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, id=None, homephone=None, mobilephone=None, workphone=None,
                 secondaryphone=None, all_phones_from_homepage=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def __repr__(self):
        return f"{self.id, self.firstname, self.lastname}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname

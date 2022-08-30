from selenium import webdriver
from selenium.webdriver.common.by import By
from barancev_programmirovanie.model.group import Group
from barancev_programmirovanie.fixture.session import SessionHelper
from barancev_programmirovanie.fixture.group import GroupHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def destroy(self):
        self.wd.quit()

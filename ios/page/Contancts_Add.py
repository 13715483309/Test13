from time import sleep

from ios.page.Base_Page import Base_Page


class Contancts_Add(Base_Page):

    def conadd(self):
        self.contacts_find_by_xpath('//*[@name="Add"]').click()
        self.contacts_find_by_xpath('//*[@name="First name"]').send_keys('zhang')
        lastname = self.contacts_find_by_xpath('//*[@name="Last name"]')
        lastname.send_keys('san')
        self.contacts_find_by_xpath('//*[@name="Company"]').send_keys('beijing')
        # self.contacts_find_by_ios_predicate('name == "Add"').click()
        self.contacts_find_by_xpath('//*[@name="Add"]').click()

if __name__ == '__main__':
    obj = Contancts_Add()
    obj.conadd()

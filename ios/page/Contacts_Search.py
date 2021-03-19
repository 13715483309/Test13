import yaml

from ios.page.Base_Page import Base_Page


class Contancts_Search(Base_Page):
    with open('/Users/chenjinfei/project/pythonProject/ios/data/contacts_search.yml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    ele_search = data['search']
    ele_name = data['name']
    ele_edit = data['edit']
    ele_cancel = data['cancel']
    ele_cancel2 = data['cancel2']

    def search(self):
        search = self.contacts_find_by_xpath(self.ele_search)
        search.click()
        search.send_keys('John')
        name = self.contacts_find_by_xpath(self.ele_name)
        name.click()
        search = self.contacts_find_by_xpath(self.ele_search)
        search.click()
        name = self.contacts_find_by_xpath(self.ele_name)
        name.click()
        edit = self.contacts_find_by_xpath(self.ele_edit)
        edit.click()
        cancel = self.contacts_find_by_xpath(self.ele_cancel)
        cancel.click()
        search = self.contacts_find_by_xpath(self.ele_search)
        search.click()
        cancel2 = self.contacts_find_by_ios_predicate(self.ele_cancel2)
        cancel2.click()


if __name__ == '__main__':
    obj = Contancts_Search()
    obj.search()
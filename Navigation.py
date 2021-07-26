# pip install Selenium
# download chromeDriver

from selenium import webdriver
import yaml
import datetime as dt
from collections import namedtuple
from Brain import Brain

brain = Brain()

class Navigation:
    def __init__(self):
        self.conf = yaml.load(open('loginDetails.yml'), Loader=yaml.FullLoader)
        self.driver = webdriver.Chrome()

    def login(self):
        url = "https://www.golf.co.nz/my-golf-login"
        usernameId = "ctl43_tbMembershipNumber"
        passwordId = "ctl43_tbPassword"
        submit_buttonId = "ctl43_btnLogin"

        username = self.conf['golf_user']['id']
        password = self.conf['golf_user']['password']

        self.driver.get(url)
        self.driver.find_element_by_id(usernameId).send_keys(username)
        self.driver.find_element_by_id(passwordId).send_keys(password)
        self.driver.find_element_by_id(submit_buttonId).click()

    def clickLookup(self, description = None, element = None):
        element_lookup = {
            "book a tee": "//a[@class='site-header__action action--book-tee']",
        }
        if element == None:
            try:
                self.driver.find_element_by_xpath(element_lookup[description]).click()
            except Exception as e:
                print(e)
        else:
            element.click()

        # self.driver.find_elements_by_class_name("available")[0].click()
        #
        # self.driver.find_elements_by_class_name("book_here_link")[0].click()
        #
        # self.driver.find_element_by_id("MainContent_ContinueButton").click()

    def click(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e)

    def getElement(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            print(e)

    def getAvailableDateElements(self):
        elements = self.driver.find_elements_by_xpath("//td[@class='available']")
        return elements

    def getBookTimes(self):
        rows = self.driver.find_elements_by_xpath("//table[@id='MainContent_TimeslotsTable']//tbody//tr")

        book_times = {}
        BookingTime = namedtuple('BookingTime', ['time', 'tee', 'slot1', 'slot2', 'slot3', 'slot4', 'slots_available'])
        for i in range(1, len(rows) + 1):
            row = self.driver.find_elements_by_xpath(
                "//table[@id='MainContent_TimeslotsTable']//tbody//tr[{}]//td".format(i))
            time = brain.stringToTime(row[0].text)
            # Get num slots available
            num_slots_available = brain.getNumSlotsAvailable(row)
            bt = BookingTime(time, int(row[1].text), row[2], row[3], row[4], row[5], num_slots_available)
            book_times[time] = bt
        return book_times

    def exit(self):
        self.driver.quit()
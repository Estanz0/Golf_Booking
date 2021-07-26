from Navigation import Navigation
import time

class Handicap():
    def __int__(self):
        pass

    def getHandicap(self):
        nav = Navigation()
        nav.login()

        hcap_index_xpath = "//div[@class='handicap-index']//span"
        hcap_element = nav.getElement(hcap_index_xpath)
        return hcap_element.text


if __name__ == "__main__":
    handicap = Handicap()
    handicap.getHandicap()
    time.sleep(500)



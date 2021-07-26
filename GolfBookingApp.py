from Navigation import Navigation
from Brain import Brain

import time

class GolfBookingApp:
    def __init__(self):
        pass

    def main(self):
        input_date_time = "23 1300"
        nav = Navigation()
        brain = Brain()
        nav.login()
        nav.clickLookup("book a tee")

        input_date, input_time = brain.inputToDatetime(input_date_time)

        available_date_elements = nav.getAvailableDateElements()
        available_dates = brain.elementsToDates(available_date_elements)

        ind = brain.checkDateAvailable(input_date, available_dates)
        if ind < 0:
            print("None available")
        else:
            print("Available")
            nav.clickLookup(element=available_date_elements[ind])

        # Find times
        book_times = nav.getBookTimes()

        # Get closest time
        seconds_diff, closest_tee_time = brain.findClosestTeeTime(book_times, input_time)

        print(seconds_diff)
        print(book_times[closest_tee_time].time)
        print(book_times[closest_tee_time].slots_available)

        time.sleep(50)

        nav.exit()

if __name__ == "__main__":
    gba = GolfBookingApp()
    gba.main()

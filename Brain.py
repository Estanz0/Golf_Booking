import datetime as dt

class Brain:
    def __init__(self):
        pass

    def inputToDatetime(self, input):
        date = input.split(" ")[0]
        time = input.split(" ")[1]
        today = dt.datetime.today()
        input_date = dt.date(today.year, today.month, int(date))
        input_time = dt.time(int(time[:2]), int(time[2:]))
        return input_date, input_time

    def stringToTime(self, input):
        sep = ':' if ':' in input else ' '
        hour = input.split(sep)[0]
        minutes = input.split(sep)[1]
        t = dt.time(int(hour), int(minutes))
        return t

    def findClosestTeeTime(self, tee_times, input_time):
        lowest_tdelta = 10000000 # Max time
        closest_tee_time = None
        # Convert to datetime
        input_datetime = dt.datetime.combine(dt.date.today(), input_time)

        for tee_time in tee_times:
            # Convert to datetime
            tee_datetime = dt.datetime.combine(dt.date.today(), tee_time)
            tdelta = abs(tee_datetime - input_datetime) if tee_datetime > input_datetime else abs(input_datetime - tee_datetime)
            if (tdelta.seconds < lowest_tdelta) & (tee_times[tee_time].slots_available == 4):
                lowest_tdelta = tdelta.seconds
                closest_tee_time = tee_time

        return lowest_tdelta, closest_tee_time

    def getNumSlotsAvailable(self, row):
        num_slots_available = 0
        for i in range(2, 6):
            if 'Available' in row[i].text:
                num_slots_available += 1
        return num_slots_available


    def elementsToDates(self, elements):
        onclick_strings = [element.get_attribute('onclick') for element in elements]
        dates_strings = [onclick_string.split("'")[1] for onclick_string in onclick_strings]
        dates_date = [dt.datetime.strptime(date, '%Y-%m-%d').date() for date in dates_strings]
        return dates_date

    def checkDateAvailable(self, input_date, available_dates):
        ind = -1
        if input_date in available_dates:
            ind = available_dates.index(input_date)
        return ind


import requests
import datetime
import time
from pprint import pprint

class Stackoverflow:

    def get_questions(self, fy, fm, fd, ty, tm, td):
        url = "https://api.stackexchange.com/2.3/questions"
        offset = datetime.timedelta(hours=3)
        datetime.timezone(offset, name='МСК')
        datetime_from = datetime.date(fy, fm, fd)
        datetime_to = datetime.date(ty, tm, td)
        params = {"fromdate": str(int(time.mktime(datetime_from.timetuple()))), "todate": str(int(time.mktime(datetime_to.timetuple()))), "order" : "desc", "sort" : "activity", "tagged" : "python", "site" : "stackoverflow"}
        response = requests.get(url, params=params)
        return response.json()

if __name__ == '__main__':
    stackoverflow = Stackoverflow()
    pprint(stackoverflow.get_questions(2022, 5, 23, 2022, 5, 25))

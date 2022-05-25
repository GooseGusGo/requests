import requests
import datetime
import time

class Stackoverflow:

    def get_questions(self, fy, fm, fd, ty, tm, td):
        url = "https://api.stackexchange.com/docs/questions"
        offset = datetime.timedelta(hours=3)
        datetime.timezone(offset, name='МСК')
        datetime_from = datetime.date(fy, fm, fd)
        datetime_to = datetime.date(ty, tm, td)
        params = {"fromdate": str(int(time.mktime(datetime_from.timetuple()))), "todate": str(int(time.mktime(datetime_to.timetuple()))), "order" : "desc", "sort" : "activity", "tagged" : "Python", "site" : "stackoverflow"}
        print(params)
        response = requests.get(url, params=params)
        print(response)
        return response.json()

if __name__ == '__main__':
    stackoverflow = Stackoverflow()
    print(stackoverflow.get_questions(2022, 5, 23, 2022, 5, 25))


# В общем схема рабочая, но косяк в URL как мне кажется, нужен совет как довести это до ума.

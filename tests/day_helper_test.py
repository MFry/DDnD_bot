from utils.day_helper import weekday_to_datetime_object

weekdays = ["Monday", "Tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def test_ordinary_weekday_conversion():
    for i, test_weekday in enumerate(weekdays):
        date_object = weekday_to_datetime_object(test_weekday)
        print('day', test_weekday, date_object.weekday())
        assert date_object.strftime("%A").lower() == weekdays[i].lower()

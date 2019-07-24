from datetime import datetime, timedelta

WEEKDAYS_TO_NUMERAL = {
    'mon': 0,
    'tue': 1,
    'wed': 2,
    'thu': 3,
    'fri': 4,
    'sat': 5,
    'sun': 6
}


def weekday_to_datetime_object(weekday):
    """

    :param weekday:
    :type weekday: str
    :return:
    :rtype datetime
    """
    # clean and format
    formatted_weekday = weekday[:3].lower()
    if formatted_weekday not in WEEKDAYS_TO_NUMERAL:
        raise Exception(f'Malformed weekday ${weekday} cannot be converted to Monday - Sunday format.')
    return datetime.now() - timedelta(days=-datetime.now().weekday()) + timedelta(
        days=WEEKDAYS_TO_NUMERAL[formatted_weekday])

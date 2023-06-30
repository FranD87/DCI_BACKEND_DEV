import datetime

def discount_calculator(value: float, due_data: datetime.date, discount: float, days: int) -> float:
    '''

    :param value: price of product
    :param due_data: date till what discount valid
    :param discount: discount as float 20% = 0.2
    :param days: total days of promotion
    :return:
    float: price with or without discount
    '''
    # check timedelta for last day of discount till today
    diff = due_data - datetime.date.today()
    # We are checking that we fit in time when discount will work (due_date - days -> days for how long it should work)
    print(datetime.timedelta(days=days))
    print(datetime.timedelta())
    print(diff)
    if datetime.timedelta() <= diff < datetime.timedelta(days=days):
        # If today fit discount terms apply discount
        return value * (1.0 - discount)
    else:
        # else do not apply discount
        return value

print(discount_calculator(
                value=100,
                due_data=datetime.date(year=2023, month=1, day=28),
                days=10,
                discount=0.2
            ))

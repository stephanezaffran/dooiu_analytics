from datetime import datetime
import datetime as dt
from itertools import groupby
from enum import Enum
import math


class LapsTime(Enum):
    year = 1
    month = 2
    day = 3


class sales_or_calltime(Enum):
    sales = 1
    calltime = 2


def communication_time(list_conversations):
    return [
        ['date', 'id'],
        *[conversation.get_clients() for conversation in list_conversations]
    ]


def get_communication_by_day(list_conversations):
    current_year = datetime.now().year
    current_month = datetime.now().month
    data_list = communication_time(list_conversations)

    filtered_data = [item for item in data_list[1:] if (int(item[0][:4]) >= current_year - 9)]
    # print(f"get_communication_by_day filtered_data: {filtered_data}")
    date_count = {}

    for item in filtered_data:
        date = item[0]
        if date in date_count:
            date_count[date] += 1
        else:
            date_count[date] = 1

    return [['date', 'count'], *[[date, count] for date, count in date_count.items()]]


def get_communication_by_date(list_conversations, attr_name):
    data_list = communication_time(list_conversations)
    data_list = [(datetime.strptime(date_str, '%Y-%m-%d'), value) for date_str, value in data_list[1:]]
    # print(f"data_list: {data_list}")
    current_year = datetime.now().year
    current_month = datetime.now().month

    if attr_name == 'month':
        filtered_data = [item for item in data_list if
                         (item[0].year == current_year - 2 and item[0].month >= current_month) or
                         item[0].year > current_year - 2]

        # print(f"filtered_data: {filtered_data}")

    elif attr_name == 'year':
        filtered_data = [item for item in data_list if (item[0].year >= current_year - 9)]

    data_totals = {}

    for item in filtered_data:
        formatted_data = item[0].strftime('%Y-%m') if attr_name == LapsTime.month.name else item[0].strftime('%Y')
        value = getattr(item[0], attr_name)
        data_totals.setdefault(formatted_data, 0)
        data_totals[formatted_data] += 1

    grouped_data = [['date', 'count']]
    for value, count in data_totals.items():
        grouped_data.append([value, count])

    # grouped_data = []
    # for key, group in groupby(filtered_data, (lambda x: getattr(x[0], attr_name))):
    #     data = list(group)
    #     data_total = sum(1 for item in data)
    #     formatted_data = data[0][0].strftime('%Y-%m') if attr_name == LapsTime.month.name else data[0][0].strftime('%Y')
    #     grouped_data.append([formatted_data, data_total])

    return grouped_data


def get_number_of_clients(list_conversations):
    # print(f"list_conversations: {list_conversations}")
    # get_number_of_news_clients_by_month(list_conversations, LapsTime.month.name)

    unique_list = []

    # Iterate through the list_objects
    for conversation in list_conversations:
        if conversation.seeker_id not in unique_list:
            # If userId is not in the dictionary, add the object
            unique_list.append(conversation.seeker_id)
    return len(unique_list)


def get_number_of_news_clients_by_month(list_conversations, attr_name):
    get_actual_week_sales_per_day_hour(list_conversations, sales_or_calltime.sales.name)
    # sorted_conversations = sorted(list_conversations, key=lambda x: x.start_time)
    unique_conversation_seeker = {}
    for conversation in list_conversations:
        if conversation.seeker_id not in unique_conversation_seeker or conversation.start_time < \
                unique_conversation_seeker[conversation.seeker_id]:
            unique_conversation_seeker[conversation.seeker_id] = conversation.start_time

    filtered_data = [(buying_date, client_id) for client_id, buying_date in unique_conversation_seeker.items()]
    print(f"unique_conversation_seeker: {filtered_data}")

    data_totals = {}
    for item in filtered_data:
        formatted_data = item[0].strftime('%Y-%m') if attr_name == LapsTime.month.name else item[0].strftime('%Y')
        value = getattr(item[0], attr_name)
        data_totals.setdefault(formatted_data, 0)
        data_totals[formatted_data] += 1

    grouped_data = [['date', 'count']]
    for value, count in data_totals.items():
        grouped_data.append([value, count])

    # grouped_data = []
    # for key, group in groupby(filtered_data, (lambda x: getattr(x[0], attr_name))):
    #     data = list(group)
    #     data_total = sum(1 for item in data)
    #     formatted_data = data[0][0].strftime('%Y-%m') if attr_name == 'month' else data[0][0].strftime('%Y')
    #     grouped_data.append([formatted_data, data_total])
    #
    # print([['date', 'count'], *grouped_data])
    #

    return [['date', 'count'], *grouped_data]


def get_actual_week_sales_per_day_hour(list_conversations, attr_name):
    # print(attr_name)
    buffer = None
    data = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ];
    current_datetime = datetime.now() - dt.timedelta(days=datetime.now().weekday() + 1)
    start_of_week = current_datetime - dt.timedelta(days=current_datetime.weekday() + 1)
    print(f"current_datetime: {current_datetime} -- start_of_week: {(start_of_week.weekday() + 1) % 7}")

    filtered_list = [obj for obj in list_conversations if
                     start_of_week <= obj.start_time <= current_datetime]
    print(f"actual_week_patient_per_day_hour: {filtered_list}")
    for item in filtered_list:
        start_day = (item.start_time.weekday() + 1) % 7
        start_hour = item.start_time.hour
        start_seconds = (item.start_time.minute) * 60 + item.start_time.second
        second_per_hour = 3600
        rest_second = second_per_hour - start_seconds
        paid_seconds = item.paid_seconds
        free_seconds = item.free_seconds
        total_paid = item.total_paid
        fee_amount = item.fee_amount
        buffer = None
        # print(f"day_hour_second: - item.start_time {item.start_time} - day {start_day} -  hour {start_hour} -  seconds {start_seconds} - free_seconds {free_seconds} - paid_seconds {paid_seconds}")
        if attr_name == sales_or_calltime.sales.name:
            if rest_second >= free_seconds:
                rest_second = rest_second - free_seconds
            else:
                start_hour += 1
                rest_second = 3600 - (free_seconds - rest_second)

            buffer = update_actual_week_data_list(data, start_hour, start_day, paid_seconds, rest_second)
        else:
            call_seconds = paid_seconds + free_seconds
            data = update_actual_week_data_list(data, start_hour, start_day, call_seconds, rest_second)
    if buffer != None:
        data = [[item * float(fee_amount) for item in sublist] for sublist in buffer]
        print(float(fee_amount) * 2)

    # print(f"sales: {fee_amount} - {data}")
    return data


def update_actual_week_data_list(data, start_hour, start_day, call_seconds, rest_second):
    while (call_seconds > 0):
        if call_seconds >= rest_second:
            data[start_hour][start_day] += math.ceil((rest_second / 60))
            # print(f"call_seconds: {rest_second}")
            start_hour += 1
            call_seconds = call_seconds - rest_second
            rest_second = 3600

        elif call_seconds < rest_second:
            data[start_hour][start_day] += math.ceil((call_seconds / 60))
            # print(f"call_seconds: {call_seconds}")
            call_seconds = 0
    return data


def get_clients_per_region(list_conversations):
    filtered_data = {}
    data_totals = {}
    for item in list_conversations:
        if item.seeker_id not in filtered_data:
            filtered_data[item.seeker_id] = item
            data_totals.setdefault(item.country_code, 0)
            data_totals[item.country_code] += 1

    grouped_data = [['country_code', 'clients']]
    for value, count in data_totals.items():
        grouped_data.append([value, count])

    return grouped_data


def get_annual_revenus_per_region(list_conversations):
    current_year = datetime.now().year
    data = {}
    for item in list_conversations:
        if item.start_time.year == current_year:
            data.setdefault(item.country_code, 0)
            data[item.country_code] += item.total_paid

    grouped_data = [['country_code', 'revenus']]
    for value, count in data.items():
        grouped_data.append([value, count])

    return grouped_data

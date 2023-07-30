
from datetime import datetime
from itertools import groupby
from enum import Enum


class LapsTime(Enum):
    year = 1
    month = 2
    day = 3


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
    print(f"data_list: {data_list}")
    current_year = datetime.now().year
    current_month = datetime.now().month

    if attr_name == 'month':
        filtered_data = [item for item in data_list if (item[0].year == current_year - 2 and item[0].month >= current_month) or
                item[0].year > current_year - 2]

        print(f"filtered_data: {filtered_data}")

    elif attr_name == 'year':
        filtered_data = [item for item in data_list if (item[0].year >= current_year - 9)]

    grouped_data = []
    for key, group in groupby(filtered_data, (lambda x: getattr(x[0], attr_name))):
        data = list(group)
        data_total = sum(1 for item in data)
        formatted_data = data[0][0].strftime('%Y-%m') if attr_name == LapsTime.month.name else data[0][0].strftime('%Y')
        grouped_data.append([formatted_data, data_total])

    return [['date', 'count'], *grouped_data]


def get_number_of_clients(list_conversations):

    print(f"list_conversations: {list_conversations}")
    get_number_of_news_clients_by_month(list_conversations, LapsTime.month.name)

    unique_list = []

    # Iterate through the list_objects
    for conversation in list_conversations:
        if conversation.seeker_id not in unique_list:
            # If userId is not in the dictionary, add the object
            unique_list.append(conversation.seeker_id)
    return len(unique_list)


def get_number_of_news_clients_by_month(list_conversations, attr_name):
    # sorted_conversations = sorted(list_conversations, key=lambda x: x.start_time)
    unique_conversation_seeker = {}
    for conversation in list_conversations:
        if conversation.seeker_id not in unique_conversation_seeker or conversation.start_time < unique_conversation_seeker[conversation.seeker_id]:
            unique_conversation_seeker[conversation.seeker_id] = conversation.start_time

    filtered_data = [( buying_date, client_id) for client_id, buying_date in unique_conversation_seeker.items()]
    print(f"unique_conversation_seeker: {filtered_data}")
    grouped_data = []
    for key, group in groupby(filtered_data, (lambda x: getattr(x[0], attr_name))):
        data = list(group)
        data_total = sum(1 for item in data)
        formatted_data = data[0][0].strftime('%Y-%m') if attr_name == 'month' else data[0][0].strftime('%Y')
        grouped_data.append([formatted_data, data_total])

    print([['date', 'count'], *grouped_data])
    return [['date', 'count'], *grouped_data]

    # unique_list = []
    #
    # # Iterate through the list_objects
    # for conversation in list_conversations:
    #     if conversation.seekerId not in unique_list:
    #         # If userId is not in the dictionary, add the object
    #         unique_list.append(conversation.seekerId)
    # return len(unique_list)





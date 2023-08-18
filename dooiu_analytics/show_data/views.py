import json
from dooiu_analytics.settings import BASE_DIR
from django.shortcuts import render, redirect
from login.models import UserProfile
from show_data.models import Conversation
from services import database_services, get_datas_for_graphs
from services.get_datas_for_graphs import LapsTime, sales_or_calltime

from services.decorators import login_and_referer_required


def get_current_user(request) -> UserProfile:
    current_user_dict = request.session.get('current_user')
    return UserProfile(**current_user_dict)


def get_conversations(current_user):
    datas = database_services.get_conversations(current_user.id)

    list_conversations = [Conversation(
        conversation_id=data[0],
        seeker_id=data[1],
        start_time=data[2],
        end_time=data[3],
        started_by=data[4],
        country_code=data[5],
        paid_seconds=data[6],
        free_seconds=data[7],
        total_paid=data[8],
        fee_amount=data[9]
    ) for data in datas]
    return list_conversations


@login_and_referer_required
def heatmap(request):
    current_user = get_current_user(request)
    if current_user:
        list_conversations = get_conversations(current_user)
        calltime = get_datas_for_graphs.get_actual_week_sales_per_day_hour(list_conversations,
                                                                           sales_or_calltime.calltime.name)
        sales = get_datas_for_graphs.get_actual_week_sales_per_day_hour(list_conversations,
                                                                        sales_or_calltime.sales.name)
        print(calltime)

        context = {
            'user': current_user,
            'sales': json.dumps(sales),
            'calltime': json.dumps(calltime),
        }
        return render(request, 'heatmap.html', context)


@login_and_referer_required
def home(request):
    current_user = get_current_user(request)

    if current_user:
        # def convert_to_json_value(value):
        #     if value is None:
        #         return None
        #     else:
        #         return value
        #
        # Preprocess the data to convert None and numpy.nan to JSON-compatible values
        # nullable_graph = [[convert_to_json_value(value) for value in row] for row in graph_data_4]

        list_conversations = get_conversations(current_user)

        day_list = get_datas_for_graphs.get_communication_by_day(list_conversations)
        month_list = get_datas_for_graphs.get_communication_by_date(list_conversations, LapsTime.month.name)
        year_list = get_datas_for_graphs.get_communication_by_date(list_conversations, LapsTime.year.name)
        number_of_clients = get_datas_for_graphs.get_number_of_clients(list_conversations)
        news_clients_per_month = get_datas_for_graphs.get_number_of_news_clients_by_month(list_conversations,
                                                                                          LapsTime.month.name)

        # print(f"month list: {month_list}  reverse list: { month_list[:1] + month_list[1:][::-1]}")
        context = {
            'user': current_user,
            'day_list': json.dumps(day_list[:1] + day_list[1:][::-1]),
            'month_list': json.dumps(month_list[:1] + month_list[1:][::-1]),
            'year_list': json.dumps(year_list[:1] + year_list[1:][::-1]),
            'number_of_clients': number_of_clients,
            'news_clients_per_month': json.dumps(news_clients_per_month[:1] + news_clients_per_month[1:][::-1]),
        }

        return render(request, 'home.html', context)


@login_and_referer_required
def regionmap(request):
    current_user = get_current_user(request)
    if current_user:
        list_conversations = get_conversations(current_user)
        clients_per_region = get_datas_for_graphs.get_clients_per_region(list_conversations)
        annual_revenus_per_region = get_datas_for_graphs.get_annual_revenus_per_region(list_conversations)
        # print(annual_revenus_per_region)

        context = {
            'user': current_user,
            'clients_per_region': json.dumps(clients_per_region),
            'annual_revenus_per_region': json.dumps(annual_revenus_per_region),
        }
    return render(request, 'regionmap.html', context)


import json
from django.core import serializers
from dooiu_analytics.settings import BASE_DIR
from django.http import HttpResponse
from django.shortcuts import render, redirect
from login.models import UserProfile
from show_data.models import Conversation
from services import database_services, get_datas_for_graphs
from services.get_datas_for_graphs import LapsTime
import datetime
from login import views as login_views
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import pickle


def get_current_user(request) -> UserProfile:
    current_user_dict = request.session.get('current_user')
    return UserProfile(**current_user_dict)


def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')


# @login_required
def home(request):
    current_user = get_current_user(request)
    if current_user:
        context = {
            'user': current_user
        }
        return render(request, 'home.html', context)
    else:
        # Gérer le cas où le nom d'utilisateur n'est pas présent dans la session
        return redirect('login')


def customer_analytic(request):

    current_user = get_current_user(request)

    if current_user:
        graph_data_1 = [
            ['Date', 'Visitors'],
            ['2023-01-01', 100],
            ['2023-01-02', 150],
            ['2023-01-03', 200]
        ]

        graph_data_2 = [
            ['Category', 'Quantity'],
            ['Category A', 50],
            ['Category B', 80],
            ['Category C', 120]
        ]

        graph_data_3 = [
            ['Browser', 'Users'],
            ['Chrome', 500],
            ['Firefox', 300],
            ['Safari', 200]
        ]

        graph_data_4 = [
            ['Month', 'Sales', 'Expenses'],
            ['January', 1000, None],
            ['February', 1200, 900],
            ['March', 1400, 1000]
        ]

        def convert_to_json_value(value):
            if value is None:
                return None
            else:
                return value

        # Preprocess the data to convert None and numpy.nan to JSON-compatible values
        nullable_graph = [[convert_to_json_value(value) for value in row] for row in graph_data_4]

        # graph_data_5 = [
        #     {"Month": 'January', "Sales": 1000, "Expenses": 800},
        #     {"Month": 'February', "Sales": 1200, "Expenses": 900},
        #     {"Month": 'March', "Sales": 1400, "Expenses": 1000},
        # ]

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

        day_list = get_datas_for_graphs.get_communication_by_day(list_conversations)
        month_list =get_datas_for_graphs.get_communication_by_date(list_conversations, LapsTime.month.name)
        year_list =get_datas_for_graphs.get_communication_by_date(list_conversations, LapsTime.year.name)


        number_of_clients = get_datas_for_graphs.get_number_of_clients(list_conversations)
        news_clients_per_month = get_datas_for_graphs.get_number_of_news_clients_by_month(list_conversations, LapsTime.month.name)

        # print(f"month list: {month_list}  reverse list: { month_list[:1] + month_list[1:][::-1]}")
        context = {
            'user': current_user,
            'graph_data_1': json.dumps(graph_data_1),
            'graph_data_2': json.dumps(graph_data_2),
            'graph_data_3': json.dumps(graph_data_3),
            'graph_data_4': json.dumps(nullable_graph),
            'day_list': json.dumps(day_list[:1] + day_list[1:][::-1]),
            'month_list': json.dumps(month_list[:1] + month_list[1:][::-1]),
            'year_list': json.dumps(year_list[:1] + year_list[1:][::-1]),
            'number_of_clients': number_of_clients,
            'news_clients_per_month': json.dumps(news_clients_per_month[:1] + news_clients_per_month[1:][::-1]),
        }

        return render(request, 'customer_analytic.html', context)
        # return JsonResponse(data)
    else:
        # Gérer le cas où le nom d'utilisateur n'est pas présent dans la session
        return redirect('login')

def sales_analytic(request):

    current_user = get_current_user(request)
    if current_user:
        context = {
            'user': current_user,
            'labels': ['Label 1', 'Label 2', 'Label 3'],
            'values': [10, 20, 30]
        }
    return render(request, 'sales_analytic.html', context)
    # return JsonResponse(data)
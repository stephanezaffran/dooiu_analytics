
from django.db import connection
from django.db import models


def get_user_data(phone_number):
    try:
        with connection.cursor() as cursor:
            # print(f"authenticate: select * from user where phoneNumber = '{phone_number}' and password = '{password}';")
            cursor.execute(f"select * FROM user where phoneNumber = '{phone_number}' LIMIT 1;")
            user_data = cursor.fetchone()
            print(f"user_data:  {user_data}")

            if user_data:
                return user_data
            else:
                return None


            # if user_data:
            #     user = self.model(phone_number=user_data[3])  # Assuming phone_number is in the second column
            #     print(f"entered to user_data : {user}  password: {user_data[8]} ")
            #     if password == user_data[8]:
            #         print(f"password: {user_data[8]}")
            #         return user

    except Exception as e:
        print(f"exception authenticate: {e.__str__()}")
        # Handle any exceptions here (e.g., database connection error)
        return None


def get_conversations(id):

    requete_sql = f'''
        SELECT 
            c.id AS conversation_id,
            c.seekerId AS seekerId,
            c.startTime AS startTime,
            c.endTime AS endTime,
            c.startedBy AS startedBy,
            usr.countryCode AS countryCode,
            cstat.paidSeconds AS paidSeconds,
            cstat.freeSeconds AS freeSeconds,
            cstat.paidSeconds AS paidSeconds,
            cstat.totalPaid AS totalPaid,
            cstat.feeAmount AS feeAmount
        FROM 
            conversation c
        JOIN 
            user usr ON c.seekerId = usr.id
        JOIN 
            conversationstats cstat ON c.id = cstat.conversationId
        WHERE 
            c.serviceProviderId ={id}
            AND c.status = 'success';
    '''
    try:
        with connection.cursor() as cursor:
            cursor.execute(requete_sql)
            conversations_datas = cursor.fetchall()
            print(f"conversations_datas:  {conversations_datas}")

            if conversations_datas:
                return conversations_datas
            else:
                return None

            # if user_data:
            #     user = self.model(phone_number=user_data[3])  # Assuming phone_number is in the second column
            #     print(f"entered to user_data : {user}  password: {user_data[8]} ")
            #     if password == user_data[8]:
            #         print(f"password: {user_data[8]}")
            #         return user

    except Exception as e:
        print(f"exception authenticate: {e.__str__()}")
        # Handle any exceptions here (e.g., database connection error)
        return None
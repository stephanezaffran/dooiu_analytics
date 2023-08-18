from django.db import models
from datetime import datetime
import datetime


# class Data(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     timestamp = models.DateTimeField()
#     value = models.FloatField()

class Conversation(models.Model):
    conversation_id = models.IntegerField()
    seeker_id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    started_by = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    paid_seconds = models.IntegerField()
    free_seconds = models.IntegerField()
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'''conversation_id: {self.conversation_id}  - seekerId: {self.seeker_id} - 
               startTime: {self.start_time} - endTime: {self.end_time} - startedBy: {self.started_by} - countryCode: {self.country_code} -
               paidSeconds: {self.paid_seconds} - freeSeconds: {self.free_seconds} - totalPaid: {self.total_paid} - feeAmount: {self.fee_amount}
                '''

    def get_clients(self):
        # call_time = self.freeSeconds + self.paidSeconds

        return [self.start_time.strftime("%Y-%m-%d"), self.seeker_id]

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'phone_number': self.phone_number,
    #         'email': self.email,
    #         'country_code': self.country_code,
    #         'user_type': self.user_type,
    #         'first_name': self.first_name,
    #         'last_name': self.last_name,
    #     }

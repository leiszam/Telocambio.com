from django.db import models
from .user import User
from datetime import datetime

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='profile', on_delete=models.CASCADE)
    birth_date = models.DateTimeField(default=datetime.now)
    gender = models.CharField('Gender', max_length=15, default=0)
    country = models.CharField('Country', max_length=15, default=0)
    payment_method = models.CharField('Payment Method ', max_length=15, default=0)
    notification_status = models.BooleanField()
    plan_type = models.CharField('Plan Type', max_length=15, default=0)




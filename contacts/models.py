from django.db import models
from datetime import datetime
# Create your models here.

class contact(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    car_id=models.IntegerField()
    consumer_needs=models.CharField(max_length=150)
    car_title=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    mobile_no=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    message=models.TextField(blank=True)
    user_id=models.IntegerField(blank=True)
    created_date=models.DateTimeField(blank=True,default=datetime.now)


    def __str__(self):
        return self.email

from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    contact = models.IntegerField()
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=200)


    def __str__(self):
        return self.name



class Service(models.Model):
    service_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    registation_no = models.IntegerField()
    service_date = models.DateField()
    service_time = models.TimeField()
    delivery_type = models.CharField(max_length=200)
    CHOICES = (('panding','panding'),('apsept','apsept'),('reject','reject'),('complite','complite'),)
    status = models.CharField(max_length = 200 ,choices = CHOICES)









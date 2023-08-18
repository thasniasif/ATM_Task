from django.db import models

# Create your models here.
class tb_atm(models.Model):
    fname = models.CharField(max_length=100, blank=True)
    lname = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=100, blank=True)
    accn_num = models.CharField(max_length=100, blank=True)
    amount = models.CharField(max_length=100, blank=True)

class trans(models.Model):
    p_id= models.ForeignKey(tb_atm, on_delete=models.CASCADE)
    t_date=models.DateTimeField('Created', auto_now=True)
    t_type=models.CharField(max_length=50,blank=True)
    t_amount=models.CharField(max_length=50,blank=True)

from django.db import models
from django.utils.crypto import get_random_string

class Account(models.Model):
    email=models.EmailField(unique=True)
    account_id=models.AutoField(primary_key=True)
    account_name=models.CharField(max_length=255)
    app_secret_token=models.CharField(max_length=255,blank=True)
    website=models.URLField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if not self.app_secret_token:
            self.app_secret_token=get_random_string(50)
        super().save(*args,**kwargs)
    def __str__(self):
        return self.account_name
    
class Destination(models.Model):
    account=models.ForeignKey(Account,related_name='destinations',on_delete=models.CASCADE)
    url=models.URLField()
    http_method=models.CharField(max_length=10,choices=[('GET','GET'),('POST','POST'),('PUT','PUT')])
    headers=models.JSONField()

    def __str__(self):
        return self.url

# Create your models here.

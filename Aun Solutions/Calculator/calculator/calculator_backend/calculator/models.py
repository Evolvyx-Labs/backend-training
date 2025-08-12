from django.db import models

# Create your models here.
class Calculations(models.Model):
    given_expression = models.TextField(max_length=200)
    end_result = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add= True)
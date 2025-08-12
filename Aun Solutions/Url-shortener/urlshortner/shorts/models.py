from django.db import models

# Create your models here.



class Urls(models.Model):
    orignal_url = models.TextField()
    short_url = models.TextField()
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return f"{self.short_url} -> {self.orignal_url} ({self.clicks} clicks)"
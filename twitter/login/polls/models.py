from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    tweet_text = models.CharField(max_length=200)
    tweet_date = models.DateTimeField('date tweeted')
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    

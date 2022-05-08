from django.db import models

# Create your models here.

class Lobby(models.Model):
    lobby_name = models.CharField(max_length=15)
    lobby_desc = models.CharField(max_length=30)
    lobby_score = models.IntegerField()
    lobby_users = models.JSONField(default=dict, editable=False)
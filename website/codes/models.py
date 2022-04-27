from django.db import models

class Code(models.Model):
    code_title = models.TextField()
    code_description = models.TextField()
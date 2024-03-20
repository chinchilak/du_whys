from django.db import models

class DynamicModel(models.Model):
    model_name = models.CharField(max_length=255)
    # date = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()

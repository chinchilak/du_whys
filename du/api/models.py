from django.db import models

class DynamicModel(models.Model):
    model_name = models.CharField(max_length=255)
    data = models.JSONField()

# class Attribute(models.Model):
#     id = models.AutoField(primary_key=True)
#     nazev_atributu_id = models.IntegerField()
#     hodnota_atributu_id = models.IntegerField()

# class AttributeName(models.Model):
#     id = models.AutoField(primary_key=True)
#     nazev = models.CharField(max_length=255)

# class AttributeValue(models.Model):
#     id = models.AutoField(primary_key=True)
#     hodnota = models.CharField(max_length=255)
from django.db import models

# Create your models here.


class OfficeM(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=15)

    class Meta:
        db_table = 'office'
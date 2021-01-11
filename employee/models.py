from django.db import models

from myapp.models import OfficeM


class  EmployeeM(models.Model):
    class Meta:
        db_table = 'employees'
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    city = models.CharField(max_length=20)
    office = models.ForeignKey(OfficeM, on_delete=models.CASCADE, related_name='employees')
    photo = models.ImageField(upload_to='employee/photos', default='', blank=True)
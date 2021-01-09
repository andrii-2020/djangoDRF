# Generated by Django 3.1.5 on 2021-01-08 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='myapp.officem')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
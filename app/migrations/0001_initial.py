# Generated by Django 4.2.7 on 2023-12-15 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('emp_no', models.IntegerField()),
                ('sal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_loc', models.CharField(max_length=100)),
                ('dept_name', models.CharField(max_length=100)),
                ('emp_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
        migrations.CreateModel(
            name='CEO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('MD', models.CharField(max_length=100)),
                ('dept_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]

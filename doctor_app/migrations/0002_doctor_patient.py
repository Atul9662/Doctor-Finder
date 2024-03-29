# Generated by Django 2.0 on 2021-03-13 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30)),
                ('Lastname', models.CharField(max_length=30)),
                ('Age', models.IntegerField(default=123)),
                ('Address', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=20)),
                ('Department', models.CharField(max_length=20)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor_app.Admin')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=30)),
                ('Lastname', models.CharField(max_length=30)),
                ('Age', models.IntegerField(default=123)),
                ('Address', models.CharField(max_length=255)),
                ('Gender', models.CharField(max_length=20)),
                ('Patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor_app.Admin')),
            ],
        ),
    ]

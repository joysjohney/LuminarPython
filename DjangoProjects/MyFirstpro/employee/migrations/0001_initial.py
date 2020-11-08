# Generated by Django 3.1.2 on 2020-11-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120, unique=True)),
                ('uname', models.CharField(max_length=125, unique=True)),
                ('password', models.CharField(max_length=120)),
                ('salary', models.IntegerField(default=5000)),
            ],
        ),
    ]

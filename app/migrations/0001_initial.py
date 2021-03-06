# Generated by Django 3.1.2 on 2020-10-19 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('cat_form', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='CallBack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.BigIntegerField()),
                ('cat_form', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='DownFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('cat_form', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='FooterFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('cat_form', models.CharField(max_length=128)),
            ],
        ),
    ]

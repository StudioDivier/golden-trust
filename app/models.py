from django.db import models

# Create your models here.


class CallBack(models.Model):
    name = models.CharField(name='name', max_length=128)
    phone = models.BigIntegerField(name='phone')
    cat_form = models.CharField(name='cat_form', max_length=128)


class BuyFeed(models.Model):
    name = models.CharField(name='name', max_length=128)
    phone = models.BigIntegerField(name='phone')
    email = models.EmailField(name='email')
    cat_form = models.CharField(name='cat_form', max_length=128)


class DownFeed(models.Model):
    name = models.CharField(name='name', max_length=128)
    phone = models.BigIntegerField(name='phone')
    email = models.EmailField(name='email')
    cat_form = models.CharField(name='cat_form', max_length=128)

class FooterFeed(models.Model):
    name = models.CharField(name='name', max_length=128)
    phone = models.BigIntegerField(name='phone')
    email = models.EmailField(name='email')
    cat_form = models.CharField(name='cat_form', max_length=128)
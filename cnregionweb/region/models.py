from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=100)
    pinyin = models.CharField(max_length=100)

class City(models.Model):
    name = models.CharField(max_length=100)
    pinyin = models.CharField(max_length=100)

class County(models.Model):
    name = models.CharField(max_length=100)
    pinyin = models.CharField(max_length=100)

class Town(models.Model):
    name = models.CharField(max_length=100)
    pinyin = models.CharField(max_length=100)

class Village(models.Model):
    name = models.CharField(max_length=100)
    pinyin = models.CharField(max_length=100)
from django.db import models

class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class Certification(models.Model):
    name = models.CharField(max_length=100)
    authority = models.CharField(max_length=100)

class Publication(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=100)

from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Organization_type(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Organization(models.Model):
    type = models.ForeignKey(Organization_type, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    summary = models.CharField(max_length=200)
    website = models.URLField()

    def __str__(self):
        return self.name + " - " + self.type.name


class Education(models.Model):
    university = models.ForeignKey(Organization, on_delete=models.PROTECT)
    degree = models.CharField(max_length=40)
    major = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField()
    summary = models.CharField(max_length=200)
    details = HTMLField()

    def __str__(self):
        return self.degree + " in " + self.major + " from " + self.university.name


class Experience(models.Model):
    company = models.ForeignKey(Organization, on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    summary = models.CharField(max_length=200)
    details = HTMLField()

    def __str__(self):
        return self.title + " @ " + self.company.name


class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField()
    summary = models.CharField(max_length=200)
    details = HTMLField()
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.title + " @ " + self.organization.name

class Skill_type(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Skill(models.Model):
    type = models.ForeignKey(Skill_type, on_delete=models.SET_DEFAULT, default=0)
    name = models.CharField(max_length=30)
    proficiency_level = models.IntegerField()

    def __str__(self):
        return self.name + " - " + self.type.name

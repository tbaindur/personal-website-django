from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User


# Create your models here.

class Intro(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, default=1)
    name = models.CharField(max_length=40)
    headline = models.CharField(max_length=100)
    summary = HTMLField()
    profile_pic = models.ImageField(default="intro_pics/default_profile_pic.jpg", upload_to='intro_pics')
    cover_pic = models.ImageField(null=True, upload_to='intro_pics')
    resume = models.FileField(upload_to='docs', null=True)
    linkedin_url = models.URLField(null=True, blank=True, default="#")
    github_url = models.URLField(null=True, blank=True, default="#")
    instagram_url = models.URLField(null=True, blank=True, default="#")
    facebook_url = models.URLField(null=True, blank=True, default="#")

    def __str__(self):
        return f'{ self.name } Intro'


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
    summary = models.CharField(max_length=200, blank=True, null=True)
    website = models.URLField()

    def __str__(self):
        return self.name + " - " + self.type.name


class Education(models.Model):
    university = models.ForeignKey(Organization, on_delete=models.PROTECT)
    degree = models.CharField(max_length=40)
    major = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    details = HTMLField()

    def __str__(self):
        return self.degree + " in " + self.major + " from " + self.university.name


class Experience(models.Model):
    company = models.ForeignKey(Organization, on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    details = HTMLField()

    def __str__(self):
        return self.title + " @ " + self.company.name


class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT)
    title = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True, null=True)
    details = HTMLField()

    PROJECT_TYPE_CHOICES = [
        ('Academic', 'Academic'),
        ('Professional', 'Professional'),
        ('Independent', 'Independent'),
        ('Hobby', 'Hobby')
    ]
    type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.title + " @ " + self.organization.name


class Skill_type(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Skill(models.Model):
    type = models.ForeignKey(Skill_type, on_delete=models.SET_NULL, null=True, related_name='skills')
    name = models.CharField(max_length=30)

    PROFICIENCY_LEVEL_CHOICES = [
        ('Basic', 'Basic'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert')
    ]
    proficiency_level = models.CharField(choices=PROFICIENCY_LEVEL_CHOICES, null=True, blank=True, max_length=20)

    def __str__(self):
        return self.name + " - " + self.type.name


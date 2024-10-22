from django.db import models
from datetime import date

class Target(models.Model):
    name = models.fields.CharField(max_length=100, null=True)
    url = models.fields.URLField(null=True)
    description = models.fields.CharField(max_length=200, null=True)
    ip = models.fields.CharField(max_length=15, null=True)
    hostname = models.fields.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name}'



class Vulnerability(models.Model):

    class Category(models.TextChoices):
        ENUMERATION = 'Enumeration'
        WEB_VULNERABILIY = 'Web vulnerability'
        SERVICE_VULNERABILIY = 'Service vulnerability'
        PRIVESC = 'Privesc'
        OTHER = 'Other'

    name = models.fields.CharField(max_length=100, null=True)
    url = models.fields.URLField(null=True)
    description = models.fields.CharField(max_length=200, null=True)
    category = models.fields.CharField(choices=Category.choices, max_length=100, null=True)

    def __str__(self):
        return f'{self.name}'


class Note(models.Model):
    title = models.fields.CharField(max_length=100, null=True)
    date = models.fields.DateField(null=False, default=date.today())
    content = models.fields.CharField(max_length=300, null=True)
    linked_target = models.ForeignKey(Target, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'

from django.db import models
from datetime import date

class Target(models.Model):

    class status(models.TextChoices):
        INTACT = 'Intact'
        FOOTHOLD = 'Foothold'
        ROOTED = 'Rooted'

    class type(models.TextChoices):
        CAPTURE_THE_FLAG = 'Capture the Flag'
        IN_THE_WILD = 'In the Wild'
        BUG_BOUNTY = 'Bug Bounty' 

    name = models.fields.CharField(max_length=100, null=True)
    url = models.fields.URLField(null=True)
    description = models.fields.CharField(max_length=500, null=True, blank=True)
    ip = models.fields.CharField(max_length=15, null=True)
    hostname = models.fields.CharField(max_length=100, null=True, blank=True)
    status = models.fields.CharField(choices=status.choices, max_length=8, default='Intact')
    type = models.fields.CharField(choices=type.choices, max_length=16, default = 'Wild')

    def __str__(self):
        return f'{self.name}'



class Vulnerability(models.Model):

    class Category(models.TextChoices):
        ENUMERATION = 'Enumeration'
        WEB_VULNERABILIY = 'Web vulnerability'
        SERVICE_VULNERABILIY = 'Service vulnerability'
        PRIVESC = 'Privesc'
        OTHER = 'Other'

    name = models.fields.CharField(max_length=200, null=True)
    url = models.fields.URLField(null=True)
    description = models.fields.CharField(max_length=1000, null=True)
    category = models.fields.CharField(choices=Category.choices, max_length=100, null=True)
    cve = models.fields.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Note(models.Model):
    title = models.fields.CharField(max_length=100, null=True)
    date = models.fields.DateField(null=False, default=date.today())
    content = models.fields.CharField(max_length=1000, null=True)
    linked_target = models.ForeignKey(Target, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'



class Ressource(models.Model):
    name = models.fields.CharField(max_length=100, null=True)
    url = models.fields.URLField(null=True)
    description = models.fields.CharField(max_length=600, null=True)

    def __str__(self):
        return f'{self.name}'
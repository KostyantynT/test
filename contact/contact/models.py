from django.db import models


class ContactInfo(models.Model):
    #this class will represent django model for ContactInfo
    name = models.CharField("Name", max_length=50)
    surname = models.CharField("Last name", max_length=50)
    birthdate = models.DateTimeField("Date of birth")
    bio = models.CharField("Bio", max_length=256)
    #I know it will be required :)
    #photo = models.ImageField("Photo", upload_to="images/", blank=True, null=True)
    #Contacts...
    email = models.EmailField("Email", max_length=254, default='')
    jabber = models.CharField("Jabber", max_length=50, default='')
    skype = models.CharField("Skype", max_length=50, default='')
    other = models.CharField("Other contacts", max_length=256, default='')


class RequestLog(models.Model):
    path = models.CharField("Request", max_length=256)
    time = models.DateTimeField("Date/Time", auto_now_add=True)

    class Meta:
        ordering = ['time']

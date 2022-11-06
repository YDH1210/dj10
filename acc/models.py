from distutils.command.upload import upload
from email.policy import default
from xml.etree.ElementTree import Comment
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pic = models.ImageField(upload_to="user")
    comment = models.TextField()
    point = models.IntegerField(default=0)

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.png"

# Create your models here.

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Message(models.Model):
    author = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class MessageAttachment(models.Model):
    attachment = models.FileField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.attachment.url

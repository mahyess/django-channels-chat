from django.contrib import admin
from .models import Message, MessageAttachment


class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'timestamp']


admin.site.register(Message, MessageAdmin)
admin.site.register(MessageAttachment)

from rest_framework.serializers import ModelSerializer

from chat.models import Message, MessageAttachment


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class MessageAttachmentSerializer(ModelSerializer):
    class Meta:
        model = MessageAttachment
        fields = "__all__"

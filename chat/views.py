from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from chat.serializers import MessageAttachmentSerializer, MessageSerializer


def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name, user_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'user_name': user_name
    })


@api_view(['POST'])
def add_message_attachment(request):
    data = {}
    attachment = request.data.get('attachment', None)
    author = request.data.get('author')
    if attachment and author:
        kind = attachment.content_type

        if "image" in kind or "video" in kind:
            data['attachment'] = attachment
        else:
            return Response(data={
                "media": "Only video/image file is supported for now."
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = MessageAttachmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            create_message_serializer = MessageSerializer(
                data={"message": f"[[ATTACHMENT]]:[[{kind}]]:{serializer.data['attachment']}",
                      "author": author})
            if create_message_serializer.is_valid():
                create_message_serializer.save()

                return Response({
                    "msg": "Success",
                    "instance": create_message_serializer.data
                }, status=status.HTTP_200_OK)

            return Response({
                "msg": "error",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "msg": "error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        "msg": "errorrr",
    }, status=status.HTTP_400_BAD_REQUEST)

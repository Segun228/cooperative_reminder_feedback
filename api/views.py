from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Message
from .serializers import MessageSerializer
from rest_framework.generics import CreateAPIView
from .sender import send_email
from rest_framework.response import Response
from rest_framework import status


class getFeedbackView(CreateAPIView):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_email(message=serializer.data.get("body", None))
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



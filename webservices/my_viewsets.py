# -*- coding: utf-8 -*-
from rest_framework import viewsets

from webservices.my_serializers import *


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class ChapterViewSet(viewsets.ModelViewSet):
    queryset = Chapter.objects.all()
    serializer_class = ChapterSerializer


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CdDvdViewSet(viewsets.ModelViewSet):
    queryset = CdDvd.objects.all()
    serializer_class = CdDvdSerializer


####################################### NEW ##########################################

class LessonTypeViewSet(viewsets.ModelViewSet):
    queryset = LessonType.objects.all()
    serializer_class = LessonTypeSerializer


class SaloonViewSet(viewsets.ModelViewSet):
    queryset = Saloon.objects.all()
    serializer_class = SaloonSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class JokeViewSet(viewsets.ModelViewSet):
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer


class StrangeStorieViewSet(viewsets.ModelViewSet):
    queryset = StrangeStorie.objects.all()
    serializer_class = StrangeStorieSerializer


class ReflectViewSet(viewsets.ModelViewSet):
    queryset = Reflect.objects.all()
    serializer_class = ReflectSerializer


class MultiMediaArchiveViewSet(viewsets.ModelViewSet):
    queryset = MultiMediaArchive.objects.all()
    serializer_class = MultiMediaArchiveSerializer

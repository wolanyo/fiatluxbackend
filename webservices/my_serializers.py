# -*- coding: utf-8 -*-
from rest_framework import serializers

from webservices.models import *


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'mediaType', 'mediaURL', 'postDate', 'postTime', 'excerpt', 'content', 'image')


class PostDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'mediaType', 'mediaURL', 'postDate', 'postTime', 'image', 'content')


class LessonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'position', 'excerpt',)


class ChapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'position', 'excerpt')


class ChapterDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'title', 'position', 'content')


class DocumentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'position', 'author', 'reference', 'price')


class CdDvdSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CdDvd
        fields = ('id', 'title', 'author', 'price', 'duration', 'image', 'mediaURL')


class CdDvdDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CdDvd
        fields = ('id', 'title', 'author', 'price', 'duration', 'image', 'excerpt', 'mediaURL')


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'image')


class BookDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'price', 'image', 'excerpt', 'excerptFile')


# Publicity serializer
class PublicitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publicity
        fields = ('id', 'title', 'publicationDate', 'image')


class PublicityDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publicity
        fields = ('id', 'title', 'publicationDate', 'excerpt', 'mediaType', 'image')


# TimeTable serializer
class TimeTableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeTable
        fields = ('id', 'title', 'eventDate', 'startTime', 'endTime', 'image')


class TimeTableDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeTable
        fields = ('id', 'title', 'eventDate', 'startTime', 'endTime', 'image', 'address', 'excerpt')


# Help serializer
class HelpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Help
        fields = ('id', 'title', 'publicationDate', 'image')


class HelpDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Help
        fields = ('id', 'title', 'publicationDate', 'image', 'excerpt')


####################################################NEW###########################
class LessonTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LessonType
        fields = ('id', 'label', 'description',)


class SaloonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Saloon
        fields = ('id', 'title', 'description', 'dateCreation', 'timeCreation', 'image',)


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'title', 'description', 'dateCreation', 'timeCreation', 'image',)


class JokeStoryReflectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JokeStoryReflect
        fields = ('id', 'title', 'excerpt', 'image')


class JokeStoryReflectDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JokeStoryReflect
        fields = ('id', 'title', 'content', 'image')


class JokeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Joke
        fields = ('id', 'title', 'excerpt', 'image')


class JokeDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Joke
        fields = ('id', 'title', 'content', 'image')


class StrangeStorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StrangeStorie
        fields = ('id', 'title', 'excerpt', 'image')


class StrangeStorieDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StrangeStorie
        fields = ('id', 'title', 'content', 'image')


class ReflectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reflect
        fields = ('id', 'title', 'excerpt', 'image')


class ReflectDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reflect
        fields = ('id', 'title', 'content', 'image')


class MultiMediaArchiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultiMediaArchive
        fields = ('id', 'title', 'publishDate', 'mediaURL', 'excerpt', 'image')


class MultiMediaArchiveDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MultiMediaArchive
        fields = ('id', 'title', 'publishDate', 'archiveType', 'playerType', 'excerpt', 'image')

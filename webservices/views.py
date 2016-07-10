# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .my_serializers import *


# ---------------------------------------POST WEB SERVICE-------------------------
@api_view(['GET', 'POST'])
def post_list(request, section):
    if request.method == 'GET':
        if section == "ALL":
            posts = Post.objects.all().order_by('-postDate', '-postTime')
        else:
            posts = Post.objects.filter(section=section).order_by('-postDate', '-postTime')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def post_media_list(request, section,  mediaType):
    if request.method == 'GET':
        if section == "ALL":
            posts = Post.objects.filter(mediaType=mediaType).order_by('-postDate', '-postTime')
        else:
            posts = Post.objects.filter(section=section, mediaType=mediaType).order_by('-postDate', '-postTime')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def post_details(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostDetailsSerializer(post)
        return Response(serializer.data)


# ------------------------------------------- LessonType Web Services-----------------------------------
@api_view(['GET', 'POST'])
def lesson_type_list(request, section):
    if request.method == 'GET':
        if section == "ALL":
            lesson_types = LessonType.objects.all().order_by("position")
        else:
            lesson_types = LessonType.objects.filter(section=section).order_by("position")
        serializer = LessonTypeSerializer(lesson_types, many=True)
        return Response(serializer.data)


# ------------------------------------------- Lesson Web Services-----------------------------------
@api_view(['GET', 'POST'])
def lesson_list(request, lessonTypeId):
    try:
        lessonType = LessonType.objects.get(id=lessonTypeId)
    except LessonType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            lessons = Lesson.objects.filter(lessonType=lessonType).order_by('position')
            serializer = LessonSerializer(lessons, many=True)
            return Response(serializer.data)
        except Lesson.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def lesson_details(request, pk):
    try:
        lesson = Lesson.objects.get(id=pk)
    except Lesson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            chapters = Chapter.objects.filter(lesson=lesson)
            serializer = ChapterSerializer(chapters, many=True)
            return Response(serializer.data)
        except Chapter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


# ------------------------------------------- Chapter Web Services-----------------------------------
@api_view(['GET', 'POST'])
def chapter_list(request, pk):
    try:
        lesson = Lesson.objects.get(id=pk)
    except Lesson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            chapters = Chapter.objects.filter(lesson=lesson).order_by('position')
            serializer = ChapterSerializer(chapters, many=True)
            return Response(serializer.data)
        except Chapter.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'POST'])
def chapter_details(request, pk):
    try:
        chapter = Chapter.objects.get(id=pk)
    except Chapter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChapterDetailsSerializer(chapter)
        return Response(serializer.data)


# ------------------------------------------- Book Web Services-----------------------------------
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all().order_by('id')
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def book_details(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookDetailsSerializer(book)
        return Response(serializer.data)


# ------------------------------------------- CDdvd Web Services-----------------------------------
@api_view(['GET', 'POST'])
def cddvd_list(request, cdDvdType):
    if request.method == 'GET':
        cddvds = CdDvd.objects.filter(discType=cdDvdType).order_by('id')
        serializer = CdDvdSerializer(cddvds, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def cddvd_details(request, pk):
    try:
        cddvd = CdDvd.objects.get(id=pk)
    except CdDvd.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CdDvdDetailsSerializer(cddvd)
        return Response(serializer.data)


# ------------------------------------------- Joke Story Reflect Web Services-----------------------------------
@api_view(['GET', 'POST'])
def jokeStoryReflect_list(request, type):
    if request.method == 'GET':
        jokeStoryReflects = JokeStoryReflect.objects.filter(type=type).order_by('id')
        serializer = JokeStoryReflectSerializer(jokeStoryReflects, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def jokeStoryReflect_details(request, pk):
    try:
        jokeStoryReflect = JokeStoryReflect.objects.get(id=pk)
    except JokeStoryReflect.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = JokeStoryReflectDetailsSerializer(jokeStoryReflect)
        return Response(serializer.data)


# ------------------------------------------- Joke Web Services-----------------------------------
@api_view(['GET', 'POST'])
def joke_list(request):
    if request.method == 'GET':
        jokes = Joke.objects.all().order_by('id')
        serializer = JokeSerializer(jokes, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def joke_details(request, pk):
    try:
        joke = Joke.objects.get(id=pk)
    except Joke.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = JokeDetailsSerializer(joke)
        return Response(serializer.data)


# ------------------------------------------- StrangeStory Web Services-----------------------------------
@api_view(['GET', 'POST'])
def strange_story_list(request):
    if request.method == 'GET':
        stories = StrangeStorie.objects.all().order_by('-id')
        serializer = StrangeStorieSerializer(stories, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def strange_story_details(request, pk):
    try:
        story = StrangeStorie.objects.get(id=pk)
    except StrangeStorie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StrangeStorieDetailsSerializer(story)
        return Response(serializer.data)


# ------------------------------------------- Saloon Web Services-----------------------------------
@api_view(['GET', 'POST'])
def saloon_list(request):
    if request.method == 'GET':
        saloons = Saloon.objects.all().order_by('-id')
        serializer = SaloonSerializer(saloons, many=True)
        return Response(serializer.data)


# ------------------------------------------- Reflect Web Services-----------------------------------
@api_view(['GET', 'POST'])
def reflect_list(request):
    if request.method == 'GET':
        reflects = Reflect.objects.all().order_by('-id')
        serializer = ReflectSerializer(reflects, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def reflect_details(request, pk):
    try:
        reflect = Reflect.objects.get(id=pk)
    except Reflect.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReflectDetailsSerializer(reflect)
        return Response(serializer.data)


# ------------------------------------------- MultimediaArchive Web Services-----------------------------------
@api_view(['GET', 'POST'])
def multimediaarchive_list(request, section, mediaType):
    if request.method == 'GET':
        if section == "ALL":
            mediaarchives = MultiMediaArchive.objects.filter(archiveType=mediaType).order_by('id')
        else:
            mediaarchives = MultiMediaArchive.objects.filter(section=section, archiveType=mediaType).order_by('id')
        serializer = MultiMediaArchiveSerializer(mediaarchives, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def multimediaarchive_details(request, pk):
    try:
        mediaarchive = MultiMediaArchive.objects.get(id=pk)
    except MultiMediaArchive.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MultiMediaArchiveDetailsSerializer(mediaarchive)
        return Response(serializer.data)


# ------------------------------------------- Publicity Web Services-----------------------------------
@api_view(['GET', 'POST'])
def publicity_list(request):
    if request.method == 'GET':
        publicities = Publicity.objects.all().order_by('-publicationDate')
        serializer = PublicitySerializer(publicities, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def publicity_details(request, pk):
    try:
        publicity = Publicity.objects.get(id=pk)
    except Publicity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PublicityDetailsSerializer(publicity)
        return Response(serializer.data)


# ------------------------------------------- Help Web Services-----------------------------------
@api_view(['GET', 'POST'])
def help_list(request):
    if request.method == 'GET':
        helps = Help.objects.all().order_by('-publicationDate')
        serializer = HelpSerializer(helps, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def help_details(request, pk):
    try:
        helps = Help.objects.get(id=pk)
    except Help.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = HelpDetailsSerializer(helps)
        return Response(serializer.data)


# ------------------------------------------- TimeTable Web Services-----------------------------------
@api_view(['GET', 'POST'])
def timetable_list(request):
    if request.method == 'GET':
        timetables = TimeTable.objects.all().order_by('-eventDate')
        serializer = TimeTableSerializer(timetables, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def timetables_details(request, pk):
    try:
        timetable = TimeTable.objects.get(id=pk)
    except TimeTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TimeTableDetailsSerializer(timetable)
        return Response(serializer.data)
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from webservices import views

urlpatterns = [
    url(r'^posts/(?P<section>[A-Z]+)/$', views.post_list),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.post_details),
    url(r'^posts/(?P<section>[A-Z]+)/(?P<mediaType>[A-Z]+)/$', views.post_media_list),
    url(r'^lessontypes/(?P<section>[A-Z]+)/$', views.lesson_type_list),
    url(r'^lessons/(?P<lessonTypeId>[0-9]+)/$', views.lesson_list),
    url(r'^lessons/(?P<pk>[0-9]+)/chapter/$', views.chapter_list),
    url(r'^chapters/(?P<pk>[0-9]+)/$', views.chapter_details),
    # url(r'^jokes/$', views.joke_list),
    # url(r'^jokes/(?P<pk>[0-9]+)/$', views.joke_details),
    url(r'^jokesstoriesreflects/(?P<type>[A-Z]+)/$', views.jokeStoryReflect_list),
    url(r'^jokesstoriesreflects/(?P<pk>[0-9]+)/$', views.jokeStoryReflect_details),
    # url(r'^stories/(?P<section>[A-Z]+)/$', views.strange_story_list),
    # url(r'^stories/(?P<pk>[0-9]+)/$', views.strange_story_details),
    url(r'^saloons/(?P<section>[A-Z]+)/$', views.saloon_list),
    url(r'^books/$', views.book_list),
    url(r'^books/(?P<pk>[0-9]+)$', views.book_details),
    url(r'^cddvds/(?P<cdDvdType>[A-Z]+)/$', views.cddvd_list),
    url(r'^cddvds/(?P<pk>[0-9]+)/$', views.cddvd_details),
    # url(r'^reflects/$', views.reflect_list),
    # url(r'^reflects/(?P<pk>[0-9]+)/$', views.reflect_details),
    url(r'^multimediaarchives/(?P<section>[A-Z]+)/(?P<mediaType>[A-Z]+)/$', views.multimediaarchive_list),
    url(r'^multimediaarchives/(?P<pk>[0-9]+)/$', views.multimediaarchive_details),
    url(r'^publicities/$', views.publicity_list),
    url(r'^publicities/(?P<pk>[0-9]+)/$', views.publicity_details),
    url(r'^helps/$', views.help_list),
    url(r'^helps/(?P<pk>[0-9]+)/$', views.help_details),
    url(r'^timetables/$', views.timetable_list),
    url(r'^timetables/(?P<pk>[0-9]+)/$', views.timetables_details),

]

urlpatterns = format_suffix_patterns(urlpatterns)

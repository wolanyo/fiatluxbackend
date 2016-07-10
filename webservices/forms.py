# -*- coding: utf-8 -*-

from django.forms import ModelForm
from suit_redactor.widgets import RedactorWidget


class PostForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'}),
            'content': RedactorWidget(editor_options={'lang': 'fr'}),
        }


class MultiMediaArchiveForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'}),
            'content': RedactorWidget(editor_options={'lang': 'fr'}),
        }


class ReflectForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'})
        }


class LessonForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'})
        }


class ChapterForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'}),
            'content': RedactorWidget(editor_options={'lang': 'fr'}),
        }


class DocumentForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'})
        }


class BookForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'})
        }


class CdDvdForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'})
        }


class PublicityForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'})
        }


class HelpForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'})
        }

class LessonTypeForm(ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'fr'}),
        }


class TimeTableForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'})
        }

class JokeForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'}),
            'content': RedactorWidget(editor_options={'lang': 'fr'}),
        }


class JokeStoryReflectForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'}),
            'content': RedactorWidget(editor_options={'lang': 'fr'}),
        }


class StrangeStorieForm(ModelForm):
    class Meta:
        widgets = {
            'excerpt': RedactorWidget(editor_options={'lang': 'fr'}),
            'content': RedactorWidget(editor_options={'lang': 'fr'}),
        }


class GroupForm(ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'fr'})
        }


class SaloonForm(ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'fr'})
        }


class MessageForm(ModelForm):
    class Meta:
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'fr'})
        }
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
#Post, Lesson, Chapter, Document, Book, CdDvd, LessonType, Group, UserGroup, UserSaloon, Message, Saloon
from .forms import *
from .notifications_services import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'mediaType', 'section', 'mediaURL', 'postDate', 'postTime', 'status', 'image')
    list_filter = ('mediaType', 'postDate', 'postTime', 'status')
    date_hierarchy = 'postDate'
    ordering = ('-postDate', '-postTime', 'title')
    search_fields = ('title', 'mediaType', 'postDate', 'mediaType')

    def save_model(self, request, obj, form, change):
        # custom stuff here
        message = "Nouvelle article : "+obj.title
        sendNotification(message)
        obj.save()


class LessonTypeAdmin(admin.ModelAdmin):
    form = LessonTypeForm
    list_display = ('label', 'description', 'position')
    list_filter = ('label', 'description', 'position')
    ordering = ('label', 'description', 'position')
    search_fields = ('label',)


class LessonAdmin(admin.ModelAdmin):
    form = LessonForm
    list_display = ('title', 'position', 'lessonType', 'status', 'image')
    list_filter = ('lessonType', 'status')
    ordering = ('position', 'title', 'image')
    search_fields = ('title', 'lessonType')


class ChapterAdmin(admin.ModelAdmin):
    form = ChapterForm
    list_display = ('title', 'position', 'lesson', 'status', 'image')
    list_filter = ('lesson', 'title', 'position')
    ordering = ('lesson', 'position', 'title', 'image')
    search_fields = ('title', 'lesson', 'lessonType')


class DocumentAdmin(admin.ModelAdmin):
    form = DocumentForm
    list_display = ('title', 'author', 'reference', 'price', 'status', 'image')
    list_filter = ('title', 'author', 'price')
    ordering = ('title', 'author', 'reference', 'price')
    search_fields = ('title', 'author', 'price')


class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ('title', 'section', 'author', 'reference', 'price', 'status', 'image')
    list_filter = ('author', 'status')
    ordering = ('title', 'author', 'reference', 'price')
    search_fields = ('title', 'author', 'price')
    # fields = ('image_tag',)
    # readonly_fields = ['image_tag']


class StrangeStorieAdmin(admin.ModelAdmin):
    form = StrangeStorieForm
    list_display = ('title', 'excerpt', 'status', 'image')
    list_filter = ('excerpt', 'status')
    ordering = ('title', 'excerpt', 'status', 'image')
    search_fields = ('title',)


class JokeAdmin(admin.ModelAdmin):
    form = JokeForm
    list_display = ('title', 'excerpt','status', 'image')
    list_filter = ('excerpt', 'status')
    ordering = ('title', 'excerpt', 'status', 'image')
    search_fields = ('title',)


class JokeStoryReflectAdmin(admin.ModelAdmin):
    form = JokeStoryReflectForm
    list_display = ('title', 'type', 'excerpt','status', 'image')
    list_filter = ('excerpt', 'status')
    ordering = ('title', 'excerpt', 'status', 'image')
    search_fields = ('title',)


class MultiMediaArchiveAdmin(admin.ModelAdmin):
    form = MultiMediaArchiveForm
    list_display = ('title', 'publishDate', 'archiveType', 'playerType', 'visibility', 'mediaURL', 'status', 'image')
    list_filter = ('archiveType', 'playerType', 'visibility', 'status')
    ordering = ('publishDate', 'title', 'archiveType', 'playerType', 'visibility', 'mediaURL', 'excerpt', 'status', 'image')
    search_fields = ('title',)


class ReflectAdmin(admin.ModelAdmin):
    form = ReflectForm
    list_display = ('title', 'excerpt', 'status', 'image')
    list_filter = ()
    ordering = ('title', 'excerpt', 'status', 'image')
    search_fields = ('title',)


class DonateAdmin(admin.ModelAdmin):
    list_display = ('civility', 'name', 'surname', 'amonth', 'dateDonate', 'timeDonate')
    list_filter = ('civility', 'dateDonate', 'timeDonate')
    ordering = ('civility', 'name', 'surname', 'dateDonate', 'timeDonate', 'amonth',)
    search_fields = ('civility', 'name', 'surname', 'amonth', 'dateDonate', 'timeDonate')


class PublicityAdmin(admin.ModelAdmin):
    form = PublicityForm
    list_display = ('title', 'mediaType', 'publicationDate', 'status', 'image')
    list_filter = ('mediaType', 'status')
    ordering = ('title', '-publicationDate')
    search_fields = ('title', 'mediaType')


class HelpAdmin(admin.ModelAdmin):
    form = HelpForm
    list_display = ('title', 'author', 'publicationDate', 'status', 'image')
    list_filter = ('status',)
    ordering = ('title', '-publicationDate')
    search_fields = ('title', 'author')


class TimeTableAdmin(admin.ModelAdmin):
    form = TimeTableForm
    list_display = ('title', 'eventDate', 'startTime', 'endTime', 'status', 'image')
    list_filter = ('status',)
    ordering = ('eventDate', 'startTime', 'title', 'image')
    search_fields = ('title', 'eventDate')

# ################################ADMIN#################################

class CdDvdAdmin(admin.ModelAdmin):
    form = CdDvdForm
    list_display = ('title', 'discType', 'section', 'author', 'duration', 'mediaURL', 'reference', 'price', 'status', 'image')
    list_filter = ('discType', 'author', 'status', 'reference')
    ordering = ('title', 'author', 'discType', 'reference', 'price')
    search_fields = ('title', 'author', 'price')


class GroupAdmin(admin.ModelAdmin):
    form = GroupForm
    list_display = ('title', 'description', 'dateCreation', 'timeCreation', 'status', 'image')
    list_filter = ('dateCreation', 'status',)
    ordering = ('title', 'dateCreation', 'timeCreation', 'status')
    search_fields = ('title', 'dateCreation', 'timeCreation', 'status')


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('user', 'group', 'dateCreation', 'timeCreation', 'status')
    list_filter = ('user', 'group', 'dateCreation', 'status')
    ordering = ('user', 'group', 'dateCreation', 'timeCreation', 'status')
    search_fields = ('user', 'group', 'dateCreation', 'status')


class SaloonAdmin(admin.ModelAdmin):
    form = SaloonForm
    list_display = ('title', 'description', 'dateCreation', 'timeCreation', 'status', 'image')
    list_filter = ('dateCreation', 'status',)
    ordering = ('title', 'dateCreation', 'timeCreation', 'status')
    search_fields = ('title', 'dateCreation', 'status')


class UserSaloonAdmin(admin.ModelAdmin):
    list_display = ('user', 'saloon', 'dateCreation', 'timeCreation', 'status')
    list_filter = ('user', 'saloon', 'dateCreation', 'status')
    ordering = ('user', 'saloon', 'dateCreation', 'timeCreation', 'status')
    search_fields = ('user', 'saloon', 'dateCreation', 'status')


class MessageAdmin(admin.ModelAdmin):
    form = MessageForm
    list_display = ('sender', 'receiver', 'sendDate', 'sendTime', 'content', 'status')
    list_filter = ('sender', 'receiver', 'sendDate')
    ordering = ('sender', 'receiver', 'sendDate', 'sendTime')
    search_fields = ('sender', 'receiver', 'sendDate')


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Utilisateurs'


# Define a new User admin
class UserProfileAdmin(UserAdmin):
    inlines = (UserProfileInline, )

admin.site.register(Post, PostAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Chapter, ChapterAdmin)
# admin.site.register(Document, DocumentAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(CdDvd, CdDvdAdmin)
admin.site.register(LessonType, LessonTypeAdmin)
admin.site.register(JokeStoryReflect, JokeStoryReflectAdmin)
admin.site.register(Joke, JokeAdmin)
admin.site.register(StrangeStorie, StrangeStorieAdmin)
admin.site.register(MultiMediaArchive, MultiMediaArchiveAdmin)
admin.site.register(Reflect, ReflectAdmin)
admin.site.register(Donate, DonateAdmin)
admin.site.register(Publicity, PublicityAdmin)
admin.site.register(Help, HelpAdmin)
admin.site.register(TimeTable, TimeTableAdmin)
#
admin.site.register(Group, GroupAdmin)
admin.site.register(Saloon, SaloonAdmin)
admin.site.register(UserGroup, UserGroupAdmin)
admin.site.register(UserSaloon, UserSaloonAdmin)
admin.site.register(Message, MessageAdmin)

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)

# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

SPIRITUALITY = 'SPIRITUALITY'
SELF_DEVELOPMENT = 'DEVELOPMENT'
NONE = "NONE"

SECTION_CHOICES = (
    (NONE, 'AUCUN'),
    (SPIRITUALITY, 'SPIRITUALITÉ'),
    (SELF_DEVELOPMENT, 'DEVELOPPEMENT PERSONNNEL'),
)


class Common(models.Model):
    title = models.CharField(max_length=200, default='', blank=False, null=False, verbose_name="Titre")
    section = models.CharField(max_length=30, choices=SECTION_CHOICES, default=SPIRITUALITY, blank=False,
                               verbose_name="Section")
    excerpt = models.TextField(max_length=2000, default='', blank=True, null=True, verbose_name="Résumé")
    image = models.ImageField(upload_to="images", verbose_name="Image illustrative", blank=True, null=True)
    status = models.BooleanField(default=True)

    def __unicode__(self):
        return u"{0} {1} ".format(self.title, self.excerpt)

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.title

    def image_tag(self):
        return '<img src="%s" />' % (self.image)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class CommonMedia(Common):
    TEXT = 'TEXT'
    AUDIO = 'AUDIO'
    VIDEO = 'VIDEO'

    MEDIA_TYPE_CHOICES = (
        (TEXT, 'TEXT'),
        (AUDIO, 'AUDIO'),
        (VIDEO, 'VIDEO'),
    )

    mediaType = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, default=TEXT, blank=True,
                                 verbose_name="Type de Média")


class Publicity(CommonMedia):
    publicationDate = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Date")

    class Meta:
        verbose_name = 'Publicité'
        verbose_name_plural = 'Publicités'


class TimeTable(Common):
    eventDate = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Date")
    startTime = models.TimeField(auto_now_add=False, auto_now=False, verbose_name="Heure de début")
    endTime = models.TimeField(auto_now_add=False, auto_now=False, verbose_name="Heure de fin")
    address = models.CharField(max_length=500, default='Siège du PARAM AKSHAR', blank=False, null=False,
                               verbose_name="Adresse")

    class Meta:
        verbose_name = 'Agenda'
        verbose_name_plural = 'Agendas'


class Help(Common):
    author = models.CharField(max_length=200, default='', blank=False, null=False, verbose_name="Auteur")
    publicationDate = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Date")

    class Meta:
        verbose_name = 'Aidons-nous'
        verbose_name_plural = 'Aidons-nous'


class MultiMediaArchive(Common):
    TVPROGRAM = 'TVPROGRAM'
    SEMINARY = 'SEMINARY'
    MUSIC = 'MUSIC'

    ARCHIVE_TYPE_CHOICES = (
        (TVPROGRAM, 'PROGRAMME TÉLÉ'),
        (SEMINARY, 'SEMINAIRE'),
        (MUSIC, 'MUSIQUE'),
    )

    YOUTUBE = 'YOUTUBE'
    DAILYMOTION = 'DAILYMOTION'

    PLAYER_TYPE_CHOICES = (
        (YOUTUBE, 'YOUTUBE'),
        (DAILYMOTION, 'DAILY MOTION'),
    )

    FREE = 'FREE'
    NON_FREE = 'NON_FREE'

    VISIBILITY_CHOICES = (
        (FREE, 'GRATUIT'),
        (NON_FREE, 'NON GRATUIT'),
    )
    publishDate = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date de publication")
    mediaURL = models.CharField(max_length=1000, default='', blank=False, null=True,
                                verbose_name="URL de la ressosurce")
    archiveType = models.CharField(max_length=10, choices=ARCHIVE_TYPE_CHOICES, default=TVPROGRAM, blank=True,
                                   verbose_name="Type de Ressource")
    playerType = models.CharField(max_length=10, choices=PLAYER_TYPE_CHOICES, default=YOUTUBE, blank=True,
                                  verbose_name="Lecteur")
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default=FREE, blank=True,
                                  verbose_name="Visibilité")


class Reflect(Common):
    class Meta:
        verbose_name = 'Graine à méditer'
        verbose_name_plural = 'Graines à méditer'


class Post(CommonMedia):
    postDate = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date de publication")
    postTime = models.TimeField(auto_now_add=True, auto_now=False, verbose_name="Heure de publication")
    content = models.TextField(verbose_name="Contenu")
    mediaURL = models.CharField(max_length=1000, default='', blank=True, null=True, verbose_name="URL de la ressosurce")

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __unicode__(self):
        return u"{0} {1} {2} {3} {4} {5}".format(self.title, self.excerpt, self.postDate, self.postTime, self.mediaType,
                                                 self.image)


class Joke(Common):
    content = models.TextField(verbose_name="Contenu")

    class Meta:
        verbose_name = 'Blague'
        verbose_name_plural = 'Blagues'

    def __unicode__(self):
        return u"{0} {1} {2} {3} {4} {5}".format(self.title, self.excerpt, self.image)


class JokeStoryReflect(Common):
    JOKE = 'BLAGUE'
    STORY = 'HISTOIRE'
    REFLECT = 'PENSEE'

    PUBLISH_TYPE_CHOICES = (
        (JOKE, 'BLAGUE'),
        (STORY, 'HISTOIRE'),
        (REFLECT, 'PENSEE'),
    )
    type = models.CharField(max_length=10, choices=PUBLISH_TYPE_CHOICES, default=JOKE, verbose_name="Type")
    content = models.TextField(verbose_name="Contenu")

    class Meta:
        verbose_name = 'Blague, Histoire, Pensé'
        verbose_name_plural = 'Blagues, Histoires, Pensés'

    def __unicode__(self):
        return u"{0} {1} {2} {3} {4} {5}".format(self.title, self.excerpt, self.image)


class StrangeStorie(Common):
    content = models.TextField(verbose_name="Contenu")

    class Meta:
        verbose_name = 'Histoire Etrange'
        verbose_name_plural = 'Histoires Etranges'

    def __unicode__(self):
        return u"{0} {1} {2} {3} {4} {5}".format(self.title, self.excerpt, self.image)


class LessonType(models.Model):
    label = models.CharField(max_length=100, default='', blank=False, null=False, verbose_name="Libelle")
    section = models.CharField(max_length=30, choices=SECTION_CHOICES, default=SPIRITUALITY, blank=False,
                               verbose_name="Section")
    description = models.TextField(max_length=500, default='', blank=True, null=True, verbose_name="Description")
    position = models.IntegerField(default=0, blank=True, null=True, verbose_name="Position")

    class Meta:
        verbose_name = 'Type de leçon'
        verbose_name_plural = 'Types de leçons'

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.label


class Lesson(CommonMedia):
    position = models.IntegerField(null=False, blank=False, default=0, verbose_name="Position")
    mediaURL = models.CharField(max_length=600, default='', blank=True, null=True, verbose_name="Media associé")
    lessonType = models.ForeignKey('LessonType', null=False, blank=False)

    class Meta:
        verbose_name = 'Leçon'
        verbose_name_plural = 'Leçons'

    def __unicode__(self):
        return u"{0}".format(self.title)
        # return u"{0} {1} {2} {3} {4}".format(self.title, self.excerpt, self.position, self.lessonType, self.image)


class Chapter(CommonMedia):
    content = models.TextField(verbose_name="Contenu")
    position = models.IntegerField(null=False, default=0, verbose_name="Position")
    lesson = models.ForeignKey('Lesson', null=False, blank=False)

    class Meta:
        verbose_name = 'Chapitre de leçon'
        verbose_name_plural = 'Chapitres des leçons'

    def __unicode__(self):
        return u"{0} {1} {2} {3} {4} {5}".format(self.title, self.excerpt, self.position, self.lesson.title,
                                                 self.mediaType, self.image)


class Document(Common):
    author = models.CharField(max_length=100, default='GODSON Elmancio', blank=True, null=True, verbose_name="Auteur")
    reference = models.CharField(max_length=100, default='ISBN', blank=True, null=True, verbose_name="Reference")
    price = models.IntegerField(null=False, default=0, verbose_name="Prix")

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Mes Documents'

    def __unicode__(self):
        return u"{0} {1} {2} {3}".format(self.title, self.author, self.reference, self.price, self.image)


class Book(Document):
    numberOfPage = models.IntegerField(null=True, blank=True, default=0, verbose_name="Nombre de page")
    excerptFile = models.FileField(upload_to='books', default='', blank=True, null=True,
                                   verbose_name="Extrait")
    file = models.FileField(upload_to='books', max_length=500, default='link', blank=True, null=True,
                            verbose_name="Fichier complet")

    class Meta:
        verbose_name = 'Livre'
        verbose_name_plural = 'Livres'


class CdDvd(Document):
    CD = 'CD'
    DVD = 'DVD'

    DISC_TYPE_CHOICES = (
        (CD, 'CD'),
        (DVD, 'DVD'),
    )
    duration = models.IntegerField(null=True, blank=True, default=0, verbose_name="Durée")
    discType = models.CharField(max_length=5, choices=DISC_TYPE_CHOICES, default=CD)
    mediaURL = models.CharField(max_length=1000, default='', blank=True, null=True,
                                verbose_name="URL de l'extrait")
    downloadLink = models.CharField(max_length=500, default='link', blank=True, null=True,
                                    verbose_name="URL de telechargement")

    class Meta:
        verbose_name = 'CD et DVD'
        verbose_name_plural = 'CDs et DVDs'


###################################ADMIN PART############################

FLOOZ = "FLOOZ"
TOGOCELL = "TOGOCELL"
CHRONOCASH = "CHRONOCASH"
CARD = "CARD"
PAYPAL = "PAYPAL"
PAYMENT_CHOICES = (
    (FLOOZ, 'FLOOZ'),
    (TOGOCELL, 'TOGOCELL'),
    (CHRONOCASH, 'CHRONOCASH'),
    (CARD, 'VISA / MASTERCARD / CARTE BLEU'),
    (PAYPAL, 'PAYPAL'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    class Meta:
        verbose_name = 'Utilisateur'
        # verbose_name_plural = 'Les Utilisateurs'

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.user.first_name


class Donate(models.Model):
    M = 'M'
    MLLE = 'Mlle'
    MME = 'Mme'

    CIVILITY_TYPE_CHOICES = (
        (M, 'M'),
        (MLLE, 'Mlle'),
        (MME, 'Mme'),
    )

    HOMME = 'Homme'
    FEMME = 'Femme'

    GENDER_TYPE_CHOICES = (
        (FEMME, 'Femme'),
        (HOMME, 'Homme'),
    )
    civility = models.CharField(max_length=10, blank=True, null=True, verbose_name="Civilité",
                                choices=CIVILITY_TYPE_CHOICES,
                                default=MLLE)
    name = models.CharField(max_length=100, default='', blank=False, null=True, verbose_name="Nom")
    surname = models.CharField(max_length=100, default='', blank=False, null=True, verbose_name="Prénom")
    amonth = models.IntegerField(null=False, blank=False, default=0, verbose_name="Montant du don")
    paymentType = models.CharField(max_length=50, blank=True, null=True, verbose_name="Type de Paiement",
                                   choices=PAYMENT_CHOICES,
                                   default=FLOOZ)
    dateDonate = models.DateField(auto_now_add=False, auto_now=False, verbose_name="Date du don")
    timeDonate = models.TimeField(auto_now_add=True, auto_now=False, verbose_name="Heure du don")

    class Meta:
        verbose_name = 'Don'
        verbose_name_plural = 'Dons'


class CommonGroup(models.Model):
    title = models.CharField(max_length=200, default='', blank=False, null=False, verbose_name="Titre")
    description = models.TextField(max_length=500, default='', blank=True, null=True, verbose_name="Description")
    image = models.ImageField(upload_to="images", verbose_name="Image", blank=True, null=True)
    status = models.BooleanField(default=False)
    dateCreation = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date de création")
    timeCreation = models.TimeField(auto_now_add=True, auto_now=False, verbose_name="Heure de création")

    class Meta:
        verbose_name = 'Groupe et membre'
        verbose_name_plural = 'Groupes et membre'


class UserLesson(models.Model):
    lesson = models.ForeignKey('Lesson', null=False, blank=False, verbose_name="Leçon")
    user = models.ForeignKey('UserProfile', null=False, blank=False, verbose_name="Utilisateur")
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Utilisateur et lesson'
        verbose_name_plural = 'Groupes et membre'

    def __unicode__(self):
        return u"{0} {1} {2} {3} {4}".format(self.group.title, self.user, self.dateCreation, self.timeCreation,
                                             self.status)


class Group(CommonGroup):
    class Meta:
        verbose_name = 'Groupe'
        verbose_name_plural = 'Groupes'


class UserGroup(models.Model):
    group = models.ForeignKey('Group', null=False, blank=False, verbose_name="Groupe")
    user = models.ForeignKey('UserProfile', null=False, blank=False, verbose_name="Utilisateur")
    dateCreation = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date de demande")
    timeCreation = models.TimeField(auto_now_add=True, auto_now=False, verbose_name="Heure de demande")
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Groupe et membre'
        verbose_name_plural = 'Groupes et membre'

    def __unicode__(self):
        return u"{0} {1} {2} {3} {4}".format(self.group.title, self.user, self.dateCreation, self.timeCreation,
                                             self.status)


class Saloon(CommonGroup):
    class Meta:
        verbose_name = 'Salon de Discussion'
        verbose_name_plural = 'Salons de discussion'


class UserSaloon(models.Model):
    saloon = models.ForeignKey('Saloon', null=False, blank=False, verbose_name="Salon de discussion")
    user = models.ForeignKey('UserProfile', null=False, blank=False, verbose_name="Utilisateur")
    dateCreation = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date")
    timeCreation = models.TimeField(auto_now_add=True, auto_now=False, verbose_name="Heure")
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Salon et Membre'
        verbose_name_plural = 'Salons et Membres'

    def __unicode__(self):
        return u"{0} {1} {2} {3} {4} ".format(self.saloon.title, self.user, self.dateCreation, self.timeCreation,
                                              self.status)

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.saloon.title + " " + self.user


class Message(models.Model):
    sender = models.ForeignKey('UserProfile', null=False, blank=False, related_name='message_sender',
                               verbose_name="Expediteur")
    receiver = models.ForeignKey('UserProfile', null=False, blank=False, related_name='message_receiver',
                                 verbose_name="Destinataire")
    sendDate = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date d'envoi")
    sendTime = models.TimeField(auto_now_add=True, auto_now=False, verbose_name="Heure d'envoi")
    content = models.TextField(verbose_name="Contenu")
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class Subscription(models.Model):
    BRONZE = 'BRONZE'
    SILVER = 'SILVER'
    GOLD = 'GOLD'

    SUBSCRIPTION_TYPE_CHOICES = (
        (BRONZE, 'BRONZE'),
        (SILVER, 'SILVER'),
        (GOLD, 'GOLD'),
    )
    users = models.ForeignKey('UserProfile', null=False, blank=False, verbose_name="Utilisateur")
    subscriptionDate = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date l'abonnement")
    subscriptionTime = models.TimeField(auto_now_add=True, auto_now=False, verbose_name="Heure de l'abonnement")
    duration = models.IntegerField(null=False, default=0, verbose_name="Durée de l'abonnement")
    expirationDate = models.DateField(auto_now_add=True, auto_now=False, verbose_name="Date d'expiration")
    subscriptionType = models.CharField(max_length=5, choices=SUBSCRIPTION_TYPE_CHOICES, default=BRONZE)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Abonnement'
        verbose_name_plural = 'Abonnements'

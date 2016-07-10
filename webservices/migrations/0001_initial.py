# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Common',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Titre', max_length=200, default='')),
                ('excerpt', models.TextField(blank=True, null=True, verbose_name='Résumé', max_length=500, default='')),
                ('image', models.ImageField(blank=True, null=True, verbose_name='Image', upload_to='images')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CommonGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Titre', max_length=200, default='')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description', max_length=500, default='')),
                ('image', models.ImageField(blank=True, null=True, verbose_name='Image', upload_to='images')),
                ('status', models.BooleanField(default=False)),
                ('dateCreation', models.DateField(verbose_name='Date de création', auto_now_add=True)),
                ('timeCreation', models.TimeField(verbose_name='Heure de création', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Groupe et membre',
                'verbose_name_plural': 'Groupes et membre',
            },
        ),
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('civility', models.CharField(choices=[('Femme', 'Femme'), ('Homme', 'Homme')], verbose_name='Sexe', blank=True, null=True, max_length=100, default='Mlle')),
                ('name', models.CharField(null=True, verbose_name='Nom', max_length=100, default='')),
                ('surname', models.CharField(null=True, verbose_name='Prénom', max_length=100, default='')),
                ('gender', models.CharField(choices=[('M', 'M'), ('Mlle', 'Mlle'), ('Mme', 'Mme')], verbose_name='Sexe', blank=True, null=True, max_length=100, default='Femme')),
                ('amonth', models.IntegerField(verbose_name='Montant du don', default=0)),
                ('dateDonate', models.DateField(verbose_name='Date du don', auto_now_add=True)),
                ('timeDonate', models.TimeField(verbose_name='Heure du don', auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Don',
                'verbose_name_plural': 'Dons',
            },
        ),
        migrations.CreateModel(
            name='LessonType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(verbose_name='Libelle', max_length=100, default='')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description', max_length=500, default='')),
                ('position', models.CharField(blank=True, null=True, verbose_name='Position', max_length=100, default='')),
            ],
            options={
                'verbose_name': 'Type de leçon',
                'verbose_name_plural': 'Les types de leçons',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sendDate', models.DateField(verbose_name="Date d'envoi", auto_now_add=True)),
                ('sendTime', models.TimeField(verbose_name="Heure d'envoi", auto_now_add=True)),
                ('content', models.TextField(verbose_name='Contenu')),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subscriptionDate', models.DateField(verbose_name="Date l'abonnement", auto_now_add=True)),
                ('subscriptionTime', models.TimeField(verbose_name="Heure de l'abonnement", auto_now_add=True)),
                ('duration', models.IntegerField(verbose_name="Durée de l'abonnement", default=0)),
                ('expirationDate', models.DateField(verbose_name="Date d'expiration", auto_now_add=True)),
                ('subscriptionType', models.CharField(choices=[('BRONZE', 'BRONZE'), ('SILVER', 'SILVER'), ('GOLD', 'GOLD')], max_length=5, default='BRONZE')),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Abonnement',
                'verbose_name_plural': 'Abonnements',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateCreation', models.DateField(verbose_name='Date de demande', auto_now_add=True)),
                ('timeCreation', models.TimeField(verbose_name='Heure de demande', auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Groupe et membre',
                'verbose_name_plural': 'Groupes et membre',
            },
        ),
        migrations.CreateModel(
            name='UserLesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Utilisateur et lesson',
                'verbose_name_plural': 'Groupes et membre',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Utilisateur',
            },
        ),
        migrations.CreateModel(
            name='UserSaloon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dateCreation', models.DateField(verbose_name='Date', auto_now_add=True)),
                ('timeCreation', models.TimeField(verbose_name='Heure', auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(verbose_name='Utilisateur', to='webservices.UserProfile')),
            ],
            options={
                'verbose_name': 'Salon et Membre',
                'verbose_name_plural': 'Salons et Membres',
            },
        ),
        migrations.CreateModel(
            name='CommonMedia',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webservices.Common')),
                ('mediaType', models.CharField(blank=True, choices=[('TEXT', 'TEXT'), ('AUDIO', 'AUDIO'), ('VIDEO', 'VIDEO')], verbose_name='Média', max_length=5, default='TEXT')),
            ],
            bases=('webservices.common',),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webservices.Common')),
                ('author', models.CharField(blank=True, null=True, verbose_name='Auteur', max_length=100, default='GODSON Elmancio')),
                ('reference', models.CharField(blank=True, null=True, verbose_name='Reference', max_length=100, default='ISBN')),
                ('price', models.IntegerField(verbose_name='Prix', default=0)),
                ('downloadLink', models.CharField(blank=True, null=True, verbose_name='Lien de telechargement', max_length=500, default='link')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Mes Documents',
            },
            bases=('webservices.common',),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('commongroup_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webservices.CommonGroup')),
            ],
            options={
                'verbose_name': 'Groupe',
                'verbose_name_plural': 'Groupes',
            },
            bases=('webservices.commongroup',),
        ),
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webservices.Common')),
                ('content', models.TextField(verbose_name='Contenu')),
            ],
            options={
                'verbose_name': 'Blague',
                'verbose_name_plural': 'Les Blagues',
            },
            bases=('webservices.common',),
        ),
        migrations.CreateModel(
            name='Saloon',
            fields=[
                ('commongroup_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webservices.CommonGroup')),
            ],
            options={
                'verbose_name': 'Salon de Discussion',
                'verbose_name_plural': 'Salons de discussion',
            },
            bases=('webservices.commongroup',),
        ),
        migrations.CreateModel(
            name='StrangeStorie',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webservices.Common')),
                ('content', models.TextField(verbose_name='Contenu')),
            ],
            options={
                'verbose_name': 'Histoire Etrange',
                'verbose_name_plural': 'Les Histoires Etranges',
            },
            bases=('webservices.common',),
        ),
        migrations.AddField(
            model_name='userlesson',
            name='user',
            field=models.ForeignKey(verbose_name='Utilisateur', to='webservices.UserProfile'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='user',
            field=models.ForeignKey(verbose_name='Utilisateur', to='webservices.UserProfile'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='users',
            field=models.ForeignKey(verbose_name='Utilisateur', to='webservices.UserProfile'),
        ),
        migrations.AddField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(verbose_name='Destinataire', to='webservices.UserProfile', related_name='message_receiver'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(verbose_name='Expediteur', to='webservices.UserProfile', related_name='message_sender'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('document_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webservices.Document')),
                ('numberOfPage', models.IntegerField(blank=True, null=True, verbose_name='Nombre de page', default=0)),
            ],
            options={
                'verbose_name': 'Livre',
                'verbose_name_plural': 'Les livres',
            },
            bases=('webservices.document',),
        ),
        migrations.CreateModel(
            name='CdDvd',
            fields=[
                ('document_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webservices.Document')),
                ('duration', models.IntegerField(blank=True, null=True, verbose_name='Durée', default=0)),
                ('discType', models.CharField(choices=[('CD', 'CD'), ('DVD', 'DVD')], max_length=5, default='CD')),
            ],
            options={
                'verbose_name': 'CD et DVD',
                'verbose_name_plural': 'CDs et DVDs',
            },
            bases=('webservices.document',),
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('commonmedia_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webservices.CommonMedia')),
                ('content', models.TextField(verbose_name='Contenu')),
                ('position', models.IntegerField(verbose_name='Position', default=0)),
            ],
            options={
                'verbose_name': 'Chapitre de leçon',
                'verbose_name_plural': 'Les Chapitres des leçons',
            },
            bases=('webservices.commonmedia',),
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('commonmedia_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webservices.CommonMedia')),
                ('position', models.IntegerField(verbose_name='Position', default=0)),
                ('mediaURL', models.CharField(blank=True, null=True, verbose_name='Media associé', max_length=600, default='')),
                ('lessonType', models.ForeignKey(to='webservices.LessonType')),
            ],
            options={
                'verbose_name': 'Leçon',
                'verbose_name_plural': 'Les leçons',
            },
            bases=('webservices.commonmedia',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('commonmedia_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webservices.CommonMedia')),
                ('postDate', models.DateField(verbose_name='Date de publication', auto_now_add=True)),
                ('postTime', models.TimeField(verbose_name='Heure de publication', auto_now_add=True)),
                ('content', models.TextField(verbose_name='Contenu')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Les Articles',
            },
            bases=('webservices.commonmedia',),
        ),
        migrations.AddField(
            model_name='usersaloon',
            name='saloon',
            field=models.ForeignKey(verbose_name='Salon de discussion', to='webservices.Saloon'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='group',
            field=models.ForeignKey(verbose_name='Groupe', to='webservices.Group'),
        ),
        migrations.AddField(
            model_name='userlesson',
            name='lesson',
            field=models.ForeignKey(verbose_name='Leçon', to='webservices.Lesson'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='lesson',
            field=models.ForeignKey(to='webservices.Lesson'),
        ),
    ]

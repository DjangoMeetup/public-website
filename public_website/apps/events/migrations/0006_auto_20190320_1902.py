# Generated by Django 2.1.4 on 2019-03-20 09:02

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('events', '0005_events_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('details', models.CharField(blank=True, max_length=1500, null=True)),
                ('main_user_group', models.ManyToManyField(blank=True, default='None', related_name='group_user', to=settings.AUTH_USER_MODEL)),
                ('organisor_group', models.ManyToManyField(blank=True, default='None', related_name='group_organisor', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='EventGroupOld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='Event Group', max_length=200, unique=True)),
                ('details', models.CharField(blank=True, max_length=1500, null=True)),
                ('main_user_group', models.ManyToManyField(blank=True, default='None', related_name='group_user_old', to=settings.AUTH_USER_MODEL)),
                ('organisor_group', models.ManyToManyField(blank=True, default='None', related_name='group_organisor_old', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'events',
            },
        ),
        migrations.RemoveField(
            model_name='eventgroups',
            name='main_user_group',
        ),
        migrations.RemoveField(
            model_name='eventgroups',
            name='organisor_group',
        ),
        migrations.AlterField(
            model_name='events',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.EventGroupOld'),
        ),
        migrations.DeleteModel(
            name='EventGroups',
        ),
    ]

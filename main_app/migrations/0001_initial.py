# Generated by Django 3.0.4 on 2020-03-22 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('infected', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('recovered', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Global',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('infected', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('recovered', models.IntegerField()),
                ('last_updated', models.CharField(max_length=100)),
                ('china_infected', models.IntegerField()),
                ('china_deaths', models.IntegerField()),
                ('china_recovered', models.IntegerField()),
                ('nonchina_infected', models.IntegerField()),
                ('nonchina_deaths', models.IntegerField()),
                ('nonchina_recovered', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('infected', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('recovered', models.IntegerField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted_at', models.DateTimeField()),
                ('content', models.TextField(max_length=250)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Country')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

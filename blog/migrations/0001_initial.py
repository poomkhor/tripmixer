# Generated by Django 5.0.1 on 2024-02-03 04:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('planner', '0002_alter_destination_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, default='', max_length=1000)),
                ('create_date', models.DateTimeField()),
                ('is_public', models.BooleanField(default=False)),
                ('destination', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='planner.destination')),
                ('holiday', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='planner.holiday')),
                ('itinerary', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='planner.itinerary')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImageURL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('create_date', models.DateTimeField()),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.post')),
            ],
        ),
    ]
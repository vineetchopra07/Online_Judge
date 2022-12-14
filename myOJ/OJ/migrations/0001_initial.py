# Generated by Django 4.0.5 on 2022-07-11 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_name', models.CharField(max_length=100)),
                ('prob_desc', models.CharField(max_length=10000)),
                ('prob_diff', models.CharField(max_length=50)),
                ('score', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User_score',
            fields=[
                ('user_Id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('score', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Test_cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=10000)),
                ('output', models.CharField(max_length=10000)),
                ('probId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OJ.problem')),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestrap', models.DateTimeField(auto_now_add=True)),
                ('verdict', models.CharField(default='NOT SOLVED', max_length=10)),
                ('probId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OJ.problem')),
                ('user_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

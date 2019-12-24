# Generated by Django 2.2.4 on 2019-08-23 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('msg', models.TextField()),
            ],
        ),
    ]
# Generated by Django 2.2.4 on 2019-08-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('deg', models.CharField(max_length=20)),
                ('des', models.CharField(max_length=30)),
                ('img', models.ImageField(blank=True, null=True, upload_to='image')),
            ],
        ),
    ]

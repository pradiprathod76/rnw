# Generated by Django 2.2.5 on 2019-09-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('deg', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='image')),
            ],
        ),
    ]

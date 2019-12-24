# Generated by Django 2.2.5 on 2019-09-14 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('p_type', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='image')),
            ],
        ),
    ]
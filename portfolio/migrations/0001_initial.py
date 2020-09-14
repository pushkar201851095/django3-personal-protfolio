# Generated by Django 3.0.7 on 2020-08-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('disription', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]

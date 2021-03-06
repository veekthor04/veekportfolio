# Generated by Django 3.0.5 on 2020-05-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veekprojects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='projects/%Y/%m/%d')),
                ('last_updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Projects',
        ),
    ]

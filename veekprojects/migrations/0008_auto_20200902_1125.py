# Generated by Django 2.1.15 on 2020-09-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veekprojects', '0007_auto_20200519_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]

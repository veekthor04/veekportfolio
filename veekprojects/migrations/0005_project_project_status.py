# Generated by Django 2.2.10 on 2020-05-19 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veekprojects', '0004_project_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.CharField(choices=[('pending', 'pending'), ('complete', 'complete'), ('aborted', 'aborted')], default='complete', max_length=9),
        ),
    ]

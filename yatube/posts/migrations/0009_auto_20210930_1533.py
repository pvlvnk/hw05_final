# Generated by Django 2.2.16 on 2021-09-30 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210930_0027'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='user is not author',
        ),
    ]

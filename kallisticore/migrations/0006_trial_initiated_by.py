# Generated by Django 2.1.2 on 2019-05-21 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kallisticore', '0005_trial_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='trial',
            name='initiated_by',
            field=models.CharField(default='unknown', max_length=7),
        ),
    ]

# Generated by Django 4.1 on 2022-09-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainingapps', '0004_alter_responselog_query_params'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2022-08-06'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default='2022-08-06'),
            preserve_default=False,
        ),
    ]

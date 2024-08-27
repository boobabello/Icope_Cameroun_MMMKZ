# Generated by Django 5.1 on 2024-08-25 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icope', '0006_alter_questionnaire_cognition_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='audition',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='cognition',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='mobilite',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='nutrition',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='santePsychique',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='vision',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0),
        ),
    ]

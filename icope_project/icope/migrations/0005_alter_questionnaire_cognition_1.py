# Generated by Django 5.1 on 2024-08-24 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icope', '0004_alter_questionnaire_audition_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='cognition_1',
            field=models.IntegerField(null=True, verbose_name='Avez-vous des problèmes de mémoire ou d’orientation ?'),
        ),
    ]

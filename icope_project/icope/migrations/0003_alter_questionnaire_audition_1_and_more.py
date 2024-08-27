# Generated by Django 5.1 on 2024-08-21 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icope', '0002_alter_questionnaire_audition_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='audition_1',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name='Audition oreille droite'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='audition_2',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name='Audition oreille gauche'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='audition_3',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name="Baisse d'audition"),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='cognition_1',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name='Avez-vous des problèmes de mémoire ou d’orientation ?'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='cognition_2',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name='Avez-vous constaté une aggravation de ces problèmes ?'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='cognition_3',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name='Quelle est la date complète d’aujourd’hui ?'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='mobilite_1',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name='Levers de chaise 14s'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='nutrition_1',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name='Perte de poids involontaire'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='nutrition_2',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name="Perte d'appétit"),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='santePsychique_1',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name='Sentiment de déprime'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='santePsychique_2',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name="Manque d'intérêt"),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='vision_1',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name="Problèmes de vue ou maladies de l'œil"),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='vision_2',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name='Consultation ophtalmologue'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='vision_3',
            field=models.BooleanField(choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name='Baisse de vue'),
        ),
    ]

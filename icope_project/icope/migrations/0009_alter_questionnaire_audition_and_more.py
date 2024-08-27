# Generated by Django 5.1 on 2024-08-25 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icope', '0008_remove_questionnaire_numero_questionnaire_statut_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='audition',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Capacité auditive atteinte'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='audition_1',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Audition oreille droite'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='audition_2',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Audition oreille gauche'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='audition_3',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name="Baisse d'audition"),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='cognition',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Capacité cognitive atteinte'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='cognition_1',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Avez-vous des problèmes de mémoire ou d’orientation ?'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='cognition_2',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Avez-vous constaté une aggravation de ces problèmes ?'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='cognition_3',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Quelle est la date complète d’aujourd’hui ?'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='mobilite',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Capacité de mobilité atteinte'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='mobilite_1',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Levers de chaise 14s'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='nutrition',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Capacité nutritionnelle atteinte'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='nutrition_1',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Perte de poids involontaire'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='nutrition_2',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name="Perte d'appétit"),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='santePsychique',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Capacité de santé psychique atteinte'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='santePsychique_1',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Sentiment de déprime'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='santePsychique_2',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name="Manque d'intérêt"),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='vision',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Capacité visuelle atteinte'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='vision_1',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name="Problèmes de vue ou maladies de l'œil"),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='vision_2',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Consultation ophtalmologue'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='vision_3',
            field=models.IntegerField(choices=[(1, 'OUI'), (0, 'NON')], default=0, verbose_name='Baisse de vue'),
        ),
    ]

# Generated by Django 5.1 on 2024-08-27 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icope', '0011_questionnaire_audiometrie_score_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionnaire',
            name='audiometrie_score',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='conditions_nutrition',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='gpcog_score',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='maladie_aigue_3_mois',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='mna_score',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='phq9_score',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='q401',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='q409',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='q410',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='q411',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='q413',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='score_depistage_nutritionnel',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='snellen_score',
        ),
        migrations.RemoveField(
            model_name='questionnaire',
            name='sppb_score',
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='a_audiometrie_score',
            field=models.IntegerField(blank=True, choices=[(0, 'Audition normale (<35 dB)'), (1, 'Perte modérée-sévère (35-80 dB)'), (2, 'Surdité (>81 dB)')], null=True, verbose_name="Quel est le score de l’évaluation\xa0 d'audiometrie?"),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='age_interval',
            field=models.IntegerField(choices=[(1, '55-60 ans'), (2, '60-65 ans'), (3, '65-70 ans'), (4, '70-75 ans'), (5, '+75 ans')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='c_gpcog_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='Score total du test de Cognition GPCOG'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='c_recit_event',
            field=models.IntegerField(blank=True, choices=[(1, 'Correct'), (0, 'Incorrect')], null=True, verbose_name='Pouvez-vous me raconter ce qui s’est passé récemment aux informations (journaux, télévision) ?'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='m_lever_chaise',
            field=models.IntegerField(blank=True, choices=[(0, 'Non réalisable'), (1, '>16.70s'), (2, '13.70-16.69s'), (3, '11.20-13.69s'), (4, '≤11.19s')], null=True, verbose_name='Test de lever de chaise\xa0: Le patient croise les bras et se lève de la chaise 5 fois'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='m_sppb_score',
            field=models.IntegerField(blank=True, choices=[(1, 'SPPB Score 10-12 : Mobilité normale'), (2, 'SPPB Score 7-9 : Perte modérée de la mobilité'), (3, 'SPPB Score 0-6 : Altération sévère de la mobilité')], null=True, verbose_name='Quel est le score total du test de motricite SPPB ?'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='n_conditions_nutrition',
            field=models.IntegerField(blank=True, choices=[(0, 'Nécessite une assistance'), (1, 'Se nourrit seul avec difficulté'), (2, 'Se nourrit seul sans difficulté')], null=True, verbose_name='Dans quelles conditions vous nourrissez-vous\xa0?'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='n_maladie_aigue',
            field=models.IntegerField(blank=True, choices=[(1, 'OUI'), (0, 'NON')], null=True, verbose_name='Avez-vous eu une maladie aiguë ou stress psychologique au cours des 3 derniers mois ?'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='n_mna_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='Appréciation de l’état nutritionnel (max 30)'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='n_score_depistage_nutritionnel',
            field=models.IntegerField(blank=True, choices=[(0, '12-14 points'), (1, '8-11 points'), (2, '0-7 points')], null=True, verbose_name='Quel est le score de dépistage\xa0?'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='sp_etat_sommeil',
            field=models.IntegerField(blank=True, choices=[(0, 'Jamais'), (1, 'Plusieurs jours'), (2, 'Plus de la moitié du temps'), (3, 'Presque tous les jours')], null=True, verbose_name='Difficultés à s’endormir ou à rester endormi(e), ou dormir trop'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='sp_pense_mort',
            field=models.IntegerField(blank=True, choices=[(0, 'Jamais'), (1, 'Plusieurs jours'), (2, 'Plus de la moitié du temps'), (3, 'Presque tous les jours')], null=True, verbose_name='Penser qu’il vaudrait mieux mourir ou envisager de vous faire du mal d’une manière ou d’une autre'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='sp_phq9_score',
            field=models.IntegerField(blank=True, choices=[(0, 'Pas de trouble de l’humeur'), (1, '1-2 symptômes, A risque'), (2, 'Dépression, >3 symptômes')], null=True, verbose_name='Quel est le score total\xa0? de la sante psychique'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='sp_trouble_sommeil',
            field=models.IntegerField(blank=True, choices=[(0, 'Durée'), (1, 'Qualité'), (2, 'Régularité')], null=True, verbose_name='De quel ordre est le trouble\xa0de sommeil ?'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='v_snellen_score',
            field=models.IntegerField(blank=True, choices=[(1, 'Pas de déficience visuelle'), (2, 'Déficience visuelle')], null=True, verbose_name='Quel est le score total\xa0 du test de Snellen?'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='statut',
            field=models.IntegerField(choices=[(1, 'Veteran'), (2, 'Autre')]),
        ),
    ]

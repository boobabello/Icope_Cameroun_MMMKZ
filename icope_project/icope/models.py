from django.db import models
from datetime import date

# Create your models here.

from django.db import models

class Questionnaire(models.Model):
    SEXE_CHOICES = [
        (1, 'Masculin'),
        (2, 'Féminin'),
    ]

    AGE_CHOICES = [
        (1, '55-60 ans'),
        (2, '60-65 ans'),
        (3, '65-70 ans'),
        (4, '70-75 ans'),
        (5, '+75 ans'),
    ]
    
    STATUT_MATRIMONIAL_CHOICES = [
        (1, 'Célibataire'),
        (2, 'Mariée'),
        (3, 'Divorcée'),
        (4, 'Veuve'),
        (5, 'Union libre'),
    ]
    
    NIVEAU_ETUDE_CHOICES = [
        (1, 'Aucun'),
        (2, 'Primaire'),
        (3, 'Secondaire'),
        (4, 'Supérieur'),
    ]
    
    ACTIVITE_PARALLELE_CHOICES = [
        (1, 'Non'),
        (2, 'Oui'),
    ]
    
    REVENU_CHOICES = [
        (1, 'SMIC'),
        (2, '2SMIC'),
        (3, '3SMIC'),
        (4, '4SMIC'),
        (5, '+4SMIC'),
    ]

    ETHNIE_CHOICES = [
        (1, 'Bantous'),
        (2, 'Semi-bantous'),
        (3, 'Soudanais'),
    ]
    
    RELIGION_CHOICES = [
        (1, 'Chrétienne'),
        (2, 'Musulmane'),
        (3, 'Animiste'),
        (4, 'Autres'),
    ]
    
    RESIDENCE_CHOICES = [
        (1, 'Urbaine'),
        (2, 'Rurale'),
    ]
    
    MISE_HORS_SERVICE_CHOICES = [
        (1, 'Médicale'),
        (2, 'Volontaire'),
        (3, 'Limite d’âge'),
        (4, 'Involontaire'),
    ]
    
    GRADE_ACTUEL_CHOICES = [
        (1, 'Soldat'),
        (2, 'Militaire de rang'),
        (3, 'Sous-officier'),
        (4, 'Officier subalterne'),
        (5, 'Officier supérieur'),
    ]

    ANNEES_SERVICE_CHOICES = [
        (1, '<5 ans'),
        (2, '5-15 ans'),
        (3, '15-35 ans'),
        (4, '>35 ans'),
    ]
    
    CORPS_ARMEE_CHOICES = [
        (1, 'Armée de terre'),
        (2, 'Armée de l’Air'),
        (3, 'Gendarmerie Nationale'),
        (4, 'Marine nationale'),
        (5, 'Garde Présidentielle'),
        (6, 'BIR'),
    ]
    
    IMC_CHOICES = [
        (1, 'Moins de 18,5'),
        (2, '18,5-24,99'),
        (3, '25-29,99'),
        (4, '30-34,99'),
        (5, '35-39,99'),
        (6, '40 et plus'),
    ]
    
    PRESSION_ARTERIELLE_CHOICES = [
        (1, '<139/89'),
        (2, '140/90-159/99'),
        (3, '160/100-179/109'),
        (4, '>=180/110'),
    ]
    
    GLYCEMIE_CHOICES = [
        (1, '- de 0,60'),
        (2, '0,70-1,10'),
        (3, '1,10-1,26'),
        (4, '+ de 1,26'),
    ]
    
    TEST_VIH_CHOICES = [
        (1, 'Négatif'),
        (2, 'Positif'),
    ]
    
    date = models.DateField(default=date.today, blank=False, null=False)
    numero = models.CharField(max_length=50, blank=False, null=False)
    # Variables socio-démographiques
    sexe = models.IntegerField(choices=SEXE_CHOICES)
    age = models.IntegerField(choices=AGE_CHOICES)
    statut_matrimonial = models.IntegerField(choices=STATUT_MATRIMONIAL_CHOICES)
    niveau_etude = models.IntegerField(choices=NIVEAU_ETUDE_CHOICES)
    activite_parallele = models.IntegerField(choices=ACTIVITE_PARALLELE_CHOICES)
    revenu_mensuel = models.IntegerField(choices=REVENU_CHOICES)
    ethnie = models.IntegerField(choices=ETHNIE_CHOICES)
    religion = models.IntegerField(choices=RELIGION_CHOICES)
    residence = models.IntegerField(choices=RESIDENCE_CHOICES)
    mise_hors_service = models.IntegerField(choices=MISE_HORS_SERVICE_CHOICES)
    grade_actuel = models.IntegerField(choices=GRADE_ACTUEL_CHOICES)
    annees_service = models.IntegerField(choices=ANNEES_SERVICE_CHOICES)
    corps_armee = models.IntegerField(choices=CORPS_ARMEE_CHOICES)
    # Variables anthropométriques et biologiques
    poids = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    taille = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    imc = models.IntegerField(choices=IMC_CHOICES)
    pression_arterielle = models.IntegerField(choices=PRESSION_ARTERIELLE_CHOICES)
    glycemie = models.IntegerField(choices=GLYCEMIE_CHOICES)
    test_vih = models.IntegerField(choices=TEST_VIH_CHOICES)
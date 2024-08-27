# Définition des variables pour les choix
STATUS_CHOICES = [
    (1, 'Veteran'),
    (2, 'Autre'),
]
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

TEST_HEPATITE_CHOICES = [
    (1, 'Négatif'),
    (2, 'Positif'),
]

CHOIX_OUI_NON = [
    (1, 'OUI'),
    (0, 'NON')
]

CHOIX_CORRECT_INCORRECT = [
    (1, 'Correct'),
    (0, 'Incorrect')
]

CHOIX_SCORE_DEPISTAGE = [
    (0, '12-14 points'),
    (1, '8-11 points'),
    (2, '0-7 points')
]

CHOIX_CONDITIONS_NUTRITION = [
    (0, 'Nécessite une assistance'),
    (1, 'Se nourrit seul avec difficulté'),
    (2, 'Se nourrit seul sans difficulté')
]

CHOIX_SNELLEN_SCORE = [
    (1, 'Pas de déficience visuelle'),
    (2, 'Déficience visuelle')
]

CHOIX_AUDIOMETRIE_SCORE = [
    (0, 'Audition normale (<35 dB)'),
    (1, 'Perte modérée-sévère (35-80 dB)'),
    (2, 'Surdité (>81 dB)')
]

CHOIX_Q409 = [
    (0, 'Jamais'),
    (1, 'Plusieurs jours'),
    (2, 'Plus de la moitié du temps'),
    (3, 'Presque tous les jours')
]

CHOIX_Q410 = [
    (0, 'Durée'),
    (1, 'Qualité'),
    (2, 'Régularité')
]

CHOIX_PHQ9_SCORE = [
    (0, 'Pas de trouble de l’humeur'),
    (1, '1-2 symptômes, A risque'),
    (2, 'Dépression, >3 symptômes')
]

CHOIX_Q413 = [
    (0, 'Non réalisable'),
    (1, '>16.70s'),
    (2, '13.70-16.69s'),
    (3, '11.20-13.69s'),
    (4, '≤11.19s')
]

CHOIX_SPPB_SCORE = [
    (1, 'SPPB Score 10-12 : Mobilité normale'),
    (2, 'SPPB Score 7-9 : Perte modérée de la mobilité'),
    (3, 'SPPB Score 0-6 : Altération sévère de la mobilité')
]
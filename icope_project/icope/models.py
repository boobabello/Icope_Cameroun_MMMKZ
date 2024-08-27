from django.db import models
from datetime import date
from .choices import*

# Create your models here.
class Questionnaire(models.Model):
    # Champs du formulaire d'enregistrement
        # Variables socio-démographiques
    date = models.DateField(default=date.today, blank=False, null=False)
    statut = models.IntegerField(choices=STATUS_CHOICES)
    sexe = models.IntegerField(choices=SEXE_CHOICES)
    age = models.IntegerField()
    age_interval = models.IntegerField(choices=AGE_CHOICES)
    statut_matrimonial = models.IntegerField(choices=STATUT_MATRIMONIAL_CHOICES)
    niveau_etude = models.IntegerField(choices=NIVEAU_ETUDE_CHOICES)
    activite_parallele = models.IntegerField(choices=ACTIVITE_PARALLELE_CHOICES)
    revenu_mensuel = models.IntegerField(choices=REVENU_CHOICES, blank=True, null=True)
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
    test_hepatite = models.IntegerField(choices=TEST_HEPATITE_CHOICES)

    # Champs pour le formulaire ICOPE1
        # Cognition
    cognition_1 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Avez-vous des problèmes de mémoire ou d’orientation (comme ne pas savoir où l’on est ou quel jour on est ?", null=True)
    cognition_2 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Si oui, avez-vous constaté une aggravation de ces problèmes au cours des 6 derniers mois ou depuis la dernière évaluation ? ", null=True)
    cognition_3 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Si oui, Quelle est la date complète d’aujourd’hui ?", null=True)
            # Nutrition
    nutrition_1 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Avez-vous perdu involontairement plus de 3kg au cours de 3 derniers mois ?", null=True)
    nutrition_2 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Avez-vous perdu de l’appétit récemment ?", null=True)
        # Vision
    vision_1 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Avez-vous des problèmes de vue : difficultés pour voir de loin ou pour lire (avec vos lunettes si vous en portez). Avez-vous des maladies de l’œil ? Avez-vous un traitement pour une hypertension artérielle ou un diabète ?", null=True)
    vision_2 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Si oui, Avez-vous consulté un ophtalmologue durant les 12 derniers mois ?", null=True)
    vision_3 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Si oui, Avez-vous l’impression que votre vue a baissé, avec ou sans vos lunettes, au cours des 6 derniers mois ou depuis votre dernière évaluation ?", null=True)
        # Audition
    audition_1 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Se mettre derrière le sujet (à distance d’un bras ou à environ 0,6 m) pour qu’il ne puisse pas lire sur les lèvres. Demander-lui de placer un doigt sur le tragus de l'oreille gauche pour obscurcir le son. Chuchoter (maison, matin), La personne a-t-elle pu répéter tous les mots Pour l’oreille droite :", null=True)
    audition_2 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Pour l’oreille gauche :", null=True)
    audition_3 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Est-ce que vous ou votre entourage avez l’impression que votre audition a baissé au cours des 6 derniers mois ou depuis votre dernière évaluation ? ", null=True)
        # Santé psychique
    santePsychique_1 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Au cours des deux dernières semaines, vous êtes-vous senti déprimé ou sans espoir ?", null=True)
    santePsychique_2 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Au cours des deux dernières semaines, avez-vous trouvé peu d'intérêt ou de plaisir à faire les choses ?", null=True)
        # Mobilité
    mobilite_1 = models.IntegerField(choices=CHOIX_OUI_NON, verbose_name="Demander au sujet de se lever d’une chaise 5 fois de suite, le plus vite possible, les bras croisés sur la poitrine. Le sujet a-t-il réalisé les 5 levers de chaise ? ", null=True)
        
        # Resultats icope1
    cognition = models.IntegerField(choices=CHOIX_OUI_NON, default=0, verbose_name='Capacité COGNITIVE atteinte ?')
    nutrition = models.IntegerField(choices=CHOIX_OUI_NON, default=0, verbose_name='Capacité NUTRITIONNELLE atteinte ?')
    vision = models.IntegerField(choices=CHOIX_OUI_NON, default=0, verbose_name='Capacité VISUELLE atteinte')
    audition = models.IntegerField(choices=CHOIX_OUI_NON, default=0, verbose_name='Capacité AUDITIVE atteinte')
    santePsychique = models.IntegerField(choices=CHOIX_OUI_NON, default=0, verbose_name='SANTE PSYCHIQUE atteinte')
    mobilite = models.IntegerField(choices=CHOIX_OUI_NON, default=0, verbose_name='MOBILITE atteinte')

    #Champs pour le formulaire ICOPE2
        #Cognition
    c_recit_event = models.IntegerField(choices=CHOIX_CORRECT_INCORRECT, verbose_name="COGNITION - Pouvez-vous me raconter ce qui s’est passé récemment aux informations (journaux, télévision) ?", null=True, blank=True)
    c_gpcog_score = models.IntegerField(verbose_name="COGNITION - Score total du test de Cognition GPCOG", null=True, blank=True)
        #Nutrition
    n_maladie_aigue = models.IntegerField(choices=CHOIX_OUI_NON,verbose_name="NUTRITION - Avez-vous eu une maladie aiguë ou stress psychologique au cours des 3 derniers mois ?", null=True, blank=True)
    n_score_depistage_nutritionnel = models.IntegerField(choices=CHOIX_SCORE_DEPISTAGE, verbose_name="NUTRITION - Quel est le score de dépistage ?", null=True, blank=True)
    n_conditions_nutrition = models.IntegerField(choices=CHOIX_CONDITIONS_NUTRITION, verbose_name="NUTRITION -Dans quelles conditions vous nourrissez-vous ?", null=True, blank=True)
    n_mna_score = models.IntegerField(verbose_name="NUTRITION - Appréciation de l’état nutritionnel (max 30)", null=True, blank=True)
        #Vision
    v_snellen_score = models.IntegerField(choices=CHOIX_SNELLEN_SCORE, verbose_name="VISION - Quel est le score total  du test de Snellen?", null=True, blank=True)
        # Audition
    a_audiometrie_score = models.IntegerField(choices=CHOIX_AUDIOMETRIE_SCORE, verbose_name="AUDITION - Quel est le score de l’évaluation  d'audiometrie?", null=True, blank=True)
        # Santé psychique
    sp_etat_sommeil = models.IntegerField(choices=CHOIX_Q409,verbose_name="SANTé PSYCHIQUE - Difficultés à s’endormir ou à rester endormi(e), ou dormir trop", null=True, blank=True)
    sp_trouble_sommeil = models.IntegerField(choices=CHOIX_Q410,verbose_name="SANTé PSYCHIQUE - De quel ordre est le trouble de sommeil ?", null=True, blank=True)
    sp_pense_mort = models.IntegerField(choices=CHOIX_Q409,verbose_name="SANTé PSYCHIQUE - Penser qu’il vaudrait mieux mourir ou envisager de vous faire du mal d’une manière ou d’une autre", null=True, blank=True)
    sp_phq9_score = models.IntegerField(choices=CHOIX_PHQ9_SCORE,verbose_name="SANTé PSYCHIQUE - Quel est le score total ? de la sante psychique", null=True, blank=True)
        # Mobilité
    m_lever_chaise = models.IntegerField(choices=CHOIX_Q413, verbose_name="MOBILITé - Test de lever de chaise : Le patient croise les bras et se lève de la chaise 5 fois", null=True, blank=True)
    m_sppb_score = models.IntegerField(choices=CHOIX_SPPB_SCORE, verbose_name="MOBILITé - Quel est le score total du test de motricite SPPB ?", null=True, blank=True)
    
    def __str__(self):
        return f"Questionnaire {self.id}"
    

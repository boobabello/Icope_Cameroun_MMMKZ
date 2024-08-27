from django import forms
from .models import Questionnaire
from .choices import*

class BaseQuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = '__all__'

class EnregistrementForm(forms.ModelForm):
    class Meta(BaseQuestionnaireForm.Meta):
        fields = [
            'date',
            'statut', 'sexe', 'age', 'age_interval', 'statut_matrimonial', 'niveau_etude',
            'activite_parallele', 'revenu_mensuel',
            'ethnie', 'religion', 'residence',
            'mise_hors_service',
            'grade_actuel', 'annees_service', 'corps_armee',
            'poids', 'taille', 'imc', 'pression_arterielle', 'glycemie', 'test_vih','test_hepatite',
        ]

class ICOPE1Form(forms.ModelForm):
    class Meta(BaseQuestionnaireForm.Meta):
        fields=[
        'cognition_1', 'cognition_2', 'cognition_3', 'cognition',
        'nutrition_1', 'nutrition_2', 'nutrition', 
        'vision_1', 'vision_2', 'vision_3', 'vision',
        'audition_1', 'audition_2', 'audition_3', 'audition',
        'santePsychique_1', 'santePsychique_2', 'santePsychique',
        'mobilite_1', 'mobilite',
    ]
        
class ICOPE2Form(forms.ModelForm):
    class Meta(BaseQuestionnaireForm.Meta):
        fields = [
        'c_recit_event',
        'c_gpcog_score',
        'n_maladie_aigue',
        'n_score_depistage_nutritionnel',
        'n_conditions_nutrition',
        'n_mna_score',
        'v_snellen_score',
        'a_audiometrie_score',
        'sp_etat_sommeil',
        'sp_trouble_sommeil',
        'sp_pense_mort',
        'sp_phq9_score',
        'm_lever_chaise',
        'm_sppb_score'
    ]
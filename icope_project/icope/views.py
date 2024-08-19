from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .forms import QuestionnaireForm

def enregistrer_questionnaire(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            form.save()
            # Ajouter le code pour rediriger l'utilisateur vers une autre page après l'enregistrement des données
    else:
        form = QuestionnaireForm()
    
    return render(request, 'enregistrer_questionnaire.html', {'form': form})
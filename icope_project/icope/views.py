from django.shortcuts import render, redirect, get_object_or_404
from .models import Questionnaire
from .forms import QuestionnaireForm

# Create your views here.

def enregistrer_questionnaire(request):
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST)
        if form.is_valid():
            questionnaire = form.save()
            return redirect('detail_questionnaire', questionnaire_id=questionnaire.id)
    else:
        form = QuestionnaireForm()
    
    return render(request, 'enregistrer_questionnaire.html', {'form': form})

def detail_questionnaire(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    return render(request,'detail_questionnaire.html', {'questionnaire': questionnaire})

def modifier_questionnaire(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    if request.method == 'POST':
        form = QuestionnaireForm(request.POST, instance=questionnaire)
        if form.is_valid:
            form.save
            return redirect('detail_questionnaire', questionnaire_id=questionnaire.id) 
    else:
        form = QuestionnaireForm(instance=questionnaire)
    
    return render(request, 'modifier_questionnaire.html', {'form': form})



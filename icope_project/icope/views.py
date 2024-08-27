from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Questionnaire
from .forms import EnregistrementForm, ICOPE1Form, ICOPE2Form

# Vues Enregistrement.
def enregistrement_create(request):
    if request.method == 'POST':
        form = EnregistrementForm(request.POST)
        if form.is_valid():
            questionnaire = form.save()
            return redirect('enregistrement-detail', questionnaire_id=questionnaire.id)
    else:
        form = EnregistrementForm()
    
    return render(request, 'enregistrement_create.html', {'form': form})

def enregistrement_detail(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    return render(request,'enregistrement_detail.html', {'questionnaire': questionnaire})

def enregistrement_update(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    if request.method == 'POST':
        form = EnregistrementForm(request.POST, instance=questionnaire)
        if form.is_valid():
            form.save()
            return redirect('enregistrement-detail', questionnaire_id=questionnaire.id) 
    else:
        form = EnregistrementForm(instance=questionnaire)
    
    return render(request, 'enregistrement_update.html', {'form': form})


# Vues ICOPE1.
def icope1(request):
    if request.method == 'POST':
        numero_patient = request.POST.get('numero_patient')
        try:
            questionnaire = Questionnaire.objects.get(id=numero_patient)
            return redirect('icope1-create', questionnaire_id=questionnaire.id)
        except Questionnaire.DoesNotExist:
            messages.error(request, "Le patient avec ce numéro n'existe pas. Veuillez modifier le numéro.")
            return redirect('icope1')
    else:
        return render(request, 'icope1.html')

def icope1_create(request, questionnaire_id):
    questionnaire = Questionnaire.objects.get(id=questionnaire_id)
    if request.method == 'POST':
        form = ICOPE1Form(request.POST, instance=questionnaire)
        if form.is_valid():
            form.save()
            return redirect('icope1-detail', questionnaire_id=questionnaire.id)
    else:
        form = ICOPE1Form(instance=questionnaire)
    
    return render(request, 'icope1_create.html', {'form': form})

def icope1_detail(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    return render(request,'icope1_detail.html', {'questionnaire': questionnaire})

def icope1_update(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    if request.method == 'POST':
        form = ICOPE1Form(request.POST, instance=questionnaire)
        if form.is_valid():
            form.save()
            return redirect('icope1-detail', questionnaire_id=questionnaire.id) 
    else:
        form = ICOPE1Form(instance=questionnaire)
    
    return render(request, 'icope1_update.html', {'form': form})


# Vues ICOPE2.
def icope2(request):
    if request.method == 'POST':
        numero_patient = request.POST.get('numero_patient')
        try:
            questionnaire = Questionnaire.objects.get(id=numero_patient)
            return redirect('icope2-create', questionnaire_id=questionnaire.id)
        except Questionnaire.DoesNotExist:
            messages.error(request, "Le patient avec ce numéro n'existe pas. Veuillez modifier le numéro.")
            return redirect('icope2')
    else:
        return render(request, 'icope2.html')

def icope2_create(request, questionnaire_id):
    questionnaire = Questionnaire.objects.get(id=questionnaire_id)
    if request.method == 'POST':
        form = ICOPE2Form(request.POST, instance=questionnaire)
        if form.is_valid():
            form.save()
            return redirect('icope2-detail', questionnaire_id=questionnaire.id)
    else:
        form = ICOPE2Form(instance=questionnaire)
    
    return render(request, 'icope2_create.html', {'form': form, 'instance': questionnaire})

def icope2_detail(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    return render(request,'icope2_detail.html', {'questionnaire': questionnaire})

def icope2_update(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, id=questionnaire_id)
    if request.method == 'POST':
        form = ICOPE2Form(request.POST, instance=questionnaire)
        if form.is_valid():
            form.save()
            return redirect('icope2-detail', questionnaire_id=questionnaire.id) 
    else:
        form = ICOPE2Form(instance=questionnaire)
    
    return render(request, 'icope2_update.html', {'form': form})
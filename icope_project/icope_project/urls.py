"""
URL configuration for icope_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from icope import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enregistrement/add/', views.enregistrement_create, name='enregistrement-create'),
    path('enregistrement/<int:questionnaire_id>', views.enregistrement_detail, name='enregistrement-detail'),
    path('enregistrement/<int:questionnaire_id>/change', views.enregistrement_update, name='enregistrement-update'),
    path('icope1/', views.icope1, name='icope1'),
    path('icope1/<int:questionnaire_id>/add/', views.icope1_create, name='icope1-create'),
    path('icope1/<int:questionnaire_id>', views.icope1_detail, name='icope1-detail'),
    path('icope1/<int:questionnaire_id>/change', views.icope1_update, name='icope1-update'),
    path('icope2/', views.icope2, name='icope2'),
    path('icope2/<int:questionnaire_id>/add/', views.icope2_create, name='icope2-create'),
    path('icope2/<int:questionnaire_id>', views.icope2_detail, name='icope2-detail'),
    path('icope2/<int:questionnaire_id>/change', views.icope2_update, name='icope2-update'),
]

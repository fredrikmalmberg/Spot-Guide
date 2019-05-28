from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('wizard/', views.FormWizardView.as_view(), name='wizard'),
]

urlpatterns += [
    path('embedded/', views.embedded_wizard, name='embedded'),
    path('destinations/', views.destinations, name='destinations'),
    #path('wizard/', views.FormWizardView.as_view(), name='wizard'),
    
]
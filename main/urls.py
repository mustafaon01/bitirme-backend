# myapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('university-programs/', UniversityProgramsView2List.as_view(), name='university-programs-list'),
    path('general-information/', GeneralInformationView.as_view(), name='general-information'),
    path('universities/', UniversitiesView.as_view(), name='universities'),
]

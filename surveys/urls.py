from django.urls import path
from .views import *

urlpatterns = [
        # Homepage
        path('', HomePageView.as_view(), name='home'),
        # Survey
        path('surveys/', survey_list, name='survey-list'),
        path('surveys/<int:pk>/', survey_detail, name='survey-detail'),
        path('surveys/add/', survey_create, name='survey-add'),
        path('surveys/<int:pk>/edit/', survey_edit , name='survey-edit'),
        path('srveys/<int:pk>/delete/', survey_delete, name='survey-delete'),
]

from django.urls import path
from .views import *

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('surveys/', survey_list, name='survey-list'),
        path('surveys/<int:pk>/edit/', survey_edit , name='survey-edit'),
        path('surveys/add/', survey_create, name='survey-add'),
        path('surveys/<int:pk>/', survey_detail, name= 'survey-detail'),
        path('srveys/<int:pk>/delete/', survey_delete, name='survey-delete'),
]

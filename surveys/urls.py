from django.urls import path
from .views import *

urlpatterns = [
        # Homepage
        path('', HomePageView.as_view(), name='home'),
        # Survey
        path('surveys/', survey_list, name='survey-list'),
        path('surveys/<uuid:pk>/', survey_detail, name='survey-detail'),
        path('surveys/add/', survey_create, name='survey-add'),
        path('surveys/<uuid:pk>/edit/', survey_edit , name='survey-edit'),
        path('surveys/<uuid:pk>/delete/', survey_delete, name='survey-delete'),
        path('surveys/<uuid:pk>/question/', question_create, name='survey-question'),
        path('surveys/<uuid:survey_pk>/question/<int:question_pk>/option',
            option_create, name='option-create'),
        path('surveys/<uuid:pk>/start/', survey_start, name='survey-start'),
]

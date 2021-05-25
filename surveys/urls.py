from django.urls import path
from .views import HomePageView, SurveyPageView

urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
        path('surveys/', SurveyPageView.as_view(), name='surveys')
]

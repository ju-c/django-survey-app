from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class SurveyPageView(TemplateView):
    template_name = 'surveys.html'

from django.contrib import admin
from .models import Survey, Question, Option


class QuestionInline(admin.TabularInline):
    model = Question


class OptionInline(admin.TabularInline):
    model = Option


class SurveyAdmin(admin.ModelAdmin):
    inlines =[
            QuestionInline
    ]
    list_display = ("title",)


class QuestionAdmin(admin.ModelAdmin):
    inlines = [
            OptionInline,
    ]
    list_display = ("quest",)


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)

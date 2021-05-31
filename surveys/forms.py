from django import forms
from .models import Survey, Question, Option


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['title']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quest']


class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['choice']


class AnswerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        options = kwargs.pop("options")
        choices = {(o.pk, o.text) for o in options}
        super().__init__(*args, **kwargs)
        option_field = forms.ChoiceField(
                choices=choices,
                widget=forms.RadioSelect,
                required=True)
        self.fields["option"] = option_field


class BaseAnswerFormSet(forms.BaseFormSet):
    def get_form_kwargs(self, index):
        kwargs = super().get_form_kwargs(index)
        kwargs["options"] = kwargs["options"][index]
        return kwargs


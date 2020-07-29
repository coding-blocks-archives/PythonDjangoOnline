from django import forms

from main import models

class AnswerForm(forms.ModelForm):
  class Meta:
    model = models.Answer
    fields = ['choice']
# -*- coding: utf-8 -*-

from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label ="会社名")
    mail = forms.CharField(label="Email")
    gender=forms.BooleanField(label="gender", required=False)
    age = forms.IntegerField(label="age")
    
from django import forms
from django.core.exceptions import ValidationError

from triangle.models import Person_model


class Triangls(forms.Form):
    katet_1 = forms.FloatField(
        label="Katet No.1",
        min_value=0,
        step_size=0.001,
        required=True,
        help_text="Please enter a number greater than 0",
    )
    katet_2 = forms.FloatField(
        label="Katet No.2",
        min_value=0,
        step_size=0.001,
        required=True,
        help_text="Please enter a number greater than 0",
    )


class Person(forms.Form):
    first_name_1 = forms.CharField(max_length=200, required=True, )
    last_name_1 = forms.CharField(max_length=200, required=True, )
    email_1 = forms.EmailField(max_length=200, required=True, )

    def clean(self):
        super().clean()
        if self.cleaned_data.get("first_name_1") == "Dima":
            raise ValidationError("User already registered")
        if not Person_model.objects.filter(
                first_name_1=self.cleaned_data.get("first_name_1")) and Person_model.objects.filter(
                last_name_1=self.cleaned_data.get("last_name_1")) and Person_model.objects.filter(
                email_1=self.cleaned_data.get("email_1")):
            raise ValidationError("User not registered")



    # def clean_last_name_1(self):
    #     if self.cleaned_data.get("last_name_1") == "Pavlo":
    #         raise ValidationError("User already registered")
    #     return self.cleaned_data.get("last_name_1")


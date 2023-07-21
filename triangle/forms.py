from django import forms

from triangle.models import Person


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


class PersonModelForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=200,
        required=True,
    )
    last_name = forms.CharField(
        max_length=200,
        required=True,
    )
    email = forms.EmailField(
        max_length=200,
        required=True,
    )

    class Meta:
        model = Person
        fields = ["first_name", "last_name", "email"]

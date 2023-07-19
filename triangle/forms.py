from django import forms


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

from django import forms
from ..models import Feedback
from ..enums import Constants

# Different property values
# initial
# help_text
# required
# label
# disabled
# max_lenght
# min_lenght
class FeedbackDataForm(forms.Form):
    name = forms.CharField(
        label='Title',
        max_length=100,
        min_length=5,
        required=True,
        initial="title information",
        help_text='Title of Feedback, for example Phone not working'
    )
    email = forms.EmailField(
        label='Email address',
        initial="test@example.com",
        max_length=250
    )
    description = forms.CharField(
        max_length=250,
        widget=forms.Textarea(
            attrs={
                'rows': 8,
                'cols': 70,
            }
        )
    )
    location = forms.CharField(max_length=100)
    age = forms.IntegerField()
    section = forms.ChoiceField(choices=Constants.SECTION_CHOICES)
    gender = forms.ChoiceField(
        choices=Constants.GENDER_CHOICES,
        widget=forms.RadioSelect(),
        initial=Constants.GENDER_CHOICES[0][0],

    )
    created_at = forms.DateField(
        widget=forms.NumberInput(
            attrs={'type': 'date'}
        )
    )

class FeedbackDataModelForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            "name",
            "email",
            "age"
        ]



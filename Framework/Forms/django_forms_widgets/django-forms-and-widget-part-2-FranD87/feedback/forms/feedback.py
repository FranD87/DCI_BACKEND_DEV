from django import forms
from ..models import Feedback
from ..enums import Constants
from ..validators import age_range_validator, age_type_validator


# initial
# help_text
# required
# label
# disabled
# max_length
# min_length
class FeedbackDataForm(forms.Form):
    name = forms.CharField(
        label="Title",
        max_length=100,
        min_length=5,
        required=False,
        initial="title information",
        help_text="Title of Feedback, for example Phone not working"
    )
    email = forms.EmailField(
        label="Email Address",
        initial="test@example.com",
        max_length=250,
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
    age = forms.IntegerField(
        validators=[age_range_validator, age_type_validator]
    )
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
            "name", "email", "age"
        ]

'''
The provided code includes two Django form classes: `FeedbackDataForm` and `FeedbackDataModelForm`.

Form: FeedbackDataForm
- Fields:
  - `name`: CharField representing the title of the feedback. It has a maximum length of 100 characters, a minimum 
     length of 5 characters, and is not required. It is initially set to "title information". It includes a help text.
  - `email`: EmailField representing the email address. It has a maximum length of 250 characters and is initially 
     set to "test@example.com".
  - `description`: CharField representing the description of the feedback. It has a maximum length of 250 characters 
     and is rendered as a textarea with 8 rows and 70 columns.
  - `location`: CharField representing the location. It has a maximum length of 100 characters.
  - `age`: IntegerField representing the age. It includes two validators: `age_range_validator` and 
     `age_type_validator`.
  - `section`: ChoiceField representing the section. It uses choices defined in `Constants.SECTION_CHOICES`.
  - `gender`: ChoiceField representing the gender. It uses choices defined in `Constants.GENDER_CHOICES` and is 
     rendered as a RadioSelect widget. The initial value is the first choice in `GENDER_CHOICES`.
  - `created_at`: DateField representing the creation date. It is rendered as a date input field.

Form: FeedbackDataModelForm
- Meta class:
  - Specifies the model to be used, which is `Feedback`.
  - Includes the `name`, `email`, and `age` fields from the `Feedback` model.

These form classes provide a way to validate and handle user input for creating or updating feedback data. The 
`FeedbackDataForm` is a regular form class, while the `FeedbackDataModelForm` is a model form class associated with 
the `Feedback` model.
'''
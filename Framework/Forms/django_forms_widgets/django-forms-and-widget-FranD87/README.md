# Python-basics-django-forms-and-widgets
A django project to reflect and understand django forms and widgets

#How to run the project
1. Create a virtual environment `python3 venv venv`
2. activate the virtual environment `source venv/bin/activate`
3. install the necessary dependencies `pip install -r requirements.txt`
4. create a `.env` file in the base directory
5. copy and edit values from the `.envexample` file
6. run `source .env`
7. run `python manage.py check` to validate all is well
8. run `python manage.py migrate` to migrate
9. run the local server with `python manage.py runserver`

# Task 1
Try out the following form fields by creating two form classes (FeedbackForm and DiaryForm).
FeedbackForm will contain : email, first_name, last_name, age, gender, comment, section, created_at
DiaryForm will contain : email, first_name, last_name, note, picture, created_at

FIELDS

BooleanField
CharField
ChoiceField
DateField
DateTimeField
DecimalField
DurationField
EmailField
FileField
FloatField
IntegerField
JSONField
SlugField
TimeField
TypedChoiceField
TypedMultipleChoiceField
URLField
UUIDField


ModelChoiceField
ModelMultipleChoiceField


# Task 2
add a few field arguments(Where applicable) to the fields of the FeedbackForm and DiaryForm

ARGUMENTS 
required
label
label_suffix
initial
widget
help_text

# Task 3
try out different widgets for :
Charfield, DateField and ChoiceField used in FeedbackForm and DiaryForm

# Task 4

Create a new Form called FeedbackModelForm using forms.ModelForm

# task 5
Display both the FeedbackForm and DiaryForm in seperate views, also initialize data for 
created_at and section fields. Make sure email, first_name, last_name, age, comment, section are required fields.
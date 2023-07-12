# **Create REST api**

## **Overview**
In Django Rest Framework (DRF), data validation and sanitization are important steps in ensuring the integrity and security of the data being passed through the API. This submodule is designed to teach you how to  validate, sanitize RESTful APIs using Django REST Framework (DRF) alongside with exception handeling.

## **Data Validation**

- Data validation is a process of ensuring that the input data provided by the user is correct and meets the specified requirements. It's important because it helps ensure data integrity and prevent errors from occurring.

- DRF provides serializers for data validation. Serializers are classes that define the fields and the validation rules for each field. You can define required fields, default values, and custom validation rules.

- DRF comes with built-in validators for common data types, such as email, URL, and date fields. You can also create custom validators that check for specific requirements.

- When a validation error occurs, DRF raises a `ValidationError` exception. The exception contains a dictionary of error messages for each invalid field.

- You can customize error messages by adding a `message` parameter to your validators or by overriding the `get_error_message()` method in your serializer.

- DRF supports both client-side validation (checking data before it's sent to the server) and server-side validation (checking data on the server after it's received).\


- The validation take place in the model and the serializers. In our book projects we will add two built in validators and two customised validators. \
In **myBookaap/serializerspy** we add the following :
```python 
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Book
from datetime import date
from django.core.validators import MaxLengthValidator
class UniqueTitleValidator:
    def __call__(self, value):
        if Book.objects.filter(title=value).exists():
            raise ValidationError("A book with this title already exists.")

class PastDateValidator:
    def __call__(self, value):
        if value > date.today():
            raise ValidationError("Published date must be in the past.")

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField( required=True, validators=[UniqueTitleValidator(),MaxLengthValidator(200)])
    author = serializers.CharField(required=True,validators=[MaxLengthValidator(200)])
    published_date = serializers.DateField(required=True, validators=[PastDateValidator()])

    class Meta:
        model = Book
        fields = ['id','title','author','description','published_date','is_published']
```
- Here's a brief explanation of the validators :

1. **UniqueTitleValidator:** This validator checks whether a book with the same title already exists in the database. It is implemented as a callable class with a **__call__** method that performs the validation logic. If a book with the same title already exists, it raises a **ValidationError** with an appropriate message.

2. **PastDateValidator:** This validator checks whether the published_date field is in the past. It is also implemented as a callable class with a **__call__** method that performs the validation logic. If the published_date field is not in the past, it raises a **ValidationError** with an appropriate message.
3. **max_length:** This built in validator checks if the maximum length of the title and the author exceeds 200 character or not.
4. **required=True**: a parameter, which means that they must be included in the request data, or else a validation error will be raised
## **Data Sanitization**

- Data sanitization is a process of cleaning up input data to remove any potentially dangerous characters or code that could cause security vulnerabilities, such as SQL injection or cross-site scripting (XSS) attacks.

- DRF provides built-in sanitizers that can be used to clean up input data. For example, the `strip_tags` sanitizer can be used to remove any HTML tags from a string, while the `escape_html` sanitizer can be used to replace any special characters with their HTML entities.

- Sanitization is performed automatically by DRF when data is deserialized. The `to_internal_value` method in a serializer is responsible for cleaning up input data.

- You can also create your own sanitizers to customize the cleaning process. Sanitizers can be added to a serializer's `to_internal_value` method or to a specific field's `run_validation` method.

- Sanitization is an important part of securing your application and protecting against attacks. However, it's important to note that sanitization alone is not enough to ensure security. Other security measures, such as input validation and user authentication, are also necessary to prevent attacks.
- - The sanitization take place in the model and the serializers. In our book projects we will add two built in validators and two customised validators. \
In **myBookaap/serializerspy** we add the following :
```python 
from rest_framework import serializers, validators
from rest_framework.exceptions import ValidationError
from .models import Book
from datetime import date
from django.utils.html import escape, strip_tags
from django.utils.text import slugify

class UniqueTitleValidator:
    def __call__(self, value):
        if Book.objects.filter(title=value).exists():
            raise ValidationError("A book with this title already exists.")

class PastDateValidator:
    def __call__(self, value):
        if value > date.today():
            raise ValidationError("Published date must be in the past.")

class CapitalizeName:
    def __call__(self, value):
        # Capitalize the first letter of each word in the name
        return value.title()

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, required=True, validators=[UniqueTitleValidator()],trim_whitespace=True)
    author = serializers.CharField(max_length=255, required=True,trim_whitespace=True)
    published_date = serializers.DateField(required=True, validators=[PastDateValidator()])
    description = serializers.CharField(required=False, allow_blank=True)

    def validate_title(self, value):
        return strip_tags(value)

    def validate_description(self, value):
        return strip_tags(value)
    
    def validate_author(self,value):
        return strip_tags(value)

    def to_internal_value(self, data):
        # Sanitize is_published field by converting string value to boolean
        if 'is_published' in data:
            data['is_published'] = True
        return super().to_internal_value(data)

    def to_representation(self, instance):
        # Capitalize the first letter of each word in the author name
        instance.author = CapitalizeName()(instance.author)
        instance.title=CapitalizeName()(instance.title)
        return super().to_representation(instance)

    class Meta:
        model = Book
        fields = ['id','title','author','description','published_date','is_published']

```
- Here is a brief explanation of the sanitizers we added :
1. **validate_title method:** This method applies the `strip_tags` function to the value of the `title` field. 

2. **validate_description method:** This method applies the `strip_tags` function to the value of the `description` field. `strip_tags` is a built-in Django function that removes any HTML tags from a string. This is important because it prevents users from inserting HTML or JavaScript code into the `description` field, which could potentially be used to perform XSS attacks.

3. **validate_author method:** This method also applies the `strip_tags` function to the value of the `author` field. This is done to ensure that the `author` field only contains plain text, and to prevent any malicious code or HTML from being injected into the field.

4. **to_internal_value method:** This method is called by Django Rest Framework when the serializer is used to deserialize incoming JSON data. The method checks if the `is_published` field is present in the incoming data, and if it is, converts the value to a boolean and replaces the original value in the data dictionary. This is done to ensure that the `is_published` field is always a boolean value, regardless of whether it is passed in as a string or a boolean.

5. **to_representation method:** This method is called by Django Rest Framework when the serializer is used to serialize a Django model instance into JSON. The method applies the `CapitalizeName` class to the `author` and `title` fields of the instance, which capitalizes the first letter of each word in the field. This is done to ensure that the `author` and `title` fields are always formatted consistently, regardless of how they were originally entered.

6. **CapitalizeName class:** This class is defined at the top of the serializer file and is used to capitalize the first letter of each word in a string. It is used by the `to_representation` method to ensure consistent formatting of the `author` and `title` fields.

7. **trim_whitespace=True** is added to the title and author fields. This means that any whitespace characters (e.g. spaces, tabs, newlines) at the beginning or end of the string will be removed before validation. This ensures that there are no leading or trailing spaces in the title and author fields, which can cause issues when querying or displaying the data.

from django import forms

class BlogForm(forms.Form):
    title = forms.CharField(max_length=25, required=True)
    name = forms.CharField(max_length=50)
    email = forms.EmailField()

def form_is_good(form: forms.Form):
    print(form)
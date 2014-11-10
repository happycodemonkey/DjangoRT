from django import forms
from django.core.validators import validate_email

# This was pulled from : https://docs.djangoproject.com/en/1.7/ref/forms/validation/
class MultiEmailField(forms.Field):
    def to_python(self, value):
        "Normalize data to a list of strings."

        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(',')

    def validate(self, value):
        "Check if value consists only of valid emails."

        # Use the parent's handling of required fields, etc.
        super(MultiEmailField, self).validate(value)

        for email in value:
            validate_email(email.strip())

class TicketForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'ticket-input'}), label='First name', max_length=100, required=True)
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'ticket-input'}), label='Last name', max_length=100, required=True)
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'ticket-input'}), label='Email', required=True)
	cc = MultiEmailField(widget=forms.EmailInput(attrs={'class' : 'ticket-input'}), required=False, help_text='Multiple emails should be comma-separated')
	subject = forms.CharField(widget=forms.TextInput(attrs={'class' : 'ticket-input'}), label='Subject', max_length=100, required=True)
	problem_description = forms.CharField(label='Problem Description', required=True, widget=forms.Textarea({'class': 'ticket-input'}))

class ReplyForm(forms.Form):
	reply = forms.CharField(required=True, widget=forms.Textarea, label="")


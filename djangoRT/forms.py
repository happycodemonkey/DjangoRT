from django import forms
from djangoRT import rtUtil

class TicketForm(forms.Form):
	rt = rtUtil.DjangoRt()

	first_name = forms.CharField(label='First name', max_length=100, required=True)
	last_name = forms.CharField(label='Last name', max_length=100, required=True)
	email = forms.EmailField(label='Email', required=True)
	cc = forms.EmailField(label='CC') # make this so that you can add multiple?
	category = forms.ChoiceField(label='Category', choices=rt.getCategories(), required=True)
	system = forms.MultipleChoiceField(label='System', choices=rt.getSystems(), required=True)
	subject = forms.CharField(label='Subject', max_length=100, required=True)
	problem_description = forms.CharField(label='Problem Description', required=True)

class ReplyForm(forms.Form):
	reply = forms.CharField(label="Reply", required=True)

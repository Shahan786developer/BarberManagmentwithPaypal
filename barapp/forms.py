from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm
from tempus_dominus.widgets import DatePicker, TimePicker

# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    desc = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter Description', 'style': 'background-color: white; color: black;'})
    )
    working_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD', 'style': 'background-color: white; color: black;'}))
    working_time = forms.TimeField(widget=forms.TextInput(attrs={'type': 'time', 'placeholder': 'HH:mm:ss', 'style': 'background-color: white; color: black;'}))

    class Meta:
        model = Order
        fields = ['services', 'desc', 'working_date', 'working_time']



class ReviewForm(forms.ModelForm):
    rew = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter Description', 'style': 'background-color: white; color: black;'})
    )
    class Meta:
        model = Review
        fields = ['worker', 'rew']


class ShopForm(forms.ModelForm):
    rew = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter Description', 'style': 'background-color: white; color: black;'})
    )
    class Meta:
        model = ShopReview
        fields = ['rew']
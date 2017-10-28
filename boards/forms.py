
from .models import Board
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, get_user_model, logout


User = get_user_model()


class ExistingUserForm(forms.Form):

	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
 	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

	# class Meta:
	# 	model = User
	# 	fields = ['username','password']

	# def clean(self, *args, **kwargs):
	# 	username = self.cleaned_data.get("username")
	# 	password = self.cleaned_data.get("password")


	# 	if username and password:
	# 		user = authenticate(username=username,password=password)
	# 		if not user:
	# 			raise forms.ValidationError("This user does not exist")
	# 		if not user.check_password(password):
	# 			raise forms.ValidationError("Incorrect Password")
	# 		if not user.is_active:
	# 			raise forms.ValidationError("This user is no longer active")
	# 		return super(ExistingUserForm, self).clean(*args,**kwargs)


# class ExistingUserForm(forms.ModelForm):

# 	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
#  	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))

# 	class Meta:
# 		model = Board
# 		fields = ['username','password']


# class UserLoginForm(forms.Form):
# 	username = forms.CharField()
# 	password = forms.CharField(widget=forms.PasswordInput)




class UserRegisterForm(forms.Form):

	FullName = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
 	FirmName = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'FirmName'}))
 	Email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
 	MobileNo = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'MobileNo'}))
 	Password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
 	Confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))



	# class Meta:
	# 	model = User
	# 	fields = [

	# 		'Username',
	# 		'FirstName',
	# 		'LastName',
	# 		'Email',
	# 		'MobileNo',
	# 		'Password1',
	# 		'Password2'

	# 	]


class ForgotPasswordForm(forms.Form):

	 	Email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter registered email'}))

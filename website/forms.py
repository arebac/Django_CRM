import django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email=forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Addres'}))
    first_name= forms.CharField(label="", max_length="100",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    last_name= forms.CharField(label="", max_length="100", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    

    class Meta:
        model= User
        fields=('username','first_name','last_name','email','passsword1','password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['placeholder']='User Name'
        self.fields['username'].label=''
        self.fields['username'].help_text='<span class="form-text text-muted"><small>Required. 150 or fewer digits and @/./+/-/_</small></span>'

        self.fields['password1'].widget.attrs['class']='form-control'
        self.fields['password1'].widget.attrs['placeholder']='Password'
        self.fields['password1'].label=''
        self.fields['password1'].help_text='<ul class="form-text text-muted small"><li>Your password can\'t be too similar to you other personal information.</li><li>Your password must contain at least 8 characters.</li>Your password can\'t be commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class']='form-control'
        self.fields['password2'].widget.attrs['placeholder']='Confirm Password'
        self.fields['password2'].label=''
        self.fields['password2'].help_text='<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

from django import forms
from .models import User
class UserCreationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','password']
        widgets={
            'first_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Your First Name'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Your Last Name'
            }),
            'email':forms.EmailInput(attrs={
                'class':'form-control',
             
            }),
            'password':forms.PasswordInput(attrs={
                'class':'form-control'
                
            })
            


            
        }
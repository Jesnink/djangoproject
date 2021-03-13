from django import forms
from .models import Book,Category
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        exclude=['user']
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Your Name'
            }),
            'author':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter author name'
            }),
            'price':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Book Price'
            }),
            'category':forms.Select(attrs={
                'class':'form-control'
                
            })
            


            
        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Category Name'
            }),
            'description':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Write Description'
            }),
            'color':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Select Color',
                'type':'color'
            })
        }
    #def clean_author(self):
        #if " " not in self.cleaned_data('author'):
            #raise forms.ValidationError('Invalid author name')
        #return self.cleaned_data.get('author')
        
from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'desc', 'year', 'image' , 'director']
        widgets={

            'name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':"Enter movie name"
                }
            ),
            'desc': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':"Enter movie description",
                    'rows':4
                }
            ),
            'year': forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'placeholder':"Enter movie year",
                }
            ),
            'image': forms.FileInput(
                attrs={
                    'class':'form-control-file',
                }
            ),
            'director': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':"Enter director name",
                }
            ),
            

        }




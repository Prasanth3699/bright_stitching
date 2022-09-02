from django import forms
from .models import *

class safetyform(forms.ModelForm):

    class Meta:
        model = safetyWears
        fields = ['name', 'material_name','price','description','image']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter product name'}),
            'material_name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control mb-3','cols':'30','rows':'4'}),
            # 'image':forms.ImageField()
        }

class tshirtform(forms.ModelForm):

    class Meta:
        model = tshirts
        fields = ['name', 'material_name','price','description','image']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter product name'}),
            'material_name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','cols':'30','rows':'4'}),
        }

class uniform_form(forms.ModelForm):

    class Meta:
        model = uniforms
        fields = ['name', 'material_name','price','description','image']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter product name'}),
            'material_name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','cols':'30','rows':'4'}),
        }

class cap_form(forms.ModelForm):

    class Meta:
        model = caps
        fields = ['name', 'material_name','price','description','image']

        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter product name'}),
            'material_name':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','cols':'30','rows':'4'}),
        }
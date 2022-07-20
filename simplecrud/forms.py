from django import forms

from simplecrud.models import Crudsimple

class CrudsimpleForm(forms.ModelForm):
    gender_choices = (
        ('Pria', 'Pria'),
        ('Wanita', 'Wanita'),
    )
    nip = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NIP'}))
    nama = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama'}))
    divisi = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Divisi'}))
    alamat = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alamat'}))
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=gender_choices)
    foto = forms.ImageField
    class Meta:
        model = Crudsimple
        fields = ('nip', 'nama', 'divisi', 'alamat', 'gender', 'foto')
        

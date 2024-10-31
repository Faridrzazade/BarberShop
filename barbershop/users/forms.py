from django import forms
from salons.models import *
from users.models import *


class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = '__all__' 



class BarberForm(forms.ModelForm):
    class Meta:
        model = Barber
        fields = '__all__' 



class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = '__all__' 

    phone = forms.CharField(max_length=15)
    gender = forms.ChoiceField(choices=[('male', 'Kişi'), ('female', 'Qadın'), ('other', 'Digər')])
    birth_date = forms.DateField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Şifrələr uyğun gəlmir.')

        return cleaned_data

class BarberRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Barber
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address', 'description', 'services', 'image', 'tiktok_username', 'instagram_username']  
        widgets = {
            'image': forms.ClearableFileInput(attrs={'required': False}),
        }
    gender = forms.ChoiceField(choices=[('male', 'Kişi'), ('female', 'Qadın'), ('other', 'Digər')])
    birth_date = forms.DateField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('��ifrələr uyğun gəlmir.')

        return cleaned_data

class SalonRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Şifrə')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Şifrəni Təkrarla')

    class Meta:
        model = Salon
        fields = ['name', 'address', 'phone', 'services', 'barbers', 'tiktok_username', 'instagram_username', 'image', 'description']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Şifrələr uyğun gəlmir.')

        return cleaned_data
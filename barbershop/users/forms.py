from django import forms
from salons.models import Salon
from users.models import Barber

class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ['name', 'address', 'phone_number', 'image']


class BarberForm(forms.ModelForm):
    class Meta:
        model = Barber
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address', 'image', 'description', 'services', 'salons']


class Form(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['tiktok_username'] 


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

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
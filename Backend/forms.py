from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpform(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'ایمیل خود را وارد کنید'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']     

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # اضافه کردن کلاس CSS به فیلدها
        for field_name in ['username', 'password1', 'password2']:
            self.fields[field_name].widget.attrs['class'] = 'form-control'
        
        self.fields['username'].widget.attrs['placeholder'] = 'نام کاربری'
        self.fields['password1'].widget.attrs['placeholder'] = 'رمز عبور'
        self.fields['password2'].widget.attrs['placeholder'] = 'تکرار رمز عبور'
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 4:
            raise forms.ValidationError('نام کاربری باید حداقل ۴ کاراکتر باشد')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلاً ثبت نام کرده است')
        return email
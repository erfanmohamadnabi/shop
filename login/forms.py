from django import forms

from django.contrib.auth.models import User
from django.core.validators import validate_email

class SignIn(forms.Form):
    username=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"name":"signinnn","maxlength":"200"}))
    fname=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"name":"signinnn","maxlength":"200"}))
    password=forms.CharField(widget=forms.PasswordInput())

    
    
    def clean_password(self):
        p=self.cleaned_data.get("password")

        if len(p) < 8:
            raise forms.ValidationError("رمز عبور باید حداقل 8 کاراکتر باشد")

        return p
    
    


    def clean_username(self):
        n = self.cleaned_data.get("username")
        u = User.objects.filter(username=n)
    
        if u.count() > 0:
            raise forms.ValidationError("این کاربر قبلا وجود دارد")
            
        if n.isdigit() and len(n) == 11:
            # اگر 'n' یک شماره تلفن درست است
            return n
        else:
            try:
                validate_email(n)
                # اگر 'n' یک ایمیل معتبر است
                return n
            except:
                raise forms.ValidationError("شماره تلفن یا ایمیل خود را به درستی وارد کنید")
        
#____________________________________________________________________________________

class loginn(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "class":"in1"
    }),max_length=220)

    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"in3"
    }),max_length=100)






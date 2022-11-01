from .models import User
from django import forms

class signupForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'full name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'email'}))
    telephone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'tel number'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm password'}))
    class Meta:
        model=User
        fields=('username','full_name','email','password','confirm_password','telephone','usertype')

    def clean(self):
        cleaned_data = super(signupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(signupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    def __init__(self, *args, **kwargs):
        super(signupForm, self).__init__(*args, **kwargs)
                
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
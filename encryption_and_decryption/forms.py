from django import forms
from .models import Author
from django.contrib.auth import(
   authenticate,
   get_user_model,
   login,
   logout,
)
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password.")
            if not user.is_active:
                raise forms.ValidationError("This user is not longer active.")


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Author
        fields = [
            'name',
            'email',
            'password',
            'confirm_password'
        ]

    def clean_password(self):
        password = forms.CharField(widget=forms.PasswordInput)
        confirm_password = forms.CharField(widget=forms.PasswordInput)
        if password != confirm_password:
            raise forms.ValidationError("Password must match.")
        password_qs = User.objects.filter(password=password)
        if password_qs.exists():
            raise forms.ValidationError("Password match")
        return confirm_password

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    password = forms.CharField(max_length=254, required=True, widget=forms.PasswordInput())


class ChangePasswordForm(forms.Form):
    username = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = User.objects.get(username=self.cleaned_data["username"])
        if user:
            user.set_password(self.cleaned_data["password1"])
            user.save()
            return user
        else:
            raise forms.ValidationError("User Not Exists")



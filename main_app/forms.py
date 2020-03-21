from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegistrationForm(UserCreationForm):
    avatar = forms.URLField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'avatar')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        profile = Profile(user=user, avatar=self.cleaned_data['avatar'])
        profile.save()
        return user

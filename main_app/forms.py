from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .utils import upload_file


class RegistrationForm(UserCreationForm):
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'avatar')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        avatar_file = self.files.get('avatar', None)
        avatar_url = ''
        if avatar_file:
            avatar_url = upload_file(avatar_file)
        profile = Profile(user=user, avatar=avatar_url)
        profile.save()
        return user

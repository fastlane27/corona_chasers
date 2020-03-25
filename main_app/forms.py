from django.forms import ModelForm, Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Comment
from .utils import upload_file
from .fields import RestrictedImageField


class RegistrationForm(UserCreationForm):
    avatar = RestrictedImageField(max_file_size=256000, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'avatar')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save()
        avatar_file = self.cleaned_data.get('avatar')
        avatar_url = ''
        if avatar_file:
            avatar_url = upload_file(avatar_file)
        profile = Profile(user=user, avatar=avatar_url)
        profile.save()
        return user


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class AvatarForm(Form):
    avatar = RestrictedImageField(max_file_size=256000)

    def save(self):
        avatar_file = self.cleaned_data.get('avatar')
        avatar_url = upload_file(avatar_file)
        return avatar_url

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group

from .models.user import Gender, User


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # instance = getattr(self, 'instance', None)
        self.fields[
            "password"
        ].help_text = "Password will autmoatically be hashed after saving the form."

    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            # 'password': forms.PasswordInput(),
            "class": "fluid",
        }

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ["username", "email", "uid", "date_joined"]


admin.site.register(User, UserAdmin)
admin.site.register(Gender)

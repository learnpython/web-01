from django import forms
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.flatpages.models import FlatPage
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator, MinLengthValidator

from users.models import UserProfile


class LoginForm(forms.Form):
    """
    Simple login form.
    """
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def login(self, request):
        """
        Perform login action or raise an error.
        """
        data = self.cleaned_data
        kwargs = {'username': data['username'], 'password': data['password']}
        user = auth.authenticate(**kwargs)

        if not user:
            raise ValidationError('Please, fill in valid username/password '
                                  'pair.')

        auth.login(request, user)
        messages.success(request, 'Welcome back, {}!'.format(user.username))

        return user


class RegisterForm(forms.Form):
    """
    Simple register form.
    """
    username = forms.CharField(label='Username')
    email = forms.EmailField(label='E-Mail')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    repeat = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput
    )
    is_company = forms.BooleanField(
        label='I am company represantive!', required=False
    )
    company = forms.CharField(
        label='Company name', required=False,
        validators=[MinLengthValidator(3), MaxLengthValidator(32)]
    )

    def clean_company_name(self):
        """
        Check that company name not previously taken.
        """
        data = self.cleaned_data

        try:
            UserProfile.objects.create(company=data['company'])
        except UserProfile.DoesNotExist:
            return data['company']

        raise ValidationError('Company name "{}" already taken!'.
                              format(data['company']))

    def clean_repeat(self):
        """
        Check that passwords matched.
        """
        data = self.cleaned_data

        if not data['password'] or not data['repeat']:
            return data

        if data['password'] != data['repeat']:
            raise ValidationError('Passwords are not match!')

        return data['repeat']

    def clean_username(self):
        """
        Check that username not previously taken.
        """
        data = self.cleaned_data

        try:
            User.objects.get(username=data['username'])
        except User.DoesNotExist:
            return data['username']

        raise ValidationError('Username "{}" already taken!'.
                              format(data['username']))

    def register(self, request):
        """
        Create new user, profile and flatpage if necessary and login it to site
        after all.
        """
        data = self.cleaned_data
        kwargs = {
            'username': data['username'],
            'password': data['password'],
            'email': data['email'],
        }

        try:
            user = User.objects.create_user(**kwargs)
        except Exception:
            raise ValidationError('Cannot register new user cause of '
                                  'database error.')
        # Don't forget to set backend to later login to site
        else:
            user.backend = 'django.contrib.auth.backends.ModelBackend'

        if data['is_company']:
            profile = user.get_profile()
            profile.company = data['company']
            profile.save()

            kwargs = {
                'url': '/company-{}/'.format(data['company']),
                'title': 'Home page',
                'content': '<p>Welcome, {}</p>\n' \
                           '<p>This is home page for your company: {}!</p>'.\
                           format(data['username'], data['company'])
            }
            flatpage = FlatPage.objects.create(**kwargs)

        auth.login(request, user)
        messages.success(request, 'You are registered at Zapis Online!')

        return user

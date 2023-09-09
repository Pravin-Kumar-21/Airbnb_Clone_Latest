from typing import Any, Dict
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import FormView, DetailView, UpdateView
from django.views import View
from . import forms, models
from django.contrib.auth import authenticate, login, logout
import os
import requests
from django.contrib import messages
import json
from django.contrib.messages.views import SuccessMessageMixin
from . import mixins


class LoginView(mixins.LoggedOutOnlyView, FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        user.verify_email()
        return super().form_valid(form)


def complete_verification(request, key):
    try:
        user = models.User.objects.get(email_secret=key)
        user.email_confirmed = True
        user.save()
    except models.User.DoesNotExist:
        pass
    return redirect(reverse("core:home"))


def github_login(request):
    client_id = os.environ.get("GIT_ID")
    redirect_uri = "http://127.0.0.1:8000/users/login/github/callback"
    return redirect(
        f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope=read:user"
    )


class GithubException(Exception):
    pass


def github_callback(request):
    try:
        client_id = os.environ.get("GIT_ID")
        client_secret = os.environ.get("GIT_SECRET")
        code = request.GET.get("code", None)
        if code is not None:
            token_request = requests.post(
                f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
                headers={"Accept": "application/json"},
            )
            token_json = token_request.json()
            error = token_json.get("error", None)
            if error is not None:
                raise GithubException("Can't get access token")
            else:
                access_token = token_json.get("access_token")
                profile_request = requests.get(
                    "https://api.github.com/user",
                    headers={
                        "Authorization": f"token {access_token}",
                        "Accept": "application/json",
                    },
                )
                profile_json = profile_request.json()
                username = profile_json.get("login", None)
                if username is not None:
                    name = profile_json.get("name")
                    email = profile_json.get("email")
                    bio = profile_json.get("bio")
                    try:
                        user = models.User.objects.get(email=email)
                        if user.login_method != models.User.LOGIN_GITHUB:
                            raise GithubException(
                                f"Please log in with: {user.login_method}"
                            )
                    except models.User.DoesNotExist:
                        user = models.User.objects.create(
                            login_method=models.User.LOGIN_GITHUB,
                            email_confirmed=True,
                        )
                        user.set_unusable_password()
                        user.save()
                    login(request, user)
                    messages.success(request, f"Welcome back {user.first_name}")
                    return redirect(reverse("core:home"))
                else:
                    raise GithubException("Can't get your profile")
        else:
            raise GithubException("Can't get code")
    except GithubException as e:
        messages.error(request, e)
        return redirect(reverse("users:login"))


def google_login(request):
    # Redirect the user to Google's authentication page
    scope = "https://www.googleapis.com/auth/userinfo.profile"
    # redirect_uri = ("http://127.0.0.1:8000/users/google/callback/")
    redirect_uri = request.build_absolute_uri("/users/accounts/google/login/callback/")
    client_id = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
    auth_url = f"https://accounts.google.com/o/oauth2/auth?scope={scope}&response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
    return redirect(auth_url)


def google_callback(request):
    try:
        code = request.GET.get("code")
        redirect_uri = request.build_absolute_uri(
            "/users/accounts/google/login/callback/"
        )
        client_id = os.environ.get("GOOGLE_OAUTH_CLIENT_ID")
        client_secret = os.environ.get("GOOGLE_OAUTH_CLIENT_SECRET")

        # Exchange the authorization code for an access token
        token_url = "https://oauth2.googleapis.com/token"
        data = {
            "code": code,
            "client_id": client_id,
            "client_secret": client_secret,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        }
        response = requests.post(token_url, data=data)
        token_data = response.json()

        # Check if the response contains the 'access_token' key
        access_token = token_data.get("access_token")

        if not access_token:
            # If 'access_token' is missing, handle the error
            raise Exception("Access token not found in the response")

        # Get user info from Google using the access token
        user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"
        headers = {"Authorization": f"Bearer {access_token}"}
        user_info_response = requests.get(user_info_url, headers=headers)
        user_info = user_info_response.json()
        print(user_info)

        # Check if the user with this email already exists in the database
        try:
            user = models.User.objects.get(
                email=user_info["email"]
            )  # Use the Django User model
        except models.User.DoesNotExist:
            # If the user doesn't exist, create a new user
            user = models.User.objects.create(
                username=user_info["email"],  # Use email as the username
                email=user_info["email"],
                first_name=user_info.get("given_name", ""),
                last_name=user_info.get("family_name", ""),
                # Other fields as needed based on your User model
            )

        # Save the user before authenticating
        user.save()

        # Authenticate the user and log in
        user = authenticate(request, username=user.username)
        login(request, user)
        # Redirect to a success page or homepage
        return redirect("core:home")
        # Replace 'home' with the name of your homepage URL pattern

    except Exception as e:
        # Handle any exceptions or errors during the OAuth process
        messages.error(request, "Something went wrong with Google authentication.")
        return redirect("core:home")


class UserProfileView(DetailView):
    model = models.User
    context_object_name = "user_obj"


class UpdateProfileView(mixins.LoggedInOnlyView, SuccessMessageMixin, UpdateView):
    pass
    model = models.User
    template_name = "users/update-profile.html"
    fields = (
        "first_name",
        "last_name",
        "avatar",
        "gender",
        "bio",
        "birthdate",
        "language",
        "currency",
        "superhost",
    )
    success_message = "Profile Updated"

    def get_object(self, queryset=None):
        return self.request.user


class UpdatePasswordView(
    mixins.LoggedInOnlyView, PasswordChangeView, SuccessMessageMixin
):
    template_name = "users/update-password.html"
    success_url = reverse_lazy("core:home")

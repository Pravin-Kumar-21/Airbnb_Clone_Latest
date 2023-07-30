from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path("login", views.LoginView.as_view(), name="login"),
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("login/github", views.github_login, name="github-login"),
    path("login/github/callback", views.github_callback, name="github-callback"),
    path("logout", views.log_out, name="logout"),
    path("verify/<str:key>", views.complete_verification, name="complete-verification"),
    path("google/login/", views.google_login, name="google_login"),
    path(
        "accounts/google/login/callback/", views.google_callback, name="google_callback"
    ),
]

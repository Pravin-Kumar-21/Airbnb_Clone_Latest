from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"
    LANGUAGE_SPANISH = "es"
    LANGUAGE_FRENCH = "fr"
    LANGUAGE_GERMAN = "de"
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_SPANISH, "Spanish"),
        (LANGUAGE_FRENCH, "French"),
        (LANGUAGE_GERMAN, "German"),
    )

    CURRENCY_IND = "inr"
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "kre"
    CURRENCY_EUR = "eur"
    CURRENCY_ESP = "esp"
    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_KRW, "KRW"),
        (CURRENCY_IND, "INR"),
        (CURRENCY_EUR, "EUR"),
        (CURRENCY_ESP, "ESP"),
    )
    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=10,
        blank=True,
    )
    bio = models.TextField(default="", blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, blank=True, default=LANGUAGE_ENGLISH
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True, default=CURRENCY_IND
    )
    superhost = models.BooleanField(default=False)

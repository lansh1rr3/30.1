from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Убираем username как обязательное поле
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)
    # Используем email как основное поле для авторизации
    email = models.EmailField(unique=True)

    # Дополнительные поля
    phone = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Указываем, что email будет использоваться вместо username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

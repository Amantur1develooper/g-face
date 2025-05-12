# from django.db import models

# # Create your models here.
# # models.py
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class Role(models.Model):
#     """
#     Модель для ролей пользователей (админ, бухгалтер и т.д.)
#     """
#     name = models.CharField(max_length=50, unique=True)
#     description = models.TextField(blank=True)
    
#     def __str__(self):
#         return self.name

# class CustomUser(AbstractUser):
#     """
#     Кастомная модель пользователя с добавлением ролей
#     """
#     roles = models.ManyToManyField(Role, blank=True)
    
#     def has_role(self, role_name):
#         """
#         Проверяет, есть ли у пользователя указанная роль
#         """
#         return self.roles.filter(name=role_name).exists()
    
#     def is_admin(self):
#         """
#         Проверяет, является ли пользователь админом
#         """
#         return self.has_role('admin')
    
#     def is_accountant(self):
#         """
#         Проверяет, является ли пользователь бухгалтером
#         """
#         return self.has_role('accountant')
    
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
# models.py
from django.db import models
from django.utils import timezone

class GameScore(models.Model):
    player_name = models.CharField(max_length=20)
    score = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-score']  # Сортировка по убыванию очков

    def __str__(self):
        return f"{self.player_name}: {self.score}"
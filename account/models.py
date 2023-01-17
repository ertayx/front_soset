from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = False
        user.send_activation_code()
        user.save(using=self._db)
        return user
    
    
    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is required")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.is_active = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    username = models.CharField(max_length=150)
    activation_code = models.CharField(max_length=8, blank=True)
    student = models.ManyToManyField('User', blank=True, related_name='users')
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    about = models.TextField(max_length=1000, blank=True)

    LEVEL_CH = (
        ('elem', 'elementary'),
        ('pre', 'pre-intermediate'),
        ('inter', 'intermediate'),
        ('upper', 'upper-intermediate'),
        ('adv', 'advanced')
    )

    level = models.CharField(choices=LEVEL_CH, default='elem', max_length=50)
    teacher = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    

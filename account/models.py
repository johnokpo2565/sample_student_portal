from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser
import uuid
# Create your models here.




class CustomUserrManager(BaseUserManager):
    def _create_user(self, first_name, last_name, email, password=None, **extrafields):

        if not email:
            raise ValueError('Email is required')
        
        if not first_name:
            raise ValueError('First name is requires')
        
        if not last_name:
            raise ValueError('Last name is required')
        
        email = self.normalize_email(email)
        user = self.model(first_name=first_name, last_name=last_name, email=email, **extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self, first_name, last_name, email, password=None,  **extrafields):
        return self._create_user(first_name=first_name, last_name=last_name, email=email, password=password, 
                                  **extrafields)
    


    def create_superuser(self, first_name, last_name, email, password=None, **extrafields):
        extrafields.setdefault('is_staff',True)
        extrafields.setdefault('is_superuser', True)
        return self._create_user(first_name=first_name, 
                                 last_name=last_name, email=email, password=password, **extrafields)
    


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True)
    address = models.TextField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    objects = CustomUserrManager()

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'


class ProfilePics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    user = models.ForeignKey(User, related_name="profilepics", on_delete=models.CASCADE)
    attachment = models.FileField(upload_to="profile")





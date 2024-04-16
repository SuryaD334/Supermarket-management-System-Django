from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin, Group)

class UserManager(BaseUserManager):
    
    def create_user(self,username,email,password = None):
        if username is None:
            raise ValueError('Users should have a username')
        if email is None:
            raise ValueError('Users should have an Email')
        if password is None:
            raise ValueError('Users should have a password')
        
        user = self.model(username = username,email = self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.save(using = self._db)
        return user
    
    def create_superuser(self,username,email,password):
        
        user = self.create_user(username,email,password = password)
        user.is_admin = True
        user.save(using = self._db)
        return user
    
class User(AbstractBaseUser,PermissionsMixin):
    
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField(verbose_name = 'email_address',max_length = 255, unique = True)        
    is_active = models.BooleanField(default = True)
    is_admin = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    objects = UserManager()
    
    def __str__(self):
        return self.username
    
    def delete (self, using = None, keep_parents = False):
        self.is_active = False
        self.save()
        
    def get_full_name (self):
        return self.username
    
    def get_short_name(self):
        return self.username
    
    def has_perm(self, perm, obj = None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin
    
class Role(Group):
    description = models.TextField(max_length=100,unique=True)
    
    def __str__(self):
        return self.name
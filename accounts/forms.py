from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, Role

class UserCreationForm(forms.ModelForm):
        
        password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
        password2 = forms.CharField(label = 'Password Confirmation', widget = forms.PasswordInput)
        is_admin = forms.BooleanField(label = 'Is Admin', required = False, widget = forms.CheckboxInput)
        
        class Meta:
            model = User
            fields = ('username','email','is_admin')
            
        def clean_password2(self):
            password1 = self.cleaned_data.get('password1')
            password2 = self.cleaned_data.get('password2')
            
            if password1 and password2:
                if password1 != password2:
                    raise forms.ValidationError('Passwords do not match')
            else :
                raise forms.ValidationError('Password cannot be empty')
            return password2
        
        def save(self, commit = True):
            user = super(UserCreationForm,self).save(commit = False)
            user.set_password(self.cleaned_data['password1'])
            admin = self.cleaned_data.get('is_admin')
            if admin:
                user.is_admin = True
            if commit:
                user.save()
            return user
        
class UserChangeForm(forms.ModelForm):
        
        password = ReadOnlyPasswordHashField()
        
        class Meta:
            model = User
            fields = ('username','email','is_admin','is_active')
            
        def clean_password(self):
            return self.initial['password']
        
class UserRegisterForm(forms.ModelForm):
    
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username','email','password']
        
class RoleCreationForm(forms.ModelForm):
    
    class Meta:
        model = Role
        fields = ['name','description']
        
class EditRoleForm(forms.ModelForm):
    
    class Meta:
        model = Role
        fields = ['name','description']   
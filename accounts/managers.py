from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    
    def create_user(self, email, phone_number, fullname, password):
        if not phone_number:
            raise ValueError('User Must Have Phone Number')
        
        if not email:
            raise ValueError('User Must Have Email')
        
        if not fullname:
            raise ValueError('User Must Have FullName')
        
        #using normalize_email for validation email 
        user = self.model(phone_number=phone_number, email=self.normalize_email(email), fullname=fullname)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone_number, fullname, password):
        user = self.create_user(email, phone_number, fullname, password)
        user.is_admin = True
        user.is_superuser = True  
        user.save(using=self._db)
        return user

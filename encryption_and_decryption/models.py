from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User



class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Encryption(models.Model):
    encryption_value = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category

class Decryption(models.Model):
    decryption_value = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category

#login...............\


class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class Userr(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

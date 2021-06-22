from django.db import models
import re

from django.db.models.fields import CharField

class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern
            errors['email'] = "Invalid email format!"

        all_users = User.objects.all()      # section required to actually prevent entry of the email into db; AJAX gives user early notice
        for user in all_users:
            if postData['email'] == user.email:
                errors['email'] = "Email already in database. Choose another"

        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"

        return errors

class User(models.Model):
    fname = models.CharField(max_length=45)
    lname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()     # replaces the default value of objects = models.Manager() to custom version above  for validations
    # books_uploaded = a list of books "uploaded" by the User
    # liked_books = a list of books "liked" by the User

    def __repr__ (self):
        return f"<User Name: {self.fname} {self.lname} ID#: {self.id}>"

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(default="x")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uploaded_by_id = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")

    def __repr__ (self):
        return f"<Book: {self.title} Uploaded by: {self.uploaded_by_id}>"





# Create your models here.

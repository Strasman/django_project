from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
#from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
#from django.conf import settings
# Create your models here.


class Author(models.Model):
    # required to associate Author model with User model (Important)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    # additional fields
    activation_key = models.CharField(max_length=255, default=1)
    email_validated = models.BooleanField(default=False)

    def __str__(self):
        if self.user:
            return self.user.username
        else:
            return "No User"


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

    def get_absolute_url(self):
        return reverse('post_by_category', args=[self.slug])


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('post_by_tag', args=[self.slug])

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, 
        help_text="Slug will be generated automatically from the title of the post")
    content = RichTextUploadingField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)   

    def get_absolute_url(self):
      return reverse('post_detail', args=[self.id, self.slug]) 
    

class Feedback(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Feedback"

    def __str__(self):
        return self.name + "-" +  self.email
    
class Contact(models.Model):
    name = models.CharField(max_length=200, help_text="Name of the sender")
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Phone number")
    topic = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return f"{self.name} - {self.email}" 

"""
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
"""
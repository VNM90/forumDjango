from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.ForeignKey(
        User,  on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    category = models.ForeignKey(
        Category, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.title


class ForumUser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.user.username

    # def get_profile_pic(self):
    #     if self.profile_pic:
    #         return self.profile_pic
    #     else:
    #         pass
        # return 'default_img_url_path'

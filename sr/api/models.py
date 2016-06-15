from django.db import models

# Create your models here.

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    desc = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ["-created", "-modified"]

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     # return reverse("posts.views.post_detail", args=[str(self.id)])
    #     return reverse("onlineshop:index")

    # def get_absolute_url_detail(self):
    #     return reverse("onlineshop:detail", kwargs={"id": self.id})


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    desc = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ["-created", "-modified"]

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     # return reverse("posts.views.post_detail", args=[str(self.id)])
    #     return reverse("onlineshop:index")

    # def get_absolute_url_detail(self):
    #     return reverse("onlineshop:detail", kwargs={"id": self.id})
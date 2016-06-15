from django.db import models
from django.contrib.auth.models import User


# Create your models here.

from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
    user = models.ForeignKey(User, default=1)
    highlighted = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        
        """
        lexer = get_lexer_by_name(self.language)
        linenos = self.linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


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
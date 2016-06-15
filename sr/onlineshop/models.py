from django.db import models

# Create your models here.


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

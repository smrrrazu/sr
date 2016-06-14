from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

def upload_location(instance, filename):
    return "%s/s%" %(instance.id, filename)

# Post model
class Post(models.Model):

    # class Meta:
    # verbose_name = "MODELNAME"
    # verbose_name_plural = "MODELNAMEs"

    title = models.CharField(max_length=100,unique=True)
    # slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="upload_location",
                null=True, 
                blank=True, 
                height_field='height_field', 
                width_field='width_field')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    content = models.TextField()
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    modified = models.DateTimeField(auto_now=True,auto_now_add=False)


    class Meta:
        ordering = ["-created","-modified"]
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        #return reverse("posts.views.post_detail", args=[str(self.id)])
        return reverse("posts:index")

    def get_absolute_url_detail(self):
       return reverse("posts:detail", kwargs={"id": self.id})


   

class QualityManagerSchedule(models.Model):

    quality_managers = models.ManyToManyField(User, verbose_name='Quality managers', related_name='QM_schedule')
    year             = models.PositiveSmallIntegerField(verbose_name='Year')
    week             = models.PositiveSmallIntegerField(verbose_name='Week')

    class Meta:
        unique_together = ('year', 'week',)

    def get_qm_initials(self):
        return [ qm.upper() for qm in self.quality_managers.values_list('username', flat=True) ]
    
    def __str__(self):
        return "%s-%s %s" % (self.year, self.week, ', '.join(self.get_qm_initials()))

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline		



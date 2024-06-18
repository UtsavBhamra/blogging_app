from django.db import models
from django.conf import settings
from django.utils import timezone

# TAG_CHOICES = {
#     'CompSoc':'CompSoc',
#     'Diode':'Diode',
#     'Piston':'Piston',
#     'Aviation':'Aviation'
# }

TAG_CHOICES=[
    ('CompSoc','CompSoc'),
    ('Diode','Diode'),
    ('Piston','Piston'),
    ('Aviation','Aviation')
]

class Tag(models.Model):
    tag_name = models.CharField(max_length=50,choices=TAG_CHOICES)

    def __str__(self):
        return str(self.tag_name)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    blog_tag = models.ManyToManyField(Tag)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True,null=True)
    
    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return str(self.title)




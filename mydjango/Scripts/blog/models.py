from django.db import models
from django.utils import timezone
# from PIL import Image
# import PIL.image
# from pillow import image
# from PIL import Image

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    # image = models.TextField()
    dUrl = 'https://www.trwalamotywacja.pl/img/tripwire/trzy-kroki-okladka.png'

    # image = models.TextField(default='abc')
    image = models.ImageField(null=True, blank=True, upload_to='images/', default='images/car.png')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# Create your models here.

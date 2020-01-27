from django.db    import models
from django.conf  import settings
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def kek(self):
        print('ye it\'s here')
    
    def publish(self):
        self.published_date = timezone.now()
        print(self.published_date)
        print('publish u know blin')
        self.save()
    
    def __str__(self):
        return self.title

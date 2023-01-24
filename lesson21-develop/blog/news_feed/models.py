from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DateTimeMixin(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True) #нужно чтобы дополнительно могли \
    # наследоваться (чтобы эти два поля забрать себе в модель


class Page(models.Model):
    title = models.CharField(max_length=150)
    discription = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_privat = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.pk} - {self.title}" #pk тот же IDб только pk в больших вариантах может сработать



    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"
        
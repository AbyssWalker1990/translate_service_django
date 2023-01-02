from django.db import models
import uuid

# Create your models here.
class TranslationCard(models.Model):
    name = models.CharField(max_length=100)
    translate_request = models.TextField(max_length=2000, blank=True, null=True )
    image = models.ImageField(default="default.jpg", upload_to='uploaded')

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="document", null=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)

    public = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
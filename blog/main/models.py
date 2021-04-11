from django.db import models
from django.utils.timezone import now


class Author(models.Model):
    name = models.CharField("Author's Name", max_length=100)
    email = models.EmailField("Author's Email", max_length=100)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    class Meta:
        unique_together = ["email_to", "author_id"]
    email_to = models.EmailField("Subscriber's Email", max_length=100)
    author_id = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.email_to


class Post(models.Model):
    title = models.CharField("Title", max_length=100)
    description = models.CharField("Description", max_length=100)
    content = models.TextField("Text")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

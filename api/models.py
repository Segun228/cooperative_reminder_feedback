from django.db import models


class Message(models.Model):
    body = models.CharField(max_length=1000, null=False, blank=False)
    def __str__(self) -> str:
        return self.body
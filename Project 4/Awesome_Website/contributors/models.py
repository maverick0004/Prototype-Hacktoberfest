from django.db import models

class Contributor(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

from django.db import models

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return "{}:{}..".format(self.id, self.name)


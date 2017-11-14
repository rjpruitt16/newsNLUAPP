from django.db import models

class article(models.Model):
    title = models.CharField(max_length=25)
    date = models.DateTimeField()
    article_content = models.CharField(max_length=300)
    score = models.DecimalField(max_digits=1, decimal_places=1)
    magnitude = models.DecimalField(max_digits=1, decimal_places=1)

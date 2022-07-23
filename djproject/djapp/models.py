from django.db import models


class AppConfig(models.Model):
    identifier = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    admin_page_sufix = models.CharField(max_length=200)
    
    def __str__(self):
        return self.identifier


class Post(models.Model):
    title = models.CharField(max_length=200)
    resume = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

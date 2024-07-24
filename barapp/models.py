from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Worker(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service, blank=False)
    desc = models.TextField(blank=True, null=True)
    working_date = models.DateField()
    working_time = models.TimeField()
    ordered_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.ordered_date)



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)
    rew = models.TextField(max_length=100, blank=True)
    rew_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_reviews', blank=True)

    def __str__(self):
        return self.rew

class ShopReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rew = models.TextField()
    rew_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rew

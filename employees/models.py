from django.db import models


class Employee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='employees', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='')
    department = models.CharField(max_length=100, default='')

    class Meta:
        ordering = ['created']


def save(self, *args, **kwargs):
    super(Employee, self).save(*args, **kwargs)

from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    roles = models.ManyToManyField(to="Role")


    def __str__(self):
        return self.name


class Role(models.Model):
    tilte = models.CharField(max_length=32)
    permissions = models.ManyToManyField(to="Permission")

    def __str__(self):
        return self.tilte


class Permission(models.Model):
    title = models.CharField(max_length=32)
    url = models.CharField(max_length=32)
    action = models.CharField(max_length=32,default="")
    group = models.ForeignKey(to='PermissionGroup',default=1)

    def __str__(self):
        return self.title


class PermissionGroup(models.Model):

    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title





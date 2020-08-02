from django.db import models


# 사용자
class User(models.Model):
    user_id = models.AutoField(primary_key=True, default=1)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    birthday = models.DateField()
    cellphone = models.CharField(max_length=20)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.name

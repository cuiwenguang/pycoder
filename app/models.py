from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    mobile = models.CharField(max_length=20, null=True, blank=True)  # 手机
    email = models.CharField(max_length=50, null=True, blank=True)  # 邮箱
    name = models.CharField(max_length=20, null=True, blank=True)  # 姓名
    avatar = models.CharField(max_length=255, null=True, blank=True)  # 头像
    open_id = models.CharField(max_length=50, default='')  # 第三方登陆open_id
    provider = models.CharField(max_length=10)  # 第三方认证提供者
    points = models.IntegerField(default=0)  # 用户积分

    def __str__(self):
        return self.name


channels = ["java", "python", "前端"]

class Series(models.Model):
    ''' 课程系列 '''
    ser_name = models.CharField(max_length=20)
    ser_remark = models.CharField(max_length=255)
    part_count = models.IntegerField(default=1)
    cover_img = models.CharField(max_length=255)
    teacher = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL)


class Course(models.Model):
    category = models.ForeignKey(Series, on_delete=models.SET_DEFAULT)
    course_name = models.CharField(max_length=50)
    course_index = models.IntegerField(default=0)
    course_remark = models.CharField(max_length=500, null=True, blank=True)


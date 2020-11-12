# -*- coding: utf-8 -*-

# @File    : auth.py
# @Date    : 2020-11-12
# @Author  : wdmeng
import hashlib

from django.db import models


def hash_password(password):
    if isinstance(password, str):
        password = password.encode('utf-8')
    return hashlib.md5(password).hexdigest().upper()


class ClientUser(models.Model):
    sex = (
        ('male', '男'),
        ('female', '女'),
    )
    username = models.CharField(max_length=50, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    avatar = models.CharField(max_length=500, default='')
    gender = models.CharField(max_length=10, choices=sex, default='男')
    birthday = models.DateTimeField(null=True, blank=True, default=None)
    status = models.BooleanField(default=True, db_index=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'username:{}'.format(self.username)

    @classmethod  # 修饰符 不需要实例化就可以被类本身调用（类方法）
    def add(cls, username, password, avatar='', gender='', birthday=None):
        """创建普通用户函数"""
        return cls.objects.create(
            username=username,
            password=hash_password(password),
            avatar=avatar,
            gender=gender,
            birthday=birthday,
            status=True
        )

    @classmethod
    def get_user(cls, username, password):
        """获取用户信息函数"""
        try:
            user = cls.objects.get(
                username=username,
                password=hash_password(password)
            )
            return user
        except:
            return None

    def update_password(self, old_password, new_password):
        hash_old_password = hash_password(old_password)
        if hash_old_password != self.password:
            return False
        hash_new_password = hash_password(new_password)
        self.password = hash_new_password
        self.save()
        return True

    def update_status(self):
        self.status = not self.status
        self.save()
        return True

    class Meta:
        ordering = ['-create_time']
        verbose_name = "用户名"
        verbose_name_plural = "用户名"

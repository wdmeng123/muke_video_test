# -*- coding: utf-8 -*-

# @File    : video.py
# @Date    : 2020-11-12
# @Author  : mengwudi
from enum import Enum
from django.db import models


class VideoType(Enum):
    movie = 'movie'
    cartoon = 'cartoon'
    episode = 'episode'
    variety = 'variety'
    other = 'other'


VideoType.movie.label = '电影'
VideoType.cartoon.label = '动漫'
VideoType.episode.label = '剧集'
VideoType.variety.label = '综艺'
VideoType.other.label = '其他'


class FromType(Enum):
    youku = 'youku'
    custom = 'custom'


FromType.youku.label = '优酷'
FromType.custom.label = '自制'


class NationalityType(Enum):
    china = 'china'
    japan = 'japan'
    korea = 'korea'
    america = 'america'
    other = 'other'


NationalityType.china.label = '中国'
NationalityType.japan.label = '日本'
NationalityType.korea.label = '韩国'
NationalityType.america.label = '美国'
NationalityType.china.label = '其他'


class Video(models.Model):
    name = models.CharField(max_length=100, null=False)
    image = models.CharField(max_length=500, default='')
    video_type = models.CharField(max_length=50, default=VideoType.other.value)
    from_to = models.CharField(max_length=20, null=False, default=FromType.custom.value)
    nationality = models.CharField(max_length=20, default='')

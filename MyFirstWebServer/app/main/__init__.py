#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'NapoleonYoung'

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors # . 代表当前文件所在的目录里，在末尾导入这两个模块是为了避免循环导入依赖，因为在views.py errors.py中还要导入蓝本


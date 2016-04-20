#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'NapoleonYoung'

import os

basedir = os.path.abspath(os.path.dirname(__file__))    #文件路径

class Config:   #基类Config,包含通用配置，在下面的子类Config中分别定义专用的配置
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '906469826@qq.com'  #上传github前将邮箱名去掉
    MAIL_PASSWORD = 'okgrvzyhmimubfaa' #此处应该为所用邮箱的授权码，去设置／开启POP3/SMTP服务
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):    #子类Config，分别定义专用的配置
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):    #子类Config，分别定义专用的配置
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-test.qulite')

class ProductionConfig(Config):    #子类Config，分别定义专用的配置
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'Production': ProductionConfig,

    'default': DevelopmentConfig

}
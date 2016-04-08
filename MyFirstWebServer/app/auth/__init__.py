#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'NapoleonYoung'

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views

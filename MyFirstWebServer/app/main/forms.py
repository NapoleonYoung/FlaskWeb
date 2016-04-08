#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'NapoleonYoung'

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

class NameForm(Form):
    name = StringField('What is your name?', validators=[InputRequired()])
    submit = SubmitField('Submit')


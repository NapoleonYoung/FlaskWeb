#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'NapoleonYoung'

from . import main
from .forms import NameForm
from flask import render_template

@main.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('index.html', form=form, name=name)

#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'NapoleonYoung'

from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(Form):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[InputRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,'Usernames must have only letters, numbers, dots or underscores')])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[InputRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('username already in use.')

class ChangePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[InputRequired()])
    password = PasswordField('New password', validators=[InputRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm new password', validators=[InputRequired()])
    submit = SubmitField('Update Password')

class PasswordResetRequestForm(Form):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    submit = SubmitField('Reset Password')

class PasswordResetForm(Form):
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    password = PasswordField('New Password', validators=[InputRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[InputRequired()])
    submit = SubmitField('Reset Passwrod')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first is None:
            raise ValidationError('Unknown email address.')

class ChangeEmailForm(Form):
    email = StringField('New Email', validators=[InputRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')


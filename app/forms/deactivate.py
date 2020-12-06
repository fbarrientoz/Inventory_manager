#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Product Form """


from flask_wtf import FlaskForm
from wtforms import SubmitField, Label

class DeleteProduct(FlaskForm):
    id = Label
    submit = SubmitField("Delete")

class ActivateProduct(FlaskForm):
    id = 
    submit = SubmitField("Un-Delete")
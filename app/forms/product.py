#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Product Form """


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField("What is the product?", validators=[DataRequired()])
    price = StringField("How much does it cost?", validators=[DataRequired()])
    description = StringField("Enter a description of the product: ", validators=[DataRequired()])
    category = StringField("Category?", validators=[DataRequired()])
    quantity = StringField("Quantity?", validators=[DataRequired()])
    unique_tag = StringField("Unique tag?", validators=[DataRequired()])
    submit = SubmitField("Submit")
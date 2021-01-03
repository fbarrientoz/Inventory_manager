from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired
from wtforms import validators


class ProductReview(FlaskForm):

    id = RadioField(choices=[], validators=[DataRequired()])

   
    body = TextAreaField("Tell Us Your Thoughts", [validators.optional(), validators.length(max=200)])

    
    submit = SubmitField("Submit")

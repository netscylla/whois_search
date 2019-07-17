from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,NumberRange

class WhoisForm(FlaskForm):
    keyword = StringField('Keyword', validators=[DataRequired()])
    days=DecimalField('days', validators=[NumberRange(min=0,max=14,message="Days must be a between 1 - 14"),DataRequired()],default=14)
    submit = SubmitField('Search')

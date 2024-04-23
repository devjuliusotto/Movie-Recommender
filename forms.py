from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    genre = StringField('Genre', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

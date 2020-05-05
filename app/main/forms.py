from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from flask_login import login_required
from .. import db

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Pitch review', validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):

    category = StringField('Review title',validators=[Required()])
    pitch = TextAreaField('Pitch ', validators=[Required()])
    submit = SubmitField('Submit')
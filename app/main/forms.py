from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required
# from flask_login import login_required
from .. import db

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    comment = TextAreaField('comment', validators=[Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):

    title = StringField('TITLE',validators=[Required()])
    description = TextAreaField('PITCH', validators=[Required()])
    submit = SubmitField('Submit')
 
from flask import (render_template, url_for, flash,redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from . import db
from models import Pitch
from pitch import PitchForm

pitch = Blueprint('pitch', __name__)


@pitch.route("/pitch/new", methods=['GET', 'POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(category=form.category.data, content=form.content.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('Your post has been created!', 'success')
        # return redirect(url_for('main.home'))
    return render_template('create_pitch.html', title='New Post', form=form, legend='New Post')


@pitch.route("/pitch/<int:pitch_id>")
def pitch(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    return render_template('post.html', title=post.title, post=post)


@pitch.route("/pitch/<int:pitch_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(pitch_id):
    pitch = Pitch.query.get_or_404(pitch_id)
    if pitch.author != current_user:
        abort(403)
    form = PitchForm()
    if form.validate_on_submit():
        pitch.category = form.category.data
        pitch.content = form.content.data
        db.session.commit()
        flash('Your pitch has been updated!', 'success')
        return redirect(url_for('pitches.pitch', pitch_id=pitch.id))
    elif request.method == 'GET':
        form.category.data = pitch.category
        form.content.data = pitch.content
    return render_template('create_pitch.html', title='Update Post', form=form, legend='Update Post')


@pitch.route("/pitch/<int:pitch_id>/delete", methods=['POST'])
@login_required
def delete_pitch(post_id):
        pitch = pitch.query.get_or_404(post_id)
        if pitch.author != current_user:
            abort(403)
        db.session.delete(post)
        db.session.commit()
        flash('Your post has been deleted!', 'success')
        # return redirect(url_for('main.home'))



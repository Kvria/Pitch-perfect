from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm,UpdateProfile,PostForm
from ..models import User,Post
from .. import db
from flask_login import login_required, current_user
# import markdown2 

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/<uname>/update',methods = ['GET','POST'])
# @login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/posts/',methods= ['POST','GET'])
@login_required
def posts():
    form = PostForm()

    title = form.title.data
    description = form.description.data

    all_post = 


    if form.validate_on_submit():
        new_post = Post(title = title, description = description, user = current_user)
        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('main.posts'))

    return render_template('posts.html',form =form)

from . import db

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch:
    '''
    Pitch class to define pitch Objects
    '''
    all_pitches = []

    def __init__(self,id,category,pitch_idea,vote_count):
        self.id =id
        self.category = category
        self.pitch_idea = pitch_idea
        self.vote_count = vote_count

    def save_pitch(self):
        Pitch.all_pitches.append(self)

    
    @classmethod
    def clear_pitch(cls):
        Pitch.all_pitches.clear()

class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    pitch_idea = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    vote_count = db.Column(db.Integer)

class Review(db.Model):
    __tablename__ = 'reviews'
     
    def save_review(self):
        db.session.add(self)
        db.session.commit()

class Review:

    all_reviews = []

    def __init__(self,pitch_id,category,review):
        self.movie_id = movie_id
        self.category = category
        self.review = review


    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls,id):

        response = []

        for review in cls.all_reviews:
            if review.movie_id == id:
                response.append(review)

        return response


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    pitches = db.relationship('Pitch',backref = 'review', lazy = "dynamic")

@property
def password(self):
    raise AttributeError('You cannot read the password attribute')

@password.setter
def password(self, password):
    self.pass_secure = generate_password_hash(password)


def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)

def __repr__(self):
    return f'User {self.username}'

class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer)
    pitch_category = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

class Review(db.Model):
    __tablename__ = 'reviews'
     
    def save_review(self):
        db.session.add(self)
        db.session.commit()

@classmethod
def get_reviews(cls,id):
    reviews = Review.query.filter_by(pitch_id=id).all()
    return reviews
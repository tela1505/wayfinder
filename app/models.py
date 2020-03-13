from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    userId = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    university = db.Column(db.String(250), nullable=False)
    password = db.Column(db.Text, nullable=False)

    # __mapper_args__ = {
    #     "polymorphic_identity": "users",
    #     "polymorphic_on": user_type }

    def get_id (self):
        return (self.userId)

    def __repr__ (self):
        return '<User {}>'.format (self.username)

    def set_password (self, password):
        self.password = generate_password_hash (password)

    def check_password (self, password):
        return check_password_hash (self.password, password)


class Post(db.Model):
    __tablename__ = 'posts'
    postId = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(250), nullable=False)
    title = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    posterId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)
    tags = db.Column(db.String(250), nullable=False)
    likes = db.Column(db.Integer, nullable=False)


class Relationship(db.Model):
    __tablename__ = 'relationship'
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'), primary_key=True)
    followingId = db.Column(db.Integer, nullable=False)


class Weight(db.Model):
    __tablename__ = 'weight_measurements'
    weightEntryId = db.Column(db.Integer, primary_key=True)
    weight = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(250), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)


class Sleep(db.Model):
    __tablename__ = 'sleep_measurements'
    sleepEntryId = db.Column(db.Integer, primary_key=True)
    sleep = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(250), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)


class Grade(db.Model):
    __tablename__ = 'grade_measurements'
    gradeEntryId = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.Integer, nullable=False)
    gradeSubject = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)

class Comment(db.Model):
    __tablename__ = 'comments'
    content = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable = False)
    commenterId = db.Column(db.Integer, db.ForeignKey('users.userId'), nullable=False)
    commentId = db.Column(db.Integer, primary_key=True)
    commentedPostId = db.Column(db.Integer, db.ForeignKey('posts.postId'), nullable=False)


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

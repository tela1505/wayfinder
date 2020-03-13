from flask import render_template, Blueprint, request, flash, redirect, url_for
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from app import db

from app.main.forms import SignupForm
from app.models import User
from app.models import Post
from app.models import Comment
from app.main.forms import CreatePostForm
from app.main.forms import CreateComment
from flask_login import current_user
from datetime import date
bp_main = Blueprint('main', __name__)


@bp_main.route('/')
def home():  # also called index

    # Post.query.delete()
    post_list = Post.query.all()


    for post in post_list:
        print(post.posterId, '!!!!')
        user = User.query.filter(User.userId==post.posterId).all()
        # username = user.username
        print(user, '=-=-=-=-=-=-=-=-')

    comment_list = Comment.query.all()

    # comments_list = Comment.query.all()


    return render_template('index.html', post_list=post_list, comment_list=comment_list)



@bp_main.route('/myFriends', methods=['POST', 'GET'])
def myFriends():
    post_list =Post.query.all()
    return render_template('myFriends.html')


@bp_main.route('/myProfile', methods=['POST', 'GET'])
def myProfile():

    return render_template('personal_profile')


@bp_main.route('/users/<name>', methods=['POST', 'GET'])
def public_profile(name=None):
    username = User.username
    return render_template('public_profile.html', name=name)


@bp_main.route('/create_post', methods=['POST', 'GET'])
def create_post():
    form = CreatePostForm(request.form)
    if request.method == 'POST':
        post = Post(content=form.content.data, title=form.title.data, date=date.today(), likes=0, posterId=current_user.userId,
                    tags=form.tags.data)
        db.session.add(post)
        db.session.commit()

        user = User.query.filter(User.userId==post.posterId).all()

            # username = user.username
        print(user, '=-=-=-=-=-=-=-=-')
        flash('the post was added successfully!')

        return render_template('index.html')

    return render_template('create_post.html', form=form)

@bp_main.route('/<postId>/comment', methods=['GET', 'POST'])
def create_comment(postId):
    form = CreateComment(request.form)
    if request.method == 'POST':
        comment = Comment(content=form.content.data, date=date.today(), commenterId=current_user.userId,
                    commentedPostId=postId)
        db.session.add(comment)
        db.session.commit()
        post = Post.query.filter(Post.postId == Comment.commentedPostId).all()
        flash('the comment was added successfully!')

        return render_template('index.html')

    return render_template('create_comment.html', form=form)


@bp_main.route('/like/<postId>', methods=['GET', 'POST'])
def like(postId):
    print('liking', postId)
    likedPost = Post.query.filter(Post.postId == postId).first()
    print(likedPost)
    likedPost.likes += 1

    db.session.commit()
    return redirect('/')

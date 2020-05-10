from flask import render_template, url_for, flash, redirect
from . import main
from ..import db, bcrypt
from .forms import RegistrationForms, LoginForms, PostForm, CommentForm
from ..models import User, Post, Comment
from flask_login import login_user, current_user, logout_user, login_required
# from ..request import get_quote


# Views
@main.route('/')  
def home():
    blogs = Post.query.all()

    '''
    View root page function that returns the index page and its data
    '''
    # quote = get_quote()
    return render_template('home.html', blogs=blogs )

@main.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForms()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title= 'Register', form=form)

@main.route('/login',methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForms()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html', title= 'login', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/post/new',methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created','success')
        return redirect(url_for('main.home'))
    return render_template('new_post.html', title='New Post',form=form)

@main.route('/post/<int:post_id>',methods=['GET','POST'])
@login_required
def blog(post_id):
    blog = Post.query.get_or_404(post_id)
    # comments = Comment.query.filter_by(id=blog.id)
    comments = Comment.query.all()
    form = CommentForm()
    if form.validate_on_submit():
        comments = Comment(content = form.content.data, author=current_user)
        db.session.add(comments)
        db.session.commit()
        flash('Your comment has been posted')
        return redirect(url_for('main.home'))
    return render_template('blog.html', title=blog.title, blog=blog, comments=comments,form=form)

# @main.route('/comment/<int:comment_id>',methods=['GET','POST'])
# @login_required
# def comment(comment_id):
#     form = CommentForm()
#     if form.validate_on_submit():
#         comment = Comment(content = form.content.data, author=current_user)
#         db.session.add(comment)
#         db.session.commit()
#         flash('Your comment has been posted')
#         return redirect(url_for('main.home'))
#     return render_template('new_comment.html', title='Commenting', form=form)
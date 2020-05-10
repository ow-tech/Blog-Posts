from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User, Post, Comment

class RegistrationForms(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username already TAKEN. PLease Choose another')   

    def validate_email(self, email):
            email = User.query.filter_by(email = email.data).first()
            if email:
                raise ValidationError('Email already used. Use a different One') 

class LoginForms(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember =BooleanField('Remember Me')
    submit = SubmitField('Login')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Your Blog', validators=[DataRequired()])
    submit = SubmitField('Post')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment..', validators=[DataRequired()])
    submit = SubmitField('Post Comment')

from flask import render_template, url_for, flash, redirect
from app import app
from forms import RegistrationForms, LoginForms


#dammy post
blogs =[
    {
        'author': "alex Barasa",
        'title': "Blog Post Alex",
        'content':"First post content",
        'date_password': "April 20, 2020"
    },
    {
    'author': "Loda Kim",
    'title': "Blog Post Kim",
    'content':"Second post content",
    'date_password': "April 20, 2020"
    }
]

# Views
@app.route('/')
def home():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('home.html', blogs = blogs)

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForms()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title= 'Register', form=form)

@app.route('/login',methods = ['GET', 'POST'])
def login():
    form = LoginForms()
    if form.validate_on_submit():
        if form.username.data =='admin' and form.password.data=='password':
            flash(f'You have been logged in {form.username.data}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password','danger')
    return render_template('login.html', title= 'login', form=form)
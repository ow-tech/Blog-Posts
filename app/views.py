from flask import render_template, flash, redirect
from app import app
from forms import RegistrationForms, LoginForm


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
    return render_template('register.html', title= 'Register' form=form)

@app.route('/login',methods = ['GET', 'POST'])
def login():
    form = LoginForms()
    return render_template('login.html', title= 'login' form=form)
from flask import render_template, url_for, flash, redirect
from flaskblog import app 
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
    {
        'author': 'Wai Chong',
        'title': 'Blog Post 1',
        'content': 'first post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Q Ma',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'April 2021, 2018'
    }
]

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    print(posts)
    return render_template('home.html', posts=posts)

@app.route("/about", methods=["GET"]) 
def about():
    print("goodbye")
    return render_template('about.html', title='About')


@app.route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '59950d6ff3a417f45d7066fe2d7c64de5'

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

@app.route("/add-post", methods=["POST"])
def add_post():
    request_data = request.get_json()
    print(request_data)
    return request_data["author"]

@app.route("/register", methods=['GET', 'POST'])
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

if __name__ == '__main__':
    app.run(debug=True)

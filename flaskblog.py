from flask import Flask, render_template, url_for

app = Flask(__name__)

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

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)

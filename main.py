from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask('app')

arr.config['SECRET_KEY'] = '34e2ee1548491bcf261d357431cf64e9'
posts = [{
    'author': 'Junsoo',
    'title': 'Flaskblog 1',
    'content': 'First post content',
    'date_posted': 'April 20, 2018'
}, {
    'author': 'Seung',
    'title': 'Flaskblog 2',
    'content': 'Second post content',
    'date_posted': 'April 21, 2018'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', posts=posts)  # Arguments = data


@app.route('/about')
def about():
  return render_template('about.html', title='About')  # Static


@app.route('/register')
def register():
  form = RegistrationForm()
  return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html', title='Login', form=form)


'''
__name__ == "__main__" is used when you 
directly run the file by interpreter instead of importing other modules.

__name__ means global variable that python interpreter already made before running the file. == Built-in variable.
'''
app.run(host='0.0.0.0', port=8080, debug=True)

# https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3 Bootstrap

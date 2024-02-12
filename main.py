from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask('app')

app.config['SECRET_KEY'] = '34e2ee1548491bcf261d357431cf64e9'
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
def home():
  return render_template('home.html', posts=posts)  # Arguments = data


@app.route('/about')
def about():
  return render_template('about.html', title='About')  # Static


@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    flash(f'Account created for {form.username.data}!', 'success')
    return redirect(url_for('home'))
  return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=["POST", "GET"])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    if form.email.data == 'admin@blog.com' and form.password.data == 'password':
      flash('You have been logged in!', 'success')
      return redirect(url_for('home'))
    else:
      flash('Login Unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title='Login', form=form)


'''
__name__ == "__main__" is used when you 
directly run the file by interpreter instead of importing other modules.

__name__ means global variable that python interpreter already made before running the file. == Built-in variable.
'''
app.run(host='0.0.0.0', port=8080, debug=True)

# https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3 Bootstrap
# https://www.geeksforgeeks.org/flask-wtf-explained-how-to-use-it/

# https://www.geeksforgeeks.org/get-post-requests-using-python/

# https://www.freecodecamp.org/news/build-basic-forms-with-html/ forms html

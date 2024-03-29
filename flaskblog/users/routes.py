from flask import Blueprint, redirect, url_for, render_template, request, flash
from flask_login import current_user, login_required, login_user, logout_user
from flaskblog.models import User, Post
from flaskblog import db, bcrypt
from flaskblog.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from flaskblog.users.utils import save_picture

users = Blueprint('users', __name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = RegistrationForm()
  if form.validate_on_submit():
    hashed_password = bcrypt.generate_password_hash(
        form.password.data).decode('utf-8')
    user = User(username=form.username.data,
                email=form.email.data,
                password=hashed_password)
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! You are now able to log in',
          'success')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('home'))
  form = LoginForm()
  if form.validate_on_submit():
    # Get the user from the database
    user = User.query.filter_by(email=form.email.data).first()
    # Check if the user exists and the password is correct
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      # Log the user in
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      for key, value in request.args.items():
        print(key, value)
      flash('Login successful!', 'success')
      return redirect(next_page) if next_page else redirect(url_for('home'))
    else:
      # The user does not exist or the password is incorrect
      flash('Login Unsuccessful. Please check username and password', 'danger')
  return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
  # Log the user out
  logout_user()
  return redirect(url_for('home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
  form = UpdateAccountForm()
  if form.validate_on_submit():
    if form.picture.data:
      picture_file = save_picture(form.picture.data)
      current_user.image_file = picture_file
    current_user.username = form.username.data
    current_user.email = form.email.data
    db.session.commit()
    flash('Your accout has been updated!', 'success')
    return redirect(url_for('account'))
  # PTG pattern
  elif request.method == "GET":
    form.username.data = current_user.username
    form.email.data = current_user.email

  image_file = url_for('static',
                       filename='profile_pics/' + current_user.image_file)
  return render_template('account.html',
                         title='Account',
                         image_file=image_file,
                         form=form)


@users.route("/user/<string:username>")
def user_posts(username):
  page = request.args.get('page', 1, type=int)
  user = User.query.filter_by(username=username).first_or_404()
  posts = Post.query.filter_by(author=user)\
  .order_by(Post.date_posted.desc())\
  .paginate(page=page,per_page=5)
  return render_template('user_posts.html', posts=posts, user=user)

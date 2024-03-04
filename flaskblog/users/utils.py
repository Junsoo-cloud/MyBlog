import secrets
import os
from flaskblog import app
from PIL import Image


def save_picture(form_picture):
  random_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(form_picture.filename)  # return name, ext itself
  print(f'f_ext is {f_ext}')
  picture_fn = random_hex + f_ext
  print(f'picture_fn is {picture_fn}')
  picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
  # Image resizing with Pillow package
  output_size = (125, 125)
  i = Image.open(form_picture)
  i.thumbnail(output_size)
  print(f'app.root_path is {app.root_path}')
  print(f'picture_path is {picture_path}')
  i.save(picture_path)
  return picture_fn

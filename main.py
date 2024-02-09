from flask import Flask, render_template

app = Flask('app')

posts = [{
    'author': 'Junsoo',
    'title': '해윤이와 곧 일년',
    'content': 'First post content',
    'date_posted': 'April 20, 2018'
}, {
    'author': 'Seung',
    'title': '정해윤 사랑해',
    'content': 'Second post content',
    'date_posted': 'April 21, 2018'
}]


@app.route('/')
def hello_world():
  return render_template('home.html', posts=posts)  # Arguments = data


@app.route('/about')
def about():
  return render_template('about.html', title='About')  # Static


'''
__name__ == "__main__" is used when you 
directly run the file by interpreter instead of importing other modules.

__name__ means global variable that python interpreter already made before running the file. == Built-in variable.
'''
app.run(host='0.0.0.0', port=8080, debug=True)

# https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=3 Bootstrap

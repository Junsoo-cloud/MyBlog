from flask import Flask, render_template

app = Flask('app')


@app.route('/')
def hello_world():
  return render_template('home.html')


@app.route('/about')
def about():
  return render_template('about.html')


'''
__name__ == "__main__" is used when you 
directly run the file by interpreter instead of importing other modules.

__name__ means global variable that python interpreter already made before running the file. == Built-in variable.
'''
app.run(host='0.0.0.0', port=8080, debug=True)

# https://www.youtube.com/watch?v=QnDWIZuWYW0&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2  4:41까지 시청

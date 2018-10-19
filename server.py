from flask import Flask, url_for
app = Flask(__name__)  # __main__


@app.route('/')
def index():
    return "Hello world!"


@app.route('/user/<username>')
def hello_user(username):
    return "Hello %s" % username


#def decorator(func):
 #   print('pre_function')
  #  func()
   # print('post_function')


#@decorator
#def test():
 #   print('test')

with app.test_request_context():
    print("http://localhost" + url_for('hello_user', username='Sofia the best'))


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

hello_user()

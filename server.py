from flask import Flask, url_for, render_template
app = Flask(__name__)  # __main__


@app.route('/')
def index():

    with app.test_request_context():
         link = url_for('hello_user', username='Sofia the best')


    return render_template('index.html', link=link)

@app.route('/user/')
@app.route('/user/<username>')
def hello_user(username=None):
    numbers = [0, 1, 2, 3, 4, 5, 6]
    return render_template(
        'userfile.html',
        username=username,
        numbers=numbers
    )


#def decorator(func):
 #   print('pre_function')
  #  func()
   # print('post_function')


#@decorator
#def test():
 #   print('test')




if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

hello_user()

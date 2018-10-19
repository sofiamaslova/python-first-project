from flask import Flask, url_for, render_template
app = Flask(__name__)  # __main__


@app.route('/')
def index():
    links = generate_links()
    return render_template('index.html', links=links)




    return render_template('index.html', link=link)
def generate_links():
    with app.test_request_context():
        danil_the_great_link = url_for('hello_user', username='"Danil the great')
        sofia_the_best_link = url_for('hello_user', username='Sofia the best')
        index_link = url_for('index')
        links = (
            ("Sofia's page", sofia_the_best_link),
            ("Danil's page", danil_the_great_link),
            ('Index', index_link),
        )


    return links


@app.route('/user/')
@app.route('/user/<username>')
def hello_user(username=None):
    links = generate_links()
    return render_template(
        'userfile.html',
        username=username,
        links=links,
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

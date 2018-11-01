from flask import Flask, url_for, render_template
app = Flask(__name__)  # __main__


@app.route('/')
def index():
    links = generate_links()
    slides = [
        {'image_src': 'https://images1.popmeh.ru/upload/img_cache/6be/6be92ece8078d7ff0ee207a73b31fe4f_ce_1920x1200x0x0_cropped_800x427.jpg',
         'title_src': 'Бурдж-Халифа, Дубай',
         'heading': 'Бурдж-Халифа, Дубаи',
         'explanation': 'Бурдж-Халифа - самое высокое здание в мире'},
        {'image_src': 'https://fountravel.ru/wp-content/uploads/2016/02/Campanile-San-Marco-Venice-1.jpg', 'title_src': 'Сан-Марко, Венеция','heading': 'Бурдж-Халифа, Дубаи',
         'explanation': 'Бурдж-Халифа - самое высокое здание в мире'},
        {'image_src': 'https://planetofhotels.com/sites/default/files/styles/attractionimageoriginal/public/sobor_duomo_v_milane_1_0.jpg?itok=6h97nmsB',
         'title_src': 'Дуомо, Милан'},
        {'image_src': 'https://i.archi.ru/i/650/146330.jpg',
         'title_src': 'Феррари Ворлд, Абу-Даби',
         'heading': 'Феррари Ворлд, Абу-Даби',
         'explanation': 'Тематический парк Феррари является крупнейшим в мире крытым парком, его территория занимает более 86 тысяч'}

    ]

    return render_template('index.html', links=links, slides=slides)


def generate_links():
    with app.test_request_context():
        danil_the_great_link = url_for('hello_user', username='"Danil the great')
        sofia_the_best_link = url_for('hello_user', username='Sofia the best')
        index_link = url_for('index')
        index_with_params_link = url_for('index', param1='param1', param2='param2')
        links = {
            "Sofia's page": sofia_the_best_link,
            "Danil's page": danil_the_great_link,
            'Index': index_link,
            'Index with params': index_with_params_link,
        }



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

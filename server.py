import pymysql
from flask import Flask, url_for, render_template
from Repository_shop import shop
app = Flask(__name__)  # __main__

connection = pymysql.connect(
    host='192.168.33.10',
    user='remote_user',
    password='123456',
    db='shop',
    charset = 'utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

@app.route('/test/')
def test():
    with connection.cursor() as cursor:
    #cursor = connection.cursor()
        cursor.execute('SELECT * FROM product')
        result = cursor.fetchall()

    return str(result)


@app.route('/')
def index():
    categories = shop.find_all_categories()
    slides = list()
    for x in categories:
        slide = {
            'category_id': x.get('id'),
            'heading': x.get('title'),
            'image_title': x.get('title'),
            'subheading': x.get('description'),
            'image_url': x.get('image_url')
        }
        slides.append(slide)
            #       cursor.execute("""
            # SELECT product.title AS title, product.description AS description,
            #          product.price AS price, image.description AS image_description, image.image_url AS image_url,
            #          product.category_id AS category_id
            #          FROM product
            #          INNER JOIN image
            #          ON image.product_id = product.id
            #          """)
            # slides = cursor.fetchall()

    return render_template('index.html', slides=slides)


# def generate_links():
#     with app.test_request_context():
#         danil_the_great_link = url_for('hello_user', username='"Danil the great')
#         sofia_the_best_link = url_for('hello_user', username='Sofia the best')
#         index_link = url_for('index')
#         index_with_params_link = url_for('index', param1='param1', param2='param2')
#         links = {
#             "Sofia's page": sofia_the_best_link,
#             "Danil's page": danil_the_great_link,
#             'Index': index_link,
#             'Index with params': index_with_params_link,
#         }
#
#
#
#     return links
#
@app.route('/category/<int:category_id>')
def find_category():
     category = shop.find_category(category_id)
     products = shop.find_products_by_category(category_id)

     return render_template('category.html', products=products)

# @app.route('/<category_id>')
# def categories(category_id):
#     with connection.cursor() as cursor:
#
#         cursor.execute("""
#             SELECT product.title AS title, product.description AS description,
#                      product.price AS price, image.description AS image_description, image.image_url AS image_url
#                      FROM product
#                      INNER JOIN image
#                      ON image.product_id = product.id
#                      WHERE category_id={}
#                      """.format(category_id))
#         slides = cursor.fetchall()
#         return render_template('index.html', slides=slides)

# @app.route('/user/<username>')
# def hello_user(username=None):
#     links = generate_links()
#     return render_template(
#         'userfile.html',
#         username=username,
#         links=links,
#     )


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

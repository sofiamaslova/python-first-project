import pymysql

connection = pymysql.connect(
    host='192.168.33.10',
    user='remote_user',
    password='123456',
    db='shop',
    charset = 'utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)


def find_category(category_id):
    with connection.cursor() as cursor:
        cursor.execute('''
                SELECT 
                    title,
                    id,
                    description,
                    image_url
                FROM category
                WHERE id = %s
                ''', (category_id,))
        category = cursor.fetchone()

    return category


def find_all_categories():
    with connection.cursor() as cursor:
    # cursor = connection.cursor()
        sql = """
        SELECT title,
               id,
               description,
               image_url
        FROM category"""
        cursor.execute(sql)
        categories = cursor.fetchall()

    return categories


def find_products_by_category(category_id):
    with connection.cursor() as cursor:
        sql = """
        SELECT 
            p.title,
            p.id,
            description,
            price,
            category_id
            i.id AS image_id,
            i.title AS image_title,
            i.image_url AS image_url
        FROM product p
        LEFT JOIN image i
        ON i.product_id = p.id
        WHERE category_id = %s
        """
        cursor.execute(sql, (category_id,))
        products = cursor.fetchall()
        
    return products
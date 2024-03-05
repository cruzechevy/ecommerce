from db import db 

cur = db.conn.cursor()

def get_all_product():
    try:
        cur.execute('SELECT * FROM products')
        products = cur.fetchall()
        if products is None:
            return []
        return products
    except:
        return []

def get_product(id):
    try:
        if id :
            cur.execute('SELECT * FROM products WHERE id = %s', (id,))
            product = cur.fetchone()

            if product is None:
                return {}
            return product
        else:
            return {}
    except:
        return {}
    

def create_product(product):
    try:
        print(product)
        cur.execute('INSERT INTO products (name, description, stock, price) VALUES (%s, %s, %s, %s)', (product['name'], product['description'], product['stock'], product['price']))
        db.conn.commit()
        new_product_id = cur.lastrowid
        return get_product(new_product_id)
    except:
        return {}


def update_product(id, product):
    try:
        print(product)
        cur.execute('UPDATE products SET name = %s, description = %s,stock = %s, price = %s WHERE id = %s', (product['name'], product['description'],product['stock'], product['price'], id))
        db.conn.commit()
        return get_product(id)
    except:
        return {}

def delete_product(id):
    try:
        cur.execute('DELETE FROM products WHERE id = %s', (id,))
        db.conn.commit()
        deleted_id = cur.lastrowid
        return deleted_id
    except:
        return 0
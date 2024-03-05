from db import db 

cur = db.conn.cursor()

def get_all_order():
    try:
        cur.execute('SELECT * FROM orders')
        orders = cur.fetchall()
        if orders is None:
            return []
        return orders
    except:
        return []

def get_order(id):
    try:
        if id :
            cur.execute('SELECT * FROM orders WHERE id = %s', (id,))
            order = cur.fetchone()

            if order is None:
                return {}
            return order
        else:
            return {}
    except:
        return {}
    

def create_order(order):
    try:
        cur.execute('INSERT INTO orders (user_id, product_id, order_quantity, total_price) VALUES (%s, %s, %s, %s)', (order['user_id'], order['product_id'], order['order_quantity'], order['total_price']))
        db.conn.commit()
        new_order_id = cur.lastrowid
        return get_order(new_order_id)
    except:
        return {}


def update_order(id, order):
    try:
        print(order)
        cur.execute('UPDATE orders SET order_quantity = %s, total_price = %s WHERE id = %s', (order['order_quantity'], order['total_price'], id))
        db.conn.commit()
        return get_order(id)
    except:
        return {}

def delete_order(id):
    try:
        cur.execute('DELETE FROM orders WHERE id = %s', (id,))
        db.conn.commit()
        deleted_id = cur.lastrowid
        return deleted_id
    except:
        return 0
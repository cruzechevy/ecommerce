from app.db import db 

cur = db.conn.cursor()

def get_all_customer():
    try:
        cur.execute('SELECT * FROM users')
        customers = cur.fetchall()
        if customers is None:
            return []
        return customers
    except:
        return []

def get_customer(id):
    try:
        if id :
            cur.execute('SELECT * FROM users WHERE id = %s', (id,))
            customer = cur.fetchone()

            if customer is None:
                return {}
            return customer
        else:
            return {}
    except:
        return {}
    

def create_customer(customer):
    try:
        cur.execute('INSERT INTO users (name, email, mobile, address) VALUES (%s, %s, %s, %s)', (customer['name'], customer['email'], customer['mobile'], customer['address']))
        db.conn.commit()
        new_customer_id = cur.lastrowid
        return get_customer(new_customer_id)
    except:
        return {}


def update_customer(id, customer):
    try:
        print(customer)
        cur.execute('UPDATE users SET name = %s, email = %s,mobile = %s, address = %s WHERE id = %s', (customer['name'], customer['email'],customer['mobile'], customer['address'], id))
        db.conn.commit()
        return get_customer(id)
    except:
        return {}

def delete_customer(id):
    try:
        cur.execute('DELETE FROM users WHERE id = %s', (id,))
        db.conn.commit()
        deleted_id = cur.lastrowid
        return deleted_id
    except:
        return 0
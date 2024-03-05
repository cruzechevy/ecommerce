from db import db 

cur = db.conn.cursor();

def check_tables():
    """Checks for missing tables and creates them if necessary.

    Raises:
        Exception: If an error occurs during table creation.
    """

    try:
        # Fetch table names directly into a set for efficient membership checks
        cur.execute('SHOW TABLES')
        
        expected_keys = {'users', 'products', 'orders'}
        table_names = set(row[0] for row in cur.fetchall())

        # Find missing keys using set difference
        missing_keys = expected_keys - table_names

        if missing_keys:
            # Create missing tables based on key names
            for key in missing_keys:
                globals()[key]()  # Call functions dynamically based on key

    except Exception as e:
        print(f"An error occurred while creating tables: {e}")
       


def products():
    """Creates the products table if it doesn't exist."""

    cur.execute('CREATE TABLE IF NOT EXISTS products (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, description VARCHAR(255) NOT NULL, stock INT NOT NULL, price INT NOT NULL)')


def orders():
    """Creates the orders table if it doesn't exist."""
    
    cur.execute('CREATE TABLE IF NOT EXISTS orders (id INT AUTO_INCREMENT PRIMARY KEY, user_id INT NOT NULL, product_id INT NOT NULL, order_quantity INT NOT NULL, total_price INT NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id),FOREIGN KEY (product_id) REFERENCES products(id))')

def users():
    """Creates the users table if it doesn't exist."""

    cur.execute('CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL, email VARCHAR(255) NOT NULL UNIQUE, address TEXT, mobile VARCHAR(10) NOT NULL UNIQUE)')

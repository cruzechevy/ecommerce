# Code to demonstrate Synchronous REST Api for E-Commerce website
# Demonstrated for GET, GET ID, POST, PUT AND DELETE HTTP Methods
# URL to run -> http://localhost:8000/docs which opens the Swagger API documentation
# Run Uvicorn - uvicorn main:app --reload

# It contains the following modules
# -------------------------------------------------------------------------------------------------------------------------
# 1. User
# 2. Order
# 3. Product

# Importing Required Packages
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.user import users
from services.order import orders
from services.product import products
from db.check_tables import check_tables
from datetime import datetime

import os  # Import for environment variable access

# Load environment variables from a `.env` file (optional)
if os.path.exists(".env"):
    load_dotenv()


app = FastAPI()

# Checks Tables are there in the database or not. If not then create tables.
check_tables()

class User(BaseModel):
    name: str
    email: str
    address: str
    mobile: int
    
class Order(BaseModel):
    user_id: int
    product_id: int
    order_quantity: int

class Product(BaseModel):
    name: str
    description: str
    stock: int
    price: int

class OrderUpdate(BaseModel):
    order_quantity: int

# -------------------------------------------------------------------------------------------------------------------------
# API's related to the Default Module
# -------------------------------------------------------------------------------------------------------------------------
@app.get('/', status_code = 200)
async def get():
    """
    Welcome page.

    Raises:
        HTTPException: If there is an error running server.
    """
    try:
        return {'message': f"Welcome to the E-commerce website."}
    except:
       HTTPException(status_code=404, detail=f"Failed to launch server")

# Api to check the health of the server.
@app.get('/health-check', status_code = 200)
async def get():
    """
    Health Check for the server.

    Raises:
        HTTPException: If there is an error running server.
    """
    try:
        healthcheck = {
            'message': "Ok",
            'timestamp': datetime.now(),
        };
        return healthcheck
    except:
       HTTPException(status_code=404, detail=f"Failed to reteive health check")

# -------------------------------------------------------------------------------------------------------------------------
# API's related to the Order Module
# -------------------------------------------------------------------------------------------------------------------------

@app.get('/users', status_code = 200, tags=["User"])
async def get_all_users():
    """
    Retrieves a list of all users.

    Raises:
        HTTPException: If there is an error fetching users.
    """
    try:
        res = []
        data = users.get_all_customer()
        print(data)
        for i in range(len(data)):
            res.append({'id':data[i][0], 'name':data[i][1], 'email':data[i][2], 'address':data[i][3], 'mobile':data[i][4]})
        return res
    except:
       HTTPException(status_code=404, detail=f"Failed to fetch users")


@app.get('/users/{id}', status_code=200, tags=["User"])
async def get_user(id: int):
    """
    Retrieves a user by their ID.

    Args:
        id (int): The ID of the user to retrieve.

    Raises:
        HTTPException: If the user with the specified ID is not found.
    """
    try:
        data = users.get_customer(id)
        return {'id':data[0], 'name':data[1], 'email':data[2], 'address':data[3], 'mobile':data[4]}
    except:
        return HTTPException(status_code=404, detail=f"Failed to fetch user with id {id}")



@app.post('/users', status_code=201, tags=["User"])
async def new_user(user_obj: User):
    """
    Creates a new user.

    Args:
        user_obj (User): The user data to create.

    Raises:
        HTTPException: If there is an error creating the user.
    """
    try:
        new_user = {
            "name" : user_obj.name,
            "email" : user_obj.email,
            "address" : user_obj.address,
            "mobile" : user_obj.mobile
        }
        data = users.create_customer(new_user)

        return {'id':data[0], 'name':data[1], 'email':data[2], 'address':data[3], 'mobile':data[4]}
    except:
        return HTTPException(status_code = 404, detail=f"User creation failed")


@app.delete('/users/{id}',status_code=200, tags=["User"])
async def delete_user(id: int):
    """
    Deletes a user by their ID.

    Args:
        id (int): The ID of the user to delete.

    Raises:
        HTTPException: If the user with the specified ID is not found or cannot be deleted.
    """
    try:
        users.delete_customer(id);
        return {'message': f"Successfully Deleted User with id {id}"}
    except:
        raise HTTPException(status_code=404, detail=f"There is no User with id as {id}")


@app.put('/users/{id}', status_code = 200, tags=["User"])
async def update_user_details(id: int, user_obj: User):
    """
    Updates the details of a user.

    Args:
        id (int): The ID of the user to update.
        user_obj (User): The updated user data.

    Raises:
        HTTPException: If the user with the specified ID is not found or cannot be updated.
    """
    try:
        new_user = {
            "name" : user_obj.name,
            "email" : user_obj.email,
            "address" : user_obj.address,
            "mobile" : user_obj.mobile
        }
        data = users.update_customer(id, new_user)
        return {'id':data[0], 'name':data[1], 'email':data[2], 'address':data[3], 'mobile':data[4]}
    except:
        return HTTPException(status_code=404, detail=f"User with id {id} does not exist")

# ---------------------------------------------------------------------------------------------------------------------------   
# API's related to the Products Module
# ---------------------------------------------------------------------------------------------------------------------------
@app.get('/products', status_code=200, tags=["Products"])
async def get_all_products():
    """
    Retrieves a list of all products.

    Raises:
        HTTPException: If there is an error fetching products.
    """
    try:
        res = []
        data = products.get_all_product()
        print(data)
        for i in range(len(data)):
            res.append({'id':data[i][0], 'name':data[i][1], 'description':data[i][2], 'stock':data[i][3], 'price':data[i][4]})
        return res
    except:
        return HTTPException(status_code = 404, detail=f"Failed to fetch products")



@app.get('/products/{product_id}', status_code=200, tags=["Products"])
async def get_product(product_id: int):
    """
    Retrieves a product by its ID.

    Args:
        product_id (int): The ID of the product to retrieve.

    Raises:
        HTTPException: If the product with the specified ID is not found.
    """
    try:
        data = products.get_product(product_id)
        return {'id':data[0], 'name':data[1], 'description':data[2], 'stock':data[3], 'price':data[4]}
    except:
        return HTTPException(status_code=404, detail=f"Product doesn't exist with id {id}")



@app.post('/products', status_code=201, tags=["Products"])
async def new_product(product_obj: Product):
    """
    Creates a new product.

    Args:
        product_obj (Product): The product data to create.

    Raises:
        HTTPException: If there is an error creating the product.
    """
    try:
        new_product = {
            'description': product_obj.description,
            'stock': product_obj.stock,
            'name': product_obj.name,
            'price': product_obj.price,
        }
        data = products.create_product(new_product)
        return {'id':data[0], 'name':data[1], 'description':data[2], 'stock':data[3], 'price':data[4]}
    except:
        return HTTPException(status_code=404, detail=f"Product creation failed")


@app.delete('/products/{product_id}',status_code=200, tags=["Products"])
async def delete_product(product_id: int):
    """
    Deletes a product by its ID.

    Args:
        product_id (int): The ID of the product to delete.

    Raises:
        HTTPException: If the product with the specified ID is not found or cannot be deleted.
    """
    try:
        products.delete_product(product_id);
        return {'message': f"Successfully Deleted Product with id {product_id}"}
    except:
        raise HTTPException(status_code=404, detail=f"There is no Product with id as {id}")


@app.put('/products/{product_id}', status_code=200, tags=["Products"])
async def update_product_details(product_id: int, product_obj: Product):
    """
    Updates the details of a product.

    Args:
        product_id (int): The ID of the product to update.
        product_obj (Product): The updated product data.

    Raises:
        HTTPException: If the product with the specified ID is not found or cannot be updated.
    """
    try:
        update_product = {
            'id': product_id,
            'description': product_obj.description,
            'stock': product_obj.stock,
            'name': product_obj.name,
            'price': product_obj.price,
        }
        data = products.update_product(product_id, update_product)
        return {'id':data[0], 'name':data[1], 'description':data[2], 'stock':data[3], 'price':data[4]}
    except:
        return HTTPException(status_code=404, detail=f"Product with id {id} does not exist")

# ---------------------------------------------------------------------------------------------------------------------------   
# API's related to the Products Module
# ---------------------------------------------------------------------------------------------------------------------------
        
@app.get('/orders', status_code=200 ,tags=["Orders"])
async def get_all_orders():
    """
    Retrieves a list of all orders.

    Raises:
        HTTPException: If there is an error fetching orders.
    """
    try:
        res = []
        data = orders.get_all_order()
        for i in range(len(data)):
            product_details = products.get_product(data[i][2])
            res.append({'id':data[i][0], 'user_id':data[i][1], 'product_id':data[i][2],'product_name': product_details[1], 'order_quantity':data[i][3], 'total_price':data[i][4]})
        return res
    except:
        return HTTPException(status_code = 404, detail=f"Failed to fetch orders")


@app.get('/orders/{order_id}', status_code=200,tags=["Orders"])
async def get_order(order_id: int):
    """
    Retrieves an order by its ID.

    Args:
        order_id (int): The ID of the order to retrieve.

    Raises:
        HTTPException: If the order with the specified ID is not found.
    """
    try:
        data = orders.get_order(order_id)
        product_details = products.get_product(data[2])
        return {'id':data[0], 'user_id':data[1],'product_id':data[2], 'product_name': product_details[1], 'order_quantity':data[3], 'total_price':data[4]}
    except:
        return HTTPException(status_code=404, detail=f"Failed to fetch order with id {id}")



@app.post('/orders', status_code=201, tags=["Orders"])
async def new_order(order_obj: Order):
    """
    Creates a new order.

    Args:
        order_obj (Order): The order data to create.

    Raises:
        HTTPException: If there is an error creating the order
            or the product stock is insufficient.
    """
    print(order_obj)
    try:
        product_details = products.get_product(order_obj.product_id)
        if not product_details:
            raise HTTPException(status_code=404, detail=f"Product Doesn't Exist")
        product_price = product_details[4]
        new_order = {
            "user_id" : order_obj.user_id,
            "product_id" : order_obj.product_id,
            "total_price" : product_price * order_obj.order_quantity,
            "order_quantity" : order_obj.order_quantity
        }
        print(new_order)
        data = orders.create_order(new_order)
        return {'id':data[0], 'user_id':data[1],'product_id': data[2] ,'product_name': product_details[1], 'order_quantity':data[3], 'total_price':data[4]}
    except:
        return HTTPException(status_code=404, detail=f"Order creation failed")


@app.delete('/orders/{order_id}',status_code=200, tags=["Orders"])
async def delete_order(order_id: int):
    """
    Deletes an order by its ID.

    Args:
        order_id (int): The ID of the order to delete.

    Raises:
        HTTPException: If the order with the specified ID is not found or cannot be deleted.
    """
    try:
        orders.delete_order(order_id);
        return {'message': f"Successfully Deleted Order with id {order_id}"}
    except:
        raise HTTPException(status_code=404, detail=f"There is no Order with id as {order_id}")



@app.put('/orders/{order_id}', status_code=200, tags=["Orders"])
async def update_order_details(order_id: int, order_obj: OrderUpdate):
    """
    Updates the order quantity of an order.

    Args:
        order_id (int): The ID of the order to update.
        order_obj (OrderUpdate): The updated order quantity.

    Raises:
        HTTPException: If the order with the specified ID is not found
            or the product stock is insufficient for update.
    """
    try:
        order_data = orders.get_order(order_id)
        product_details = products.get_product(order_data[2])
        product_price = product_details[4]
        new_order = {
            "total_price" : product_price * order_obj.order_quantity,
            "order_quantity" : order_obj.order_quantity
        }
        data = orders.update_order(order_id, new_order)
        return {'id':data[0], 'user_id':data[1],'product_id': data[2], 'product_name': product_details[1], 'order_quantity':data[3], 'total_price':data[4]}
    except:
        return HTTPException(status_code=404, detail=f"Order with id {order_id} does not exist")
    
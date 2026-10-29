
import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Product request model
class Product(BaseModel):
    id: int
    name: str
    price: float
    category: str


# Database connection
def get_db_connection():
    conn = sqlite3.connect("urskartz.db")
    conn.row_factory = sqlite3.Row
    return conn


# Create database table
def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            category TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


create_table()


@app.get("/")
def home():
    return {"message": "Welcome to Urskartz AI Agent"}


# Save a product to the database
@app.post("/products")
def create_product(product: Product):
    conn = get_db_connection()

    try:
        conn.execute(
            """
            INSERT INTO products (id, name, price, category)
            VALUES (?, ?, ?, ?)
            """,
            (product.id, product.name, product.price, product.category)
        )
        conn.commit()

        return {
            "message": "Product saved successfully",
            "product": product
        }

    except sqlite3.IntegrityError:
        return {"message": "Product ID already exists"}

    finally:
        conn.close()


# Retrieve a product from the database
@app.get("/products/{product_id}")
def get_product(product_id: int):
    conn = get_db_connection()

    try:
        product = conn.execute(
            "SELECT * FROM products WHERE id = ?",
            (product_id,)
        ).fetchone()

        if product is None:
            return {"message": "Product not found"}

        return dict(product)

    finally:
        conn.close()


# Retrieve all products from the database
@app.get("/products")
def get_products():
    conn = get_db_connection()

    try:
        products = conn.execute(
            "SELECT * FROM products"
        ).fetchall()

        return [dict(product) for product in products]

    finally:
        conn.close()

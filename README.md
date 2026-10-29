Day 1 — Learning summary
1. Python and FastAPI setup
- Installed Python and the FastAPI library.
- Created a local virtual environment (.venv).
- Activated the environment and installed dependencies using pip.



2. Created REST API endpoints
- GET / — welcome message.
- GET /products — retrieve all products.
- GET /products/{product_id} — retrieve a product by ID.
- POST /products — create and save a product.



3. Pydantic — BaseModel

Used Product(BaseModel) to define and validate incoming JSON product data, including ID, name, price, and category.



4. SQLite database
- Created urskartz.db.
- Created the products table.
- Inserted products using SQL.
- Retrieved products from the database.

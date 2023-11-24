# E-Commerce API

## Getting Started

### Prerequisites
- Python
- Docker

### Installation
1. Run the application
   ```bash
   docker-compose up --build
   
### Stacks
1. Flask Framework
2. Postgre SQL

## API List

- [Products API](#products-api)
  - [Get All Products](#get-all-products)
  - [Get Product by ID](#get-product-by-id)
  - [Create Product](#create-product)
  - [Update Product](#update-product)

- [Shopping Cart API](#shopping-cart-api)
  - [Add to Cart](#add-to-cart)
  - [Get Cart](#get-cart)
  - [Checkout](#checkout)

- [Authentication API](#authentication-api)
  - [User Registration](#user-registration)
  - [User Login](#user-login)

## Products API

### Get All Products

**Endpoint:** `GET /products/all`

Retrieve a list of all products.

### Get Product by ID

**Endpoint:** `GET /products/{product_id}`

Retrieve information about a specific product.

### Create Product

**Endpoint:** `POST /products`

Create a new product.

**Request:**
```json
{
  "name": "Product Name",
  "price": 29.99,
  "description": "Product description",
  "stock_quantity": 100
}
```
### Update Product

**Endpoint:** `PUT /update/{product_id}`

Update existing product.

**Request:**
```json
{
  "name": "Product Name",
  "price": 29.99,
  "description": "Product description",
  "stock_quantity": 100
}
```

## Shopping Cart API

### Add to Cart

**Endpoint:** `POST /cart/add/{product_id}`

Add a product to the user's shopping cart.

**Request:**
```json
{
  "quantity": 2
}
```

### Get Cart

**Endpoint:** `GET /cart/get`

**Response**
```json
{
  "cart": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 3,
      "quantity": 1
    }
  ]
}

```

### Checkout

**Endpoint:** `POST /cart/checkout`

**Response**
```json
{
  "message": "Checkout successful"
}
```

## Authentication API

### User Registration

**Endpoint:** `POST /register`

**Request:**
```json
{
  "username": "username",
  "email": "my@email.com",
  "password": "my_password"
}
```

### User Login

**Endpoint:** `POST /login`

**Request:**
```json
{
  "username": "username",
  "password": "my_password"
}
```

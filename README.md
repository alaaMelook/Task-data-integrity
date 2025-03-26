# Task-data-integrity
 Implement Flask API with Login, 2FA, and JWT Authentication

🎯 Project Overview

This is a secure Flask-based API that implements user authentication with Two-Factor Authentication (2FA) using Google Authenticator, and JWT-based authorization for performing CRUD operations on a Products database.

⚡ Features

   - User Registration: Users can sign up with a username and password.
   - 2FA with Google Authenticator: Secure login requires a one-time password (OTP).
   - JWT Authentication: Upon successful login, users receive a JWT token valid for 10 minutes.
   - Protected CRUD Operations: Products database supports Create, Read, Update, and Delete with JWT authentication.


🏛 Database Structure

   Users Table:

   - Column	Type	Description
   - id	INT (PK)	Unique user ID
   - username	VARCHAR(50)	Unique username
   - password	VARCHAR(256)	Hashed password
   - twofa_secret	VARCHAR(256)	Google Authenticator secret

   Products Table:

   - Column	Type	Description
   - id	INT (PK)	Auto-increment product ID
   - name	VARCHAR(100)	Product name
   - description	VARCHAR(255)	Product description
   - price	DECIMAL(10,2)	Product price
   - quantity	INT	Stock quantity


🚀 How to Run

   Clone the repo:

    git clone https://github.com/YourUsername/YourRepo.git

    cd YourRepo

    Set up a virtual environment and install dependencies:

    python -m venv venv

    source venv/bin/activate   # On Windows use: venv\Scripts\activate
    
  
Set up MySQL database (update .env with credentials).


Run the Flask application:
 
    python app.py

Use Postman to test endpoints. First, register a user, log in, verify OTP, and use the JWT token for secured CRUD requests.


📌 Endpoints
Method	Endpoint	Description 

 - POST	/auth/register	Register a new user  

 - POST	/auth/login	Login and get OTP 

 - POST	/auth/verify	Verify OTP and get JWT token 

 - POST	/api/products	Create a product (JWT required) 

 - GET	/api/products	Get all products (JWT required)   

 - PUT	/api/products/{id}	Update a product (JWT required)   

 - DELETE	/api/products/{id}	Delete a product (JWT required)   


🛠 Technologies Used

  - Flask (Python)

  - MySQL (Database)

  - JWT Authentication

  - Google Authenticator (2FA)

  - Postman for Testing

📜 License

This project is open-source and available under the MIT License.


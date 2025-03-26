from flask import Flask
from flask_jwt_extended import JWTManager
from auth import auth
from product import product

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'
jwt = JWTManager(app)

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(product, url_prefix="/api")

if __name__ == '__main__':
    app.run(debug=True)

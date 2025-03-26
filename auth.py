from flask import Blueprint, request, jsonify
from db import get_db_connection
import hashlib
import pyotp
import qrcode
import base64
from io import BytesIO

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()
    twofa_secret = pyotp.random_base32()

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password, twofa_secret) VALUES (%s, %s, %s)", 
                   (username, password, twofa_secret))
    conn.commit()
    cursor.close()
    conn.close()

    otp_url = pyotp.totp.TOTP(twofa_secret).provisioning_uri(username, issuer_name="FlaskAPI")
    qr = qrcode.make(otp_url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_base64 = base64.b64encode(buffer.getvalue()).decode()

    return jsonify({"message": "User registered", "qr_code": qr_base64})


from flask_jwt_extended import JWTManager, create_access_token
from flask import Flask
import datetime

jwt = JWTManager()

@auth.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = hashlib.sha256(data.get('password').encode()).hexdigest()
    otp_code = data.get('otp')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user and pyotp.TOTP(user['twofa_secret']).verify(otp_code):
        access_token = create_access_token(identity=username, expires_delta=datetime.timedelta(minutes=10))
        return jsonify({"access_token": access_token})
    
    return jsonify({"error": "Invalid credentials"}), 401

import csv
from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__,static_url_path='/static')

# Endpoint for serving the main page
@app.route('/')
def serve_main_page():
    return render_template('mainpage.html')

# Endpoint for serving the login page for company employees
@app.route('/login')
def serve_login_page():
    return render_template('templates/login.html')

# Endpoint for serving the registration page for regular users
@app.route('/register')
def serve_registration_page():
    return render_template('templates/registration.html')

# Endpoint for capturing image after user registration
@app.route('/capture', methods=['POST'])
def capture_image():
    try:
        # Assuming image is captured and processed here
        # For simplicity, just displaying a success message
        return jsonify({'message': 'Registered successfully'})
    except Exception as e:
        return jsonify({'error': 'An error occurred during image capture'}), 500

if __name__ == '__main__':
    app.run(debug=True)
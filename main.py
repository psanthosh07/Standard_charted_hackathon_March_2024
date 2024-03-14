import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_url_path='/static')

# Initialize Firebase Admin SDK
cred = credentials.Certificate(r"C:\Users\Santhosh\Desktop\Standard_charted_hackathon_March_2024\Standard_charted_hackathon_March_2024\serviceaccountkey.json")  # Replace with your service account key path
firebase_admin.initialize_app(cred)
db = firestore.client()

# Endpoint for serving video KYC HTML file
@app.route('/')
def serve_html():
    return render_template('video_kyc.html')

# Endpoint for user registration
@app.route('/register', methods=['POST', 'GET'])
def register_user():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            name = data.get('name')
            dob = data.get('dob')
            email = data.get('email')
            address = data.get('address')
            pan_aadhaar = data.get('panAadhaar')
            signature = data.get('signature')
            income_range = data.get('incomeRange')
            employment_type = data.get('employmentType')
            imageData = data.get('imageData')
            
            if not all([name, dob, email, address, pan_aadhaar, signature, income_range, employment_type, imageData]):
                return jsonify({'error': 'Missing required fields'}), 400
            
            # Add user data to Firestore
            users_ref = db.collection('users')
            users_ref.add({
                'name': name,
                'dob': dob,
                'email': email,
                'address': address,
                'pan_aadhaar': pan_aadhaar,
                'signature': signature,
                'income_range': income_range,
                'employment_type': employment_type,
                'imageData': imageData
            })
            
            print("User registered successfully:", data)  # Debugging print statement
            return jsonify({'message': 'User registered successfully'})
        except Exception as e:
            print("Error registering user:", str(e))  # Debugging print statement
            return jsonify({'error': 'An error occurred while registering the user'}), 500
    else:
        return "Method Not Allowed", 405

# Endpoint for video KYC session
@app.route('/video-kyc', methods=['POST'])
def start_video_kyc():
    # Sample logic for video KYC
    # You can integrate video conferencing APIs here
    # and perform KYC process
    
    return jsonify({'message': 'Video KYC completed successfully'})

if __name__ == '__main__':
    app.run(debug=True)

import csv
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

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
            imageData = data.get('imageData')
            
            if not name or not dob or not email or not imageData:
                return jsonify({'error': 'Missing required fields'}), 400
            
            # Write data to CSV file
            with open('user_data.csv', mode='a', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['name', 'dob', 'email', 'imageData'])
                if file.tell() == 0:
                    writer.writeheader()  # Write header if file is empty
                writer.writerow(data)
            
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

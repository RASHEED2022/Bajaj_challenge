from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to process input data
def process_data(data):
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]
    lowercase_alphabets = [item for item in alphabets if item.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None
    return numbers, alphabets, highest_lowercase

# POST endpoint
@app.route('/bfhl', methods=['POST'])
def post_data():
    try:
        data = request.json.get('data', [])
        numbers, alphabets, highest_lowercase = process_data(data)
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",  # Replace with dynamic user_id logic
            "email": "john@xyz.com",  # Replace with your email logic
            "roll_number": "ABCD123",  # Replace with your roll number logic
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)})

# GET endpoint
@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)

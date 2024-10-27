from flask import Flask, jsonify

app = Flask(__name__)

# Route for addition
@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def add(num1, num2):
    result = num1 + num2  # Perform addition
    return jsonify(result=result)  # Return result in JSON format

# Route for subtraction
@app.route('/sub/<int:num1>/<int:num2>', methods=['GET'])
def subtract(num1, num2):
    result = num1 - num2  # Perform subtraction
    return jsonify(result=result)  # Return result in JSON format

# Route for multiplication
@app.route('/mul/<int:num1>/<int:num2>', methods=['GET'])
def multiply(num1, num2):
    result = num1 * num2  # Perform multiplication
    return jsonify(result=result)  # Return result in JSON format

# Modified Route for division
@app.route('/div/<int:num1>/<int:num2>', methods=['GET'])
def divide(num1, num2):
    try:
        result = num1 / num2  # Perform division (this will raise an error if num2 is zero)
        return jsonify(result=result)  # Return result in JSON format
    except ZeroDivisionError:  # Catch division by zero
        return jsonify(error="Division by zero is not allowed."), 400
    except Exception as e:  # Catch any other exceptions
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode


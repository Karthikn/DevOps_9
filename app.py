from flask import Flask, request, jsonify

#createing s server

app = Flask(__name__)

students = [{"name": "Rahul", "feedback": 4}, 

            {"name": "Rohit", "feedback": 3}, 

            {"name": "Rohan", "feedback": 2}]

@app.route('/')

def hello_world():

    return 'Hello, World!'

@app.route('/student/<name>')

def get_students():

    return request.param.name

 

if __name__ == '__main__':

    app.run(debug=True)
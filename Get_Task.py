from flask import Flask, jsonify, abort

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]

# Get a specific task 
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:                             #ForLoop
        if task['id'] == task_id:
            return jsonify({'task': task})
    abort(404, description="Task not found")

if __name__ == '__main__': #Code snippet
    app.run(debug=True) 


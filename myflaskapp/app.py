import os
from flask import Flask, render_template

app = Flask(__name__)

# Mock data
pets = [
    {'name': 'Max', 'image_url': 'assets/dog.jpg', 'fun_fact': 'Loves to play fetch'},
    {'name': 'Lisa', 'image_url': 'assets/cat.jpg', 'fun_fact': 'Has a penchant for climbing trees'}
]

# print(os.path.abspath("templates"))
# print(os.path.abspath("assets"))

@app.route('/')
def index():
    return render_template('index.html', pets=pets)

@app.route('/pets/<int:index>')
def pet_show(index):
    if index >= len(pets) or index < 0:
        return "Pet not found", 404
    return render_template('pet_show.html', pet=pets[index])

@app.route('/facts/new', methods=['GET'])
def new_fact():
    try:
        return render_template('new_fact.html')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)

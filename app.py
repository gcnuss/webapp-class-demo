from flask import Flask, render_template, request, jsonify
from model import DataModel

app = Flask(__name__)
data_model = DataModel()

@app.route('/')
def index():
    return render_template('baby_size_css.html')

@app.route('/solve', methods=['POST'])
def solve():
    user_data = request.json
    week = int(user_data['week'])
    measure_food_dict = data_model.get_food(week)
    measure,food = measure_food_dict['measure'], measure_food_dict['food']
    return jsonify({'measure': measure, 'food': food})

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=1)

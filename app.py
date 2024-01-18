from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
received_posts = []
mon_list = []
tue_list = []
wed_list = []
thu_list = []
fri_list = []

def calculate_average(posts):
    addition = 0
    for post in posts:
        addition += int(post)
    if not len(posts) == 0:
        average = addition / len(posts)
    else:
        average = 0
    return average

@app.route('/receive_post', methods=['POST'])
def receive_post():
    weekday = datetime.now().weekday()

    if weekday == 0:
        weekend = False
        list = mon_list
    elif weekday == 1:
        weekend = False
        list = tue_list
    elif weekday == 2:
        weekend = False
        list = wed_list
    elif weekday == 3:
        weekend = False
        list = thu_list
    elif weekday == 4:
        weekend = False
        list = fri_list
    else:
        weekend = True

    data = request.json  # Assumes JSON payload
    response = "Rating not recieved!"
    if not int(data) > 5 and not int(data) < 1 and not weekend:
        list.append(data)
        response = f"Rating received successfully! Using list {list}."
    else:
        if weekend:
            response = "It's a weekend!"
        else:
            response = "Rating too high or low!"
    
    return response

@app.route('/show_posts', methods=['GET'])
def show_posts():
    mon = calculate_average(mon_list)
    tue = calculate_average(tue_list)
    wed = calculate_average(wed_list)
    thu = calculate_average(thu_list)
    fri = calculate_average(fri_list)

    return jsonify({'Monday':round(mon, 2), 'Tuesday':round(tue, 2), 'Wednesday':round(wed, 2), 'Thursday':round(thu, 2), 'Friday':round(fri, 2)})

if __name__ == '__main__':
    app.run(debug=True)

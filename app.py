from flask import Flask, request, jsonify

app = Flask(__name__)
received_posts = []

def calculate_average():
    addition = 0
    for post in received_posts:
        addition += int(post)
    if not len(received_posts) == 0:
        average = addition / len(received_posts)
    else:
        average = 0
    return average

@app.route('/receive_post', methods=['POST'])
def receive_post():
    data = request.json  # Assumes JSON payload
    response = "Rating not recieved!"
    if not int(data) > 5 and not int(data) < 1:
        received_posts.append(data)
        response = "Rating received successfully!"
    else:
        response = "Rating too high or low!"
    
    return response

@app.route('/show_posts', methods=['GET'])
def show_posts():
    send = calculate_average()
    return jsonify({'Rating':round(send, 2)})

if __name__ == '__main__':
    app.run(debug=True)

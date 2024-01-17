import requests
import json

while True:
    try:
        rating = int(input("Rating(1-5): "))
    except:
        print("Error.")
        input()
        exit()

    url = 'http://127.0.0.1:5000/receive_post'  # Update with the correct URL

    data_to_send = rating

    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(data_to_send), headers=headers)

    print("Response:", response.text)
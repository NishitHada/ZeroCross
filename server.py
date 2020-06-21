#!flask/bin/python
import json
from flask import Flask, jsonify, abort, request, make_response, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


used_rooms = {0, 1, 2, 4, 5, 6, 3, 10, 9}


@app.route('/create_room/', methods=['GET'])
def create_room():
    # return "ROOM CREATION REQUEST"
    for i in range(0, 11):
        if i not in used_rooms:
            used_rooms.add(i)
            print("Updated used list:")
            print(used_rooms)
            return jsonify({'room_id:': i})
    return make_response(jsonify({'Error': 'No room available'}), 400)


@app.route('/available_rooms/', methods=['GET'])
def available_rooms():
    # return "PRINT LIST OF AVAILABLE ROOMS"
    available = []
    for i in range(0, 11):
        if i not in used_rooms:
            available.append(i)
    print(available)
    return jsonify({'Available Room List:': json.dumps(available)})


@app.route('/used_rooms_list/', methods=['GET'])
def used_rooms_list():
    return make_response(jsonify({'Used Room List': json.dumps(list(used_rooms))}), 400)


# @app.route('/<int:room_id>/update', methods=['PUT'])
# def update():

if __name__ == '__main__':
    app.run(debug=True)

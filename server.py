#!flask/bin/python
import json
from flask import Flask, jsonify, abort, request, make_response, url_for
# import uuid
from board import Board

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


used_rooms = {0, 1, 2, 4, 5, 6, 3, 10, 9}
# mappings = {0:'6035844c-8aea-49c3-9e1e-67615c1c12b8', 1:'dfbef37d-23f3-440d-8fdb-ed92c4df35a7',
#             2:'215731a2-b563-4420-b33b-72fb14648a02', 3:'a3b8ce2c-fa83-4d81-aaf5-d87d8be35c40',
#             4:'bce4b5f5-9d7d-44ae-978e-75160b4b06c4', 5:'c5c89177-cb67-4bea-876d-3f02f552db4a',
#             6:'f8295844-0040-45a2-a1d8-57aafaea1064', 9:'c0a42ec7-caf9-494c-a1e6-dc444096170f',
#             10:'a6236f25-e274-4eed-b0c3-ae5b2f9b0fda'}
mappings = {0: 'zero'}
for i in used_rooms:
    mappings[i] = Board()


@app.route('/create_room/', methods=['GET'])
def create_room():
    # return "ROOM CREATION REQUEST"
    for i in range(0, 11):
        if i not in used_rooms:
            used_rooms.add(i)
            print("Updated used list:", used_rooms)
            # mappings[i] = str(uuid.uuid4())
            mappings[i] = Board()
            mappings[i].print_board()
            print(mappings)
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


@app.route('/<int:room_id>/update', methods=['PUT'])
def update(room_id):
    print(room_id)
    print(request.json)
    # return jsonify(request.json)

    if room_id not in used_rooms:
        return make_response(jsonify({'Error': 'Room not found'}), 404)
    row = request.json['Row']
    col = request.json['Col']
    sign = request.json['Sign']
    mappings[room_id].update(row, col, sign)
    print("Updated Board at room id", room_id, " -> ", mappings[room_id].get_board())
    return jsonify(request.json)
    # return jsonify({mappings[i].get_board()})


if __name__ == '__main__':
    app.run(debug=True)

import time

import eventlet
eventlet.monkey_patch()

from flask import Flask, jsonify
from flask_socketio import SocketIO

from flask_cors import CORS, cross_origin
from routes import basic_routes, sudoku_routes

from utils import sudoku_socketio
from sudoku_solver import utils


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(app, cors_allowed_origins="*", max_http_buffer_size=10000000)

# Registrar los Blueprints
# app.register_blueprint(basic_routes.basic_routes)
# app.register_blueprint(sudoku_routes.sudoku_routes)


@app.route('/')
def index():
    return "Flask-SocketIO Server Running"


@socketio.on('connect')
@cross_origin()
def handle_connect():
    print("Client connected")
    socketio.emit("connected", {"data": "Connected!"})
    return jsonify({"data": "Connected!"})

@app.route("/get_sudoku", methods=["GET"])
def get_sudoku():
    path = "csv/sudoku_sencillo.csv"

    sudoku_df = utils.read_table_from_csv(path=path)

    return jsonify(sudoku_df.to_json(orient="values"))

@app.route("/solve", methods=["POST", "GET"])
def solve_sudoku():

    board = "./csv/sudoku_sencillo.csv"

    sudoku_obj = sudoku_socketio.SudokuSocketIO(table=board)
    socketio.start_background_task(target=sudoku_obj.brute_force_socketio, socketio=socketio)

    return '', 204



if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5001)
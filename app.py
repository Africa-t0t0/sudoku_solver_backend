import time
import eventlet
eventlet.monkey_patch()

from flask import Flask, jsonify
from flask_socketio import SocketIO
from flask_cors import CORS, cross_origin

from utils.extensions import socketio
from routes import basic_routes, sudoku_routes
from sudoku_solver import utils


app = Flask(__name__)

CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
socketio.init_app(app=app)


# Registrar los Blueprints
app.register_blueprint(basic_routes.basic_routes)
app.register_blueprint(sudoku_routes.sudoku_routes)


@app.route("/")
def index():
    return "Flask-SocketIO Server Running"


@socketio.on("connect")
@cross_origin()
def handle_connect():
    print("Client connected")
    socketio.emit("connected", {"data": "Connected!"})
    return jsonify({"data": "Connected!"})


if __name__ == "__main__":
    socketio.run(app, debug=True, host='0.0.0.0', port=5001)
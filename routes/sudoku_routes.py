from flask import Blueprint, jsonify

from utils.extensions import socketio
from utils import sudoku_socketio

from sudoku_solver import sudoku, utils


sudoku_routes = Blueprint("sudoku_routes", __name__)

@sudoku_routes.route("/get_sudoku", methods=["GET"])
def get_sudoku():
    path = "csv/sudoku_sencillo.csv"

    sudoku_df = utils.read_table_from_csv(path=path)

    return jsonify(sudoku_df.to_json(orient="values"))

@sudoku_routes.route("/solve", methods=["POST", "GET"])
def solve_sudoku():
    board = "./csv/sudoku_sencillo.csv"

    sudoku_obj = sudoku_socketio.SudokuSocketIO(table=board)
    socketio.start_background_task(target=sudoku_obj.brute_force_socketio, socketio=socketio)

    return '', 204



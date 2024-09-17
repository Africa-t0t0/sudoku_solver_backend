from flask import Blueprint, jsonify

from sudoku_solver import sudoku

basic_routes = Blueprint("basic_routes", __name__)

@basic_routes.route("/")
def index():
    return "<h1>Sudoku Solver</h1>"

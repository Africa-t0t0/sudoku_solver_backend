from flask import Blueprint, jsonify

from sudoku_solver import sudoku, utils

sudoku_routes = Blueprint("sudoku_routes", __name__)





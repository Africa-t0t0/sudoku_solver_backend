from flask import Blueprint, jsonify

from sudoku_solver import sudoku

sudoku_routes = Blueprint("sudoku_routes", __name__)


@sudoku_routes.route("/solve", methods=["POST"])
def solve_sudoku():
    # Aquí instancias y utilizas tu clase Sudoku
    # Ejemplo:
    board = "./sudoku_solver/csv/sudoku_sencillo.csv"

    sudoku_solver = sudoku.Sudoku(board)
    solved = sudoku_solver.brute_force()
    return jsonify(solved_board=solved)
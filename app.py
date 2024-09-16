from flask import Flask, jsonify

from sudoku_solver import sudoku

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Sudoku Solver</h1>"


@app.route("/solve", methods=["POST"])
def solve_sudoku():
    # Aquí instancias y utilizas tu clase Sudoku
    # Ejemplo:
    board = "./sudoku_solver/csv/sudoku_sencillo.csv"

    sudoku_solver = sudoku.Sudoku(board)
    solved = sudoku_solver.brute_force()
    return jsonify(solved_board=solved)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)

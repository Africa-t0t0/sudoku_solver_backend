import time

from flask_socketio import SocketIO

from sudoku_solver import sudoku


class SudokuSocketIO(sudoku.Sudoku):
    """
        We create the class in this repo because we avoid installing socketio dependencies
        on the other repo.
    """
    _socketIO = None

    def _basic_solution_socketio(self) -> bool:
        empty_cell = self._find_empty_cells_brute()
        if not empty_cell:
            return True
        position_x, position_y = empty_cell
        for num in range(1, 10):
            if self._brute_force_valid(position_x=position_x, position_y=position_y, num=num):
                self._table_df.iloc[position_x, position_y] = num
                if self._basic_solution_socketio():
                    return True
                self._table_df.iloc[position_x, position_y] = 0
                self._socketIO.emit("update", {"data" :self._table_df.to_json(orient="values")}, broadcast=True)
                time.sleep(0.001)
                print("emiting!")
                self.print_table_realtime()

        return False

    def brute_force_socketio(self, socketio: SocketIO) -> bool:
        print("background!")

        self._socketIO = socketio
        solution = self._basic_solution_socketio()
        self._socketIO.emit("completed", {"data": self._table_df.to_json(orient="values")})
        return solution

import math

class Matrix:
    def __init__(self, list_of_cells: list[list[int]]):
        total_rows = len(list_of_cells) 
        if total_rows <= 0:
            raise Exception("Invalid list of cells: there are no rows.")

        total_cols = len(list_of_cells[0])
        if total_cols <= 0:
            raise Exception("Invalid list of cells: Matrix can't have empty rows.")

        index = 0
        for row in list_of_cells:
            index += 1
            if len(row) != total_cols:
                raise Exception(f"Line {index} has a different number of elements regarding the first row: {total_cols}")

        self.rows = total_rows
        self.cols = total_cols
        self.internal_matrix = list_of_cells


    def element_at(self, row: int, col: int):
        if row <= 0:
            raise Exception(f"Invalid row: row should be a positive integer.")

        if col <= 0:
            raise Exception(f"Invalid column: column should be a positive integer.")

        if row > self.rows:
            raise Exception(f"Invalid row: Matrix has a total of {self.rows} rows.")

        if col > self.cols:
            raise Exception(f"Invalid column: Matrix has a total of {self.cols} columns.")

        return self.internal_matrix[row][col]


    def _common_distance_parameters_validation(self, row1: int, col1: int, row2: int, col2: int):
        if row1 <= 0:
            raise Exception(f"Invalid row1: row1 should be a positive integer.")

        if col1 <= 0:
            raise Exception(f"Invalid col1: col1 should be a positive integer.")

        if row2 <= 0:
            raise Exception(f"Invalid row2: row2 should be a positive integer.")

        if col2 <= 0:
            raise Exception(f"Invalid col2: col2 should be a positive integer.")


    def manhattan_distance(self, row1: int, col1: int, row2: int, col2: int):
        self._common_distance_parameters_validation(row1, col1, row2, col2)
        return abs(row1 - row2) + abs(col1 - col2)


    def diagonal_distance(self, row1: int, col1: int, row2: int, col2: int):
        self._common_distance_parameters_validation(row1, col1, row2, col2)
        distance_x = abs(row1 - row2)
        distance_y = abs(col1 - col2)

        return (distance_x + distance_y) + ((math.sqrt(2) - 2) * min(distance_x, distance_y))


    def euclidean_distance(self, row1: int, col1: int, row2: int, col2: int):
        self._common_distance_parameters_validation(row1, col1, row2, col2)
        side_1 = 2 * abs(row1 - row2)
        side_2 = 2 * abs(col1 - col2)
        return math.sqrt(side_1 + side_2)


    def __repr__(self):
        repr = f"<Matrix rows={self.rows} cols={self.cols}>\n"
        repr += "+" + ("---" * self.cols) + "+\n"
        for row in self.internal_matrix:
            repr += "|"
            for element in row:
                repr += f" {element} "
            repr += "|\n"
        repr += "+" + ("---" * self.cols) + "+\n"
        return repr

import unittest

import test_data

import solver


class TestTypes(unittest.TestCase):

    def test_output_type(self):
        solution = solver.solve(test_data.solved)
        self.assertEqual(len(solution), 9)
        self.assertIsInstance(solution, list)
        for row in solution:
            self.assertEqual(len(row), 9)
            self.assertIsInstance(row, list)
            for cell in row:
                self.assertIsInstance(cell, int)


class TestUniqueness(unittest.TestCase):

    def test_uniqueness_in_rows(self):
        solution = solver.solve(test_data.solved)
        for row in solution:
            self.assertEqual(len(set(row)), len(row))

    def test_uniqueness_in_columns(self):
        solution = solver.solve(test_data.solved)
        for column_index in range(9):
            column = [ solution[row_index][column_index] for row_index in range(9)]
            self.assertEqual(len(set(column)), len(column))

    def test_uniqueness_in_boxes(self):
        solution = solver.solve(test_data.solved)
        for box_index in range(9):
            bi = (box_index // 3) * 3
            bj = (box_index % 3) * 3
            box = []
            for i in range(3):
                for j in range(3):
                    box.append(solution[bi + i][bj + j])
            self.assertEqual(len(set(box)), len(box))


class TestNumericRange(unittest.TestCase):

    def test_numeric_range(self):
        solution = solver.solve(test_data.solved)
        for i in range(9):
            for j in range(9):
                self.assertGreaterEqual(solution[i][j], 1)
                self.assertLessEqual(solution[i][j], 9)


if __name__ == '__main__':
    unittest.main()

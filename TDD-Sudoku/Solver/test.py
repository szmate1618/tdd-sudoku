import unittest

import test_data

import solver


class TestTypes(unittest.TestCase):

    def test_solve_output_type(self):
        solution = solver.solve(test_data.solved)

        self.assertEquals(len(solution), 9)
        self.assertIsInstance(solution, list)

        for line in solution:
            self.assertEquals(len(line), 9)
            self.assertIsInstance(line, list)

            for cell in line:
                self.assertIsInstance(cell, int)


class TestUniqueness(unittest.TestCase):

    def test_uniqueness_in_lines(self):
        solution = solver.solve(test_data.solved)
        for line in solution:
            self.assertEqual(len(set(line)), len(line))

if __name__ == '__main__':
    unittest.main()

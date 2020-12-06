import unittest

import test_data

import solver

class Test_test(unittest.TestCase):
    def test_solve_output_type(self):
        solution = solver.solve(test_data.solved)
        self.assertEquals(len(solution), 9)
        self.assertIsInstance(solution, list)

if __name__ == '__main__':
    unittest.main()
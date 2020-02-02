# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

from sparse_matrix_olga_udacity import SparseMatrix

class TestSparseMatrixClass(unittest.TestCase):  
    
    def test_initialization(self): 
        self.sparse_matrix = SparseMatrix([1, 2, 3, 4], [(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2 )
   
        self.assertEqual(self.sparse_matrix.element_list, [1, 2, 3, 4], 
                         'wrong elements were assigned to sparse matrix object')
        self.assertEqual(self.sparse_matrix.coordinate_list, [(0, 0), (0, 1), (1, 0), (1, 1)], 
                         'incorrect coordinates for non-zero elements')
        self.assertEqual(self.sparse_matrix.size_rows, 2, 
                         'incorrect size (rows)')
        self.assertEqual(self.sparse_matrix.size_cols, 2, 
                         'incorrect size (cols)')

        
        self.sparse_matrix = SparseMatrix([2, 3, 4, 5], [(0, 0), (0, 1), (1, 0), (1, 1)], 3, 5 )
        self.assertEqual(self.sparse_matrix.element_list, [2, 3, 4, 5], 
                         'wrong elements were assigned to sparse matrix object')
        self.assertEqual(self.sparse_matrix.coordinate_list, [(0, 0), (0, 1), (1, 0), (1, 1)], 
                         'incorrect coordinates for non-zero elements')
        self.assertEqual(self.sparse_matrix.size_rows, 3, 
                         'incorrect size (rows)')
        self.assertEqual(self.sparse_matrix.size_cols, 5, 
                         'incorrect size (cols)')


        self.sparse_matrix = SparseMatrix([1, 2, 1], [(0, 2), (1, 1), (1, 2)], 3, 5 )
        self.assertEqual(self.sparse_matrix.element_list, [1, 2, 1], 
                         'wrong elements were assigned to sparse matrix object')
        self.assertEqual(self.sparse_matrix.coordinate_list, [(0, 2), (1, 1), (1, 2)], 
                         'incorrect coordinates for non-zero elements')
        self.assertEqual(self.sparse_matrix.size_rows, 3, 
                         'incorrect size (rows)')
        self.assertEqual(self.sparse_matrix.size_cols, 5, 
                         'incorrect size (cols)')
        
        
    def test_add(self):
        sparse_matrix_one = SparseMatrix([1, 2, 3, 4], [(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2 )
        sparse_matrix_two = SparseMatrix([2, 3, 4, 5], [(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2 )
        sparse_matrix_sum = sparse_matrix_one + sparse_matrix_two
        
        self.assertEqual(sparse_matrix_sum.element_list, [3, 5, 7, 9])
        self.assertEqual(sparse_matrix_sum.coordinate_list, [(0, 0), (0, 1), (1, 0), (1, 1)])
    
        sparse_matrix_three = SparseMatrix([1, 2, 3], [(0, 0), (1, 1), (1, 2)], 2, 4 )
        sparse_matrix_four = SparseMatrix([1, 1, 2], [(0, 1), (1, 0), (1, 1)], 2, 4 )
        sparse_matrix_sum = sparse_matrix_three + sparse_matrix_four
        
        self.assertEqual(sparse_matrix_sum.element_list, [1, 1, 1, 4, 3])
        self.assertEqual(sparse_matrix_sum.coordinate_list, [(0, 0), (0, 1), (1, 0), (1, 1), (1,2)])
    
        sparse_matrix_five = SparseMatrix([1, 2, 3, 4], [(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2 )
        sparse_matrix_six = SparseMatrix([-1, -2, -3, -4], [(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2 )
        sparse_matrix_sum = sparse_matrix_five + sparse_matrix_six
       
        self.assertEqual(sparse_matrix_sum.element_list, [])
        self.assertEqual(sparse_matrix_sum.coordinate_list, [])
    
    
    def test_sub(self):
        sparse_matrix_one = SparseMatrix([1, 2, 3, 4], [(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2 )
        sparse_matrix_two = SparseMatrix([2, 3, 4, 5], [(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2 )
        sparse_matrix_sub = sparse_matrix_one - sparse_matrix_two
        
        self.assertEqual(sparse_matrix_sub.element_list, [-1, -1, -1, -1])
        self.assertEqual(sparse_matrix_sub.coordinate_list, [(0, 0), (0, 1), (1, 0), (1, 1)])
    
        sparse_matrix_three = SparseMatrix([1, 2, 3], [(0, 0), (1, 1), (1, 2)], 2, 4 )
        sparse_matrix_four = SparseMatrix([1, 1, 2], [(0, 1), (1, 0), (1, 1)], 2, 4 )
        sparse_matrix_sub = sparse_matrix_three - sparse_matrix_four
        
        self.assertEqual(sparse_matrix_sub.element_list, [1, -1, -1, 3])
        self.assertEqual(sparse_matrix_sub.coordinate_list, [(0, 0), (0, 1), (1, 0), (1,2)])
    
    def test_mult(self):
        sparse_matrix_one = SparseMatrix([1, 2, 3, 4], [(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2 )
        sparse_matrix_two = SparseMatrix([2, 3, 4, 5], [(0, 0), (0, 1), (1, 0), (1, 1)], 2, 2 )
        sparse_matrix_mul = sparse_matrix_one*sparse_matrix_two
        
        self.assertEqual(sparse_matrix_mul.element_list, [10, 13, 22, 29])
        self.assertEqual(sparse_matrix_mul.coordinate_list, [(0, 0), (0, 1), (1, 0), (1, 1)])
        self.assertEqual(sparse_matrix_mul.size_rows, 2)
        self.assertEqual(sparse_matrix_mul.size_cols, 2)
    
        sparse_matrix_three = SparseMatrix([1, 2], [(0, 0), (0, 1)], 3, 2 )
        sparse_matrix_four = SparseMatrix([2, 3], [(1, 0), (1, 1)], 2, 2 )
        sparse_matrix_mul = sparse_matrix_three*sparse_matrix_four
        
        self.assertEqual(sparse_matrix_mul.element_list, [4, 6])
        self.assertEqual(sparse_matrix_mul.coordinate_list, [(0, 0), (0, 1)])
        self.assertEqual(sparse_matrix_mul.size_rows, 3)
        self.assertEqual(sparse_matrix_mul.size_cols, 2)
        
        sparse_matrix_five = SparseMatrix([1, 1, 1], [(0, 0), (1, 1), (2, 2)], 4, 3 )
        sparse_matrix_six = SparseMatrix([1, 1, 1], [(0, 0), (1, 0), (2, 0)], 3, 5 )
        sparse_matrix_mul = sparse_matrix_five*sparse_matrix_six
        
        self.assertEqual(sparse_matrix_mul.element_list, [1, 1, 1])
        self.assertEqual(sparse_matrix_mul.coordinate_list, [(0, 0), (1, 0), (2, 0)])
        self.assertEqual(sparse_matrix_mul.size_rows, 4)
        self.assertEqual(sparse_matrix_mul.size_cols, 5)
    
if __name__ == '__main__':
    unittest.main()
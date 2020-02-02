class SparseMatrix:

    def __init__(self, element_list, coordinate_list, m, n):
        """Class for performing basic operations with two-dimensional sparse matrices

        Attributes:
                element_list (list): non-zero elements of matrix
                coordinate_list (list): position of non-zero element in a matrix, list of tuples
                size_rows (int): number of rows
                size_cols (int): number of columns

        """

        try:
            assert len(element_list) == len(coordinate_list)
        except AssertionError as error:
            raise

        self.element_list = element_list
        self.coordinate_list = coordinate_list
        self.size_rows = m
        self.size_cols = n
        
        return
    
                 
    def __add__(self, other):        
        """Function to add together sparse matrices 
        
        Args:
            other (SparseMatrix): SparseMatrix instance
            
        Returns:
            SparseMatrix: SparseMatrix instance
            
        """
        
        try:
            assert self.size_rows == other.size_rows, 'matrices are of different size (rows)'
            assert self.size_cols == other.size_cols, 'matrices are of different size (columns)'
        except AssertionError as error:
            raise
        
        all_coordinates = sorted(list(set(self.coordinate_list).union(other.coordinate_list)))
        all_elements = [0] * len(all_coordinates)
        non_zero_elem_list = []
        non_zero_coor_list = []
        
        for i in range(len(all_coordinates)):
            if (all_coordinates[i] in self.coordinate_list) & (all_coordinates[i] in other.coordinate_list):
                all_elements[i] = self.element_list[self.coordinate_list.index(all_coordinates[i])]  + \
                other.element_list[other.coordinate_list.index(all_coordinates[i])]
                continue
            
            if all_coordinates[i] in self.coordinate_list:
                all_elements[i] =  self.element_list[self.coordinate_list.index(all_coordinates[i])]
                continue
                
            if all_coordinates[i] in other.coordinate_list:
                all_elements[i] =  other.element_list[other.coordinate_list.index(all_coordinates[i])]
                continue

        for i in range(len(all_elements)):
            if all_elements[i] != 0:
                non_zero_elem_list.append(all_elements[i])
                non_zero_coor_list.append(all_coordinates[i])
            
                
        result = SparseMatrix(non_zero_elem_list, non_zero_coor_list, self.size_rows, self.size_cols )
                
        return result      

    
    def __sub__(self, other):
        """Function to subtract one sparse matrix from another
        
        Args:
            other (SparseMatrix): SparseMatrix instance
            
        Returns:
            SparseMatrix: SparseMatrix instance
            
        """
  
        try:
            assert self.size_rows == other.size_rows, 'matrices are of different size (rows)'
            assert self.size_cols == other.size_cols, 'matrices are of different size (columns)'
        except AssertionError as error:
            raise
        
        minus_elem = [-a for a in other.element_list]
        minus_other = SparseMatrix(minus_elem, other.coordinate_list, other.size_rows, other.size_cols )
        result = self + minus_other
        return result
    
    def __mul__(self, other):
        """Function to multiplicate two sparse matrices
        
        Args:
            other (SparseMatrix): SparseMatrix instance
            
        Returns:
            SparseMatrix: SparseMatrix instance
            
        """
  
        try:
            assert self.size_cols == other.size_rows, 'dimensions mismatch'
        except AssertionError as error:
            raise
        
        coord_list = []
        elem_list = []
        
        for i in range(len(self.coordinate_list)):
            for j in range(len(other.coordinate_list)):
                a = self.element_list[i]
                b = other.element_list[j]
                if self.coordinate_list[i][1] == other.coordinate_list[j][0]:
                    coordinate = (self.coordinate_list[i][0], other.coordinate_list[j][1])
                    if coordinate in coord_list:
                        elem_list[coord_list.index(coordinate)] = \
                        elem_list[coord_list.index(coordinate)] + a*b
                    else:
                        coord_list.append(coordinate)
                        elem_list.append(a*b)
                        
        
        result = SparseMatrix(elem_list, coord_list, self.size_rows, other.size_cols)
        
        return result

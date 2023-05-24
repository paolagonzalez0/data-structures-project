
import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BSTTester(unittest.TestCase):
  
    def setUp(self):
        self.__bst = Binary_Search_Tree()

    # Empty BST
    def test_empty_bst(self):
        self.assertEqual("[ ]", str(self.__bst))
        self.assertEqual("[ ]", self.__bst.in_order())
        self.assertEqual("[ ]", self.__bst.pre_order())
        self.assertEqual("[ ]", self.__bst.post_order())
        self.assertEqual([], self.__bst.to_list())
        self.assertEqual(0, self.__bst.get_height())
    # One Value
    def test_one_value(self):
        self.__bst.insert_element(10)
        self.assertEqual("[ 10 ]", str(self.__bst))
        self.assertEqual("[ 10 ]", self.__bst.in_order())
        self.assertEqual("[ 10 ]", self.__bst.pre_order())
        self.assertEqual("[ 10 ]", self.__bst.post_order())
        self.assertEqual([10], self.__bst.to_list())
        self.assertEqual(1, self.__bst.get_height())

    def test_one_insert_remove(self):
        self.__bst.insert_element(10)
        self.__bst.remove_element(10)
        self.assertEqual("[ ]", str(self.__bst))
        self.assertEqual("[ ]", self.__bst.in_order())
        self.assertEqual("[ ]", self.__bst.pre_order())
        self.assertEqual("[ ]", self.__bst.post_order())
        self.assertEqual([], self.__bst.to_list())
        self.assertEqual(0, self.__bst.get_height())
    
    def test_left_value(self):
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.assertEqual("[ 5, 10 ]", str(self.__bst))
        self.assertEqual("[ 5, 10 ]", self.__bst.in_order())
        self.assertEqual("[ 10, 5 ]", self.__bst.pre_order())
        self.assertEqual("[ 5, 10 ]", self.__bst.post_order())
        self.assertEqual([5, 10], self.__bst.to_list())
        self.assertEqual(2, self.__bst.get_height())

    def test_right_value(self):
        self.__bst.insert_element(5)
        self.__bst.insert_element(10)
        self.assertEqual("[ 5, 10 ]", str(self.__bst))
        self.assertEqual("[ 5, 10 ]", self.__bst.in_order())
        self.assertEqual("[ 5, 10 ]", self.__bst.pre_order())
        self.assertEqual("[ 10, 5 ]", self.__bst.post_order())
        self.assertEqual([5, 10], self.__bst.to_list())
        self.assertEqual(2, self.__bst.get_height())
    
    def test_single_left_rotation(self):
        self.__bst.insert_element(15)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)
        self.assertEqual("[ 5, 10, 15 ]", str(self.__bst))
        self.assertEqual("[ 5, 10, 15 ]", self.__bst.in_order())
        self.assertEqual("[ 10, 5, 15 ]", self.__bst.pre_order())
        self.assertEqual("[ 5, 15, 10 ]", self.__bst.post_order())
        self.assertEqual([5, 10, 15], self.__bst.to_list())
        self.assertEqual(2, self.__bst.get_height())

    def test_single_right_rotation(self):
        self.__bst.insert_element(5)
        self.__bst.insert_element(10)
        self.__bst.insert_element(15)
        self.assertEqual("[ 5, 10, 15 ]", str(self.__bst))
        self.assertEqual("[ 5, 10, 15 ]", self.__bst.in_order())
        self.assertEqual("[ 10, 5, 15 ]", self.__bst.pre_order())
        self.assertEqual("[ 5, 15, 10 ]", self.__bst.post_order())
        self.assertEqual([5, 10, 15], self.__bst.to_list())
        self.assertEqual(2, self.__bst.get_height())

    def test_double_left_right_rotation(self):
        self.__bst.insert_element(15)
        self.__bst.insert_element(5)
        self.__bst.insert_element(10)
        self.assertEqual("[ 5, 10, 15 ]", str(self.__bst))
        self.assertEqual("[ 5, 10, 15 ]", self.__bst.in_order())
        self.assertEqual("[ 10, 5, 15 ]", self.__bst.pre_order())
        self.assertEqual("[ 5, 15, 10 ]", self.__bst.post_order())
        self.assertEqual([5, 10, 15], self.__bst.to_list())
        self.assertEqual(2, self.__bst.get_height())
    
    def test_double_right_left_rotation(self):
        self.__bst.insert_element(5)
        self.__bst.insert_element(15)
        self.__bst.insert_element(10)
        self.assertEqual("[ 5, 10, 15 ]", str(self.__bst))
        self.assertEqual("[ 5, 10, 15 ]", self.__bst.in_order())
        self.assertEqual("[ 10, 5, 15 ]", self.__bst.pre_order())
        self.assertEqual("[ 5, 15, 10 ]", self.__bst.post_order())
        self.assertEqual([5, 10, 15], self.__bst.to_list())
        self.assertEqual(2, self.__bst.get_height())

    def test_recursive_left_rotation(self):
        self.__bst.insert_element(10)
        self.__bst.insert_element(20)
        self.__bst.insert_element(30) # Left Rotation
        self.__bst.insert_element(40)
        self.__bst.insert_element(50) # Left Rotation
        self.__bst.insert_element(60) # Left Rotation
        self.__bst.insert_element(70) # Left Rotation
        self.__bst.insert_element(80) 
        self.__bst.insert_element(90) # Left Rotation
        self.__bst.insert_element(100) # Left Rotation

        self.assertEqual("[ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]", str(self.__bst))
        self.assertEqual("[ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]", self.__bst.in_order())
        self.assertEqual("[ 40, 20, 10, 30, 80, 60, 50, 70, 90, 100 ]", self.__bst.pre_order())
        self.assertEqual("[ 10, 30, 20, 50, 70, 60, 100, 90, 80, 40 ]", self.__bst.post_order())
        self.assertEqual([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], self.__bst.to_list())
        self.assertEqual(4, self.__bst.get_height())

    def test_recursive_right_rotation(self):
        self.__bst.insert_element(100)
        self.__bst.insert_element(90)
        self.__bst.insert_element(80) # Right Rotation
        self.__bst.insert_element(70)
        self.__bst.insert_element(60) # Right Rotation
        self.__bst.insert_element(50) # Right Rotation
        self.__bst.insert_element(40) # Right Rotation
        self.__bst.insert_element(30) 
        self.__bst.insert_element(20) # Right Rotation
        self.__bst.insert_element(10) # Right Rotation

        self.assertEqual("[ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]", str(self.__bst))
        self.assertEqual("[ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 ]", self.__bst.in_order())
        self.assertEqual("[ 70, 30, 20, 10, 50, 40, 60, 90, 80, 100 ]", self.__bst.pre_order())
        self.assertEqual("[ 10, 20, 40, 60, 50, 30, 80, 100, 90, 70 ]", self.__bst.post_order())
        self.assertEqual([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], self.__bst.to_list())
        self.assertEqual(4, self.__bst.get_height())

    def test_recursive_left_right_rotation(self):
        self.__bst.insert_element(50)
        self.__bst.insert_element(30)
        self.__bst.insert_element(40) # Left-right Rotation
        self.__bst.insert_element(20)
        self.__bst.insert_element(25) # Left-right Rotation
        self.__bst.insert_element(45) 
        self.__bst.insert_element(47) # Left-right Rotation
        self.__bst.insert_element(44) 
        self.__bst.insert_element(43) # Right Rotation
        self.__bst.insert_element(46) # Left-right Rotation

        self.assertEqual("[ 20, 25, 30, 40, 43, 44, 45, 46, 47, 50 ]", str(self.__bst))
        self.assertEqual("[ 20, 25, 30, 40, 43, 44, 45, 46, 47, 50 ]", self.__bst.in_order())
        self.assertEqual("[ 40, 25, 20, 30, 45, 44, 43, 47, 46, 50 ]", self.__bst.pre_order())
        self.assertEqual("[ 20, 30, 25, 43, 44, 46, 50, 47, 45, 40 ]", self.__bst.post_order())
        self.assertEqual([20, 25, 30, 40, 43, 44, 45, 46, 47, 50], self.__bst.to_list())
        self.assertEqual(4, self.__bst.get_height())

    def test_recursive_right_left_rotation(self):
        self.__bst.insert_element(50)
        self.__bst.insert_element(90)
        self.__bst.insert_element(75) # Right-left Rotation
        self.__bst.insert_element(100)
        self.__bst.insert_element(95) # Right-left Rotation
        self.__bst.insert_element(60) 
        self.__bst.insert_element(55) # Right-left Rotation
        self.__bst.insert_element(120) 
        self.__bst.insert_element(110) # Right-left Rotation
        self.__bst.insert_element(97) # Right-left Rotation

        self.assertEqual("[ 50, 55, 60, 75, 90, 95, 97, 100, 110, 120 ]", str(self.__bst))
        self.assertEqual("[ 50, 55, 60, 75, 90, 95, 97, 100, 110, 120 ]", self.__bst.in_order())
        self.assertEqual("[ 75, 55, 50, 60, 100, 95, 90, 97, 110, 120 ]", self.__bst.pre_order())
        self.assertEqual("[ 50, 60, 55, 90, 97, 95, 120, 110, 100, 75 ]", self.__bst.post_order())
        self.assertEqual([50, 55, 60, 75, 90, 95, 97, 100, 110, 120], self.__bst.to_list())
        self.assertEqual(4, self.__bst.get_height())

    def test_left_to_right_floater(self):
        self.__bst.insert_element(15)
        self.__bst.insert_element(10)        
        self.__bst.insert_element(20)
        self.__bst.insert_element(5)        
        self.__bst.insert_element(12)
        self.__bst.insert_element(3) # Rotation with floater 12
        self.assertEqual("[ 3, 5, 10, 12, 15, 20 ]", str(self.__bst))
        self.assertEqual("[ 3, 5, 10, 12, 15, 20 ]", self.__bst.in_order())
        self.assertEqual("[ 10, 5, 3, 15, 12, 20 ]", self.__bst.pre_order())
        self.assertEqual("[ 3, 5, 12, 20, 15, 10 ]", self.__bst.post_order())
        self.assertEqual([3, 5, 10, 12, 15, 20], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

    def test_right_to_left_floater(self):
        self.__bst.insert_element(15)
        self.__bst.insert_element(10)        
        self.__bst.insert_element(20)
        self.__bst.insert_element(25)        
        self.__bst.insert_element(17)
        self.__bst.insert_element(30) # Rotation with floater 17
        self.assertEqual("[ 10, 15, 17, 20, 25, 30 ]", str(self.__bst))
        self.assertEqual("[ 10, 15, 17, 20, 25, 30 ]", self.__bst.in_order())
        self.assertEqual("[ 20, 15, 10, 17, 25, 30 ]", self.__bst.pre_order())
        self.assertEqual("[ 10, 17, 15, 30, 25, 20 ]", self.__bst.post_order())
        self.assertEqual([10, 15, 17, 20, 25, 30], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

    def test_duplicate_value_insertion(self):
        self.__bst.insert_element(95)  
        with self.assertRaises(ValueError):     
            self.__bst.insert_element(95)    
        self.assertEqual("[ 95 ]", str(self.__bst))
        self.assertEqual("[ 95 ]", self.__bst.in_order())
        self.assertEqual("[ 95 ]", self.__bst.pre_order())
        self.assertEqual("[ 95 ]", self.__bst.post_order())
        self.assertEqual([95], self.__bst.to_list())
        self.assertEqual(1, self.__bst.get_height())

    def test_removing_nonexistent_value(self):
        with self.assertRaises(ValueError):     
            self.__bst.remove_element(95)
        self.__bst.insert_element(95)    
        with self.assertRaises(ValueError):     
            self.__bst.remove_element(20)
        self.assertEqual("[ 95 ]", str(self.__bst))
        self.assertEqual("[ 95 ]", self.__bst.in_order())
        self.assertEqual("[ 95 ]", self.__bst.pre_order())
        self.assertEqual("[ 95 ]", self.__bst.post_order())
        self.assertEqual([95], self.__bst.to_list())
        self.assertEqual(1, self.__bst.get_height())

    def test_1(self): 
        self.__bst.insert_element(20)
        self.__bst.insert_element(10)
        self.__bst.insert_element(40)
        self.__bst.insert_element(5)
        self.__bst.insert_element(15)
        self.__bst.insert_element(12) 
        self.assertEqual("[ 5, 10, 12, 15, 20, 40 ]", str(self.__bst))
        self.assertEqual("[ 5, 10, 12, 15, 20, 40 ]", self.__bst.in_order())
        self.assertEqual("[ 15, 10, 5, 12, 20, 40 ]", self.__bst.pre_order())
        self.assertEqual("[ 5, 12, 10, 40, 20, 15 ]", self.__bst.post_order())
        self.assertEqual([5, 10, 12, 15, 20, 40], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

    def test_2(self): 
        self.__bst.insert_element(50)
        self.__bst.insert_element(20)
        self.__bst.insert_element(75)
        self.__bst.insert_element(80)
        self.__bst.insert_element(90) # rotate right

        self.__bst.remove_element(75) # remove leaf node
        self.__bst.insert_element(75)

        self.__bst.remove_element(20) #rotate right
        self.__bst.remove_element(50) # remove node with right child

        self.__bst.insert_element(83)
        self.__bst.insert_element(81) # rotate left
        self.__bst.insert_element(85) # rotate right
        self.__bst.insert_element(82)

        self.__bst.remove_element(80) # remove node with 2 children
        self.__bst.remove_element(81) # remove node with 2 children

        self.assertEqual("[ 75, 82, 83, 85, 90 ]", str(self.__bst))
        self.assertEqual("[ 75, 82, 83, 85, 90 ]", self.__bst.in_order())
        self.assertEqual("[ 83, 82, 75, 90, 85 ]", self.__bst.pre_order())
        self.assertEqual("[ 75, 82, 85, 90, 83 ]", self.__bst.post_order())
        self.assertEqual([75, 82, 83, 85, 90], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

    def test_3(self):
        self.__bst.insert_element(50)
        self.__bst.insert_element(30)
        self.__bst.insert_element(20)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)       
        self.__bst.insert_element(25)       
        self.__bst.insert_element(60)       
        self.__bst.insert_element(70)       
        self.__bst.insert_element(80)       
        self.__bst.insert_element(22) 
        self.assertEqual("[ 5, 10, 20, 22, 25, 30, 50, 60, 70, 80 ]", str(self.__bst))
        self.assertEqual("[ 5, 10, 20, 22, 25, 30, 50, 60, 70, 80 ]", self.__bst.in_order())
        self.assertEqual("[ 5, 10, 20, 22, 25, 30, 50, 60, 70, 80 ]", self.__bst.in_order())
        self.assertEqual("[ 30, 20, 10, 5, 25, 22, 60, 50, 70, 80 ]", self.__bst.pre_order())
        self.assertEqual("[ 5, 10, 22, 25, 20, 50, 80, 70, 60, 30 ]", self.__bst.post_order())
        self.assertEqual([5, 10, 20, 22, 25, 30, 50, 60, 70, 80], self.__bst.to_list())
        self.assertEqual(4, self.__bst.get_height())

    def test_4(self):
        self.__bst.insert_element(25)
        self.__bst.insert_element(30)
        self.__bst.insert_element(31)
        self.__bst.insert_element(50)
        self.__bst.insert_element(45)       
        self.__bst.insert_element(55)       
        self.__bst.insert_element(34)

        self.__bst.remove_element(50)
        self.__bst.remove_element(25)
        self.__bst.remove_element(30)

        self.assertEqual("[ 31, 34, 45, 55 ]", str(self.__bst))
        self.assertEqual("[ 31, 34, 45, 55 ]", self.__bst.in_order())
        self.assertEqual("[ 45, 31, 34, 55 ]", self.__bst.pre_order())
        self.assertEqual("[ 34, 31, 55, 45 ]", self.__bst.post_order())
        self.assertEqual([31, 34, 45, 55], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

    def test_5(self):
        self.__bst.insert_element(25)
        self.__bst.insert_element(30)
        self.__bst.remove_element(25)
        self.assertEqual("[ 30 ]", str(self.__bst))
        self.assertEqual("[ 30 ]", self.__bst.in_order())
        self.assertEqual("[ 30 ]", self.__bst.pre_order())
        self.assertEqual("[ 30 ]", self.__bst.post_order())
        self.assertEqual([30], self.__bst.to_list())
        self.assertEqual(1, self.__bst.get_height())

    def test_6(self):
        self.__bst.insert_element(25)
        self.__bst.insert_element(30)
        self.__bst.remove_element(30)
        self.assertEqual("[ 25 ]", str(self.__bst))
        self.assertEqual("[ 25 ]", self.__bst.in_order())
        self.assertEqual("[ 25 ]", self.__bst.pre_order())
        self.assertEqual("[ 25 ]", self.__bst.post_order())
        self.assertEqual([25], self.__bst.to_list())
        self.assertEqual(1, self.__bst.get_height())

    def test_7(self):
        self.__bst.insert_element(45)
        self.__bst.insert_element(40)
        self.__bst.insert_element(50)
        self.__bst.insert_element(35)
        self.__bst.insert_element(30)
        self.assertEqual("[ 30, 35, 40, 45, 50 ]", str(self.__bst))
        self.assertEqual("[ 30, 35, 40, 45, 50 ]", self.__bst.in_order())
        self.assertEqual("[ 45, 35, 30, 40, 50 ]", self.__bst.pre_order())
        self.assertEqual("[ 30, 40, 35, 50, 45 ]", self.__bst.post_order())
        self.assertEqual([30, 35, 40, 45, 50], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

        self.__bst.remove_element(35)
        self.assertEqual("[ 30, 40, 45, 50 ]", str(self.__bst))
        self.assertEqual("[ 30, 40, 45, 50 ]", self.__bst.in_order())
        self.assertEqual("[ 45, 40, 30, 50 ]", self.__bst.pre_order())
        self.assertEqual("[ 30, 40, 50, 45 ]", self.__bst.post_order())
        self.assertEqual([30, 40, 45, 50], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

    def test_8(self):
        self.__bst.insert_element(45)
        self.__bst.insert_element(40)
        self.__bst.insert_element(50)
        self.__bst.insert_element(55)
        self.__bst.insert_element(60)

        self.assertEqual("[ 40, 45, 50, 55, 60 ]", str(self.__bst))
        self.assertEqual("[ 40, 45, 50, 55, 60 ]", self.__bst.in_order())
        self.assertEqual("[ 45, 40, 55, 50, 60 ]", self.__bst.pre_order())
        self.assertEqual("[ 40, 50, 60, 55, 45 ]", self.__bst.post_order())
        self.assertEqual([40, 45, 50, 55, 60], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

        self.__bst.remove_element(45)
        self.assertEqual("[ 40, 50, 55, 60 ]", str(self.__bst))
        self.assertEqual("[ 40, 50, 55, 60 ]", self.__bst.in_order())
        self.assertEqual("[ 50, 40, 55, 60 ]", self.__bst.pre_order())
        self.assertEqual("[ 40, 60, 55, 50 ]", self.__bst.post_order())
        self.assertEqual([40, 50, 55, 60], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

    def test_9(self):
        self.__bst.insert_element(45)
        self.__bst.insert_element(40)
        self.__bst.insert_element(55)
        self.__bst.insert_element(50)        
        self.__bst.insert_element(35)
        self.__bst.insert_element(60)
    
        self.__bst.remove_element(50)
        self.__bst.remove_element(40)
        self.__bst.remove_element(35)

        self.assertEqual("[ 45, 55, 60 ]", str(self.__bst))
        self.assertEqual("[ 45, 55, 60 ]", self.__bst.in_order())
        self.assertEqual("[ 55, 45, 60 ]", self.__bst.pre_order())
        self.assertEqual("[ 45, 60, 55 ]", self.__bst.post_order())
        self.assertEqual([45, 55, 60], self.__bst.to_list())
        self.assertEqual(2, self.__bst.get_height())

    def test_10(self):
        self.__bst.insert_element(75)
        self.__bst.insert_element(65)
        self.__bst.insert_element(80)
        self.__bst.insert_element(85)        
        self.__bst.insert_element(60)
        self.__bst.insert_element(70)
    
        self.__bst.remove_element(75)
        self.__bst.remove_element(80)

        self.assertEqual("[ 60, 65, 70, 85 ]", str(self.__bst))
        self.assertEqual("[ 60, 65, 70, 85 ]", self.__bst.in_order())
        self.assertEqual("[ 65, 60, 85, 70 ]", self.__bst.pre_order())
        self.assertEqual("[ 60, 70, 85, 65 ]", self.__bst.post_order())
        self.assertEqual([60, 65, 70, 85], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

    def test_11(self):
        self.__bst.insert_element(40)
        self.__bst.insert_element(65)
        self.__bst.insert_element(75)
        self.__bst.insert_element(25)        
        self.__bst.insert_element(10)
        self.__bst.insert_element(60)
    
        self.__bst.remove_element(65)
        self.__bst.remove_element(40)
        self.__bst.remove_element(25)

        self.assertEqual("[ 10, 60, 75 ]", str(self.__bst))
        self.assertEqual("[ 10, 60, 75 ]", self.__bst.in_order())
        self.assertEqual("[ 60, 10, 75 ]", self.__bst.pre_order())
        self.assertEqual("[ 10, 75, 60 ]", self.__bst.post_order())
        self.assertEqual([10, 60, 75], self.__bst.to_list())
        self.assertEqual(2, self.__bst.get_height())

    def test_12(self): # Insert all, remove all
        self.__bst.insert_element(50)
        self.__bst.insert_element(30)
        self.__bst.insert_element(20)
        self.__bst.insert_element(10)
        self.__bst.insert_element(5)       
        self.__bst.insert_element(25)       
        self.__bst.insert_element(60)       
        self.__bst.insert_element(70)       
        self.__bst.insert_element(80)       
        self.__bst.insert_element(22) 
        self.__bst.remove_element(5)       
        self.__bst.remove_element(25)
        self.__bst.remove_element(50)
        self.__bst.remove_element(30)
        self.__bst.remove_element(20)
        self.__bst.remove_element(70)       
        self.__bst.remove_element(80)       
        self.__bst.remove_element(22) 
        self.__bst.remove_element(10)       
        self.__bst.remove_element(60)       

        self.assertEqual("[ ]", str(self.__bst))
        self.assertEqual("[ ]", self.__bst.in_order())
        self.assertEqual("[ ]", self.__bst.pre_order())
        self.assertEqual("[ ]", self.__bst.post_order())
        self.assertEqual([], self.__bst.to_list())
        self.assertEqual(0, self.__bst.get_height())

    def test_13(self):
        self.__bst.insert_element(70)
        self.__bst.insert_element(40)
        self.__bst.insert_element(50) # Left-right rotation, remove leaf node
        self.__bst.insert_element(80)
        self.__bst.insert_element(30)   
        with self.assertRaises(ValueError): # Removing value that is not in the tree  
            self.__bst.remove_element(95)    
        self.__bst.insert_element(90)     
        self.__bst.remove_element(30) # Remove leaf node, right rotation
        self.__bst.insert_element(60) # Right-left rotation
        self.__bst.insert_element(65)       
        self.__bst.insert_element(55)  
        self.__bst.remove_element(50) # Remove value with two children
        self.__bst.remove_element(60) # Remove node with right child only
        self.__bst.insert_element(85)       
        self.__bst.remove_element(90) # Remove node with left child only
        self.__bst.insert_element(75)   
        self.__bst.remove_element(65) # Remove leaf node
        self.__bst.insert_element(83)   
        self.__bst.remove_element(40) # Left rotation
    
        self.assertEqual("[ 55, 70, 75, 80, 83, 85 ]", str(self.__bst))
        self.assertEqual("[ 55, 70, 75, 80, 83, 85 ]", self.__bst.in_order())
        self.assertEqual("[ 80, 70, 55, 75, 85, 83 ]", self.__bst.pre_order())
        self.assertEqual("[ 55, 75, 70, 83, 85, 80 ]", self.__bst.post_order())
        self.assertEqual([55, 70, 75, 80, 83, 85], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

    def test_14(self):
        self.__bst.insert_element(60)
        self.__bst.insert_element(30) 
        self.__bst.insert_element(90)
        with self.assertRaises(ValueError):     
            self.__bst.insert_element(90)
        self.__bst.insert_element(75)       
        self.__bst.insert_element(100)     
        self.__bst.remove_element(60) # Remove root value 
        self.__bst.insert_element(80)
        self.__bst.remove_element(30) # Left rotation 
        self.__bst.insert_element(77) # Left-right rotation
        self.__bst.insert_element(50) # Right rotation
        self.__bst.insert_element(76)
        self.__bst.insert_element(95) 
        self.__bst.remove_element(80) # Remove leaf node
        self.__bst.insert_element(97)
        self.__bst.insert_element(110)  
        self.__bst.remove_element(95) # Remove value with 2 children
        self.__bst.remove_element(110) # Remove leaf node
        self.__bst.remove_element(100) # Remove leaf node
        self.__bst.remove_element(97) # Remove node with only left child
        self.__bst.remove_element(50) # Remove leaf node
        self.__bst.remove_element(75) # Remove node with only right child

        self.assertEqual("[ 76, 77, 90 ]", str(self.__bst))
        self.assertEqual("[ 76, 77, 90 ]", self.__bst.in_order())
        self.assertEqual("[ 77, 76, 90 ]", self.__bst.pre_order())
        self.assertEqual("[ 76, 90, 77 ]", self.__bst.post_order())
        self.assertEqual([76, 77, 90], self.__bst.to_list())
        self.assertEqual(2, self.__bst.get_height())
        
    def test_15(self):
        self.__bst.insert_element(75)
        self.__bst.insert_element(50) 
        self.__bst.insert_element(110)
        self.__bst.insert_element(95)  
        with self.assertRaises(ValueError):     
            self.__bst.insert_element(95)      
        self.__bst.insert_element(150) 
        self.__bst.insert_element(170) # Left rotation
        self.__bst.insert_element(65) 
        self.__bst.remove_element(170) # Right rotation, Remove leaf node
        self.__bst.insert_element(55) # Right-left Rotation
        self.__bst.remove_element(75) # Removed root
        self.__bst.insert_element(53)  # Left-right rotation
        self.__bst.remove_element(55) # Remove node with right child only
        self.__bst.remove_element(65) 
        self.__bst.remove_element(53) # Remove node with left child only

        self.assertEqual("[ 50, 95, 110, 150 ]", str(self.__bst))
        self.assertEqual("[ 50, 95, 110, 150 ]", self.__bst.in_order())
        self.assertEqual("[ 95, 50, 110, 150 ]", self.__bst.pre_order())
        self.assertEqual("[ 50, 150, 110, 95 ]", self.__bst.post_order())
        self.assertEqual([50, 95, 110, 150], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())

    def test_16(self):
        self.__bst.insert_element(65)
        self.__bst.insert_element(45) 
        self.__bst.insert_element(95)
        self.__bst.insert_element(80)       
        self.__bst.insert_element(110) 
        self.__bst.insert_element(30)
        self.__bst.insert_element(50)
        self.__bst.remove_element(45)
        self.__bst.remove_element(30) 
        self.__bst.remove_element(65)         
        self.__bst.remove_element(80) 
        self.__bst.remove_element(50) 

        self.assertEqual("[ 95, 110 ]", str(self.__bst))
        self.assertEqual("[ 95, 110 ]", self.__bst.in_order())
        self.assertEqual("[ 95, 110 ]", self.__bst.pre_order())
        self.assertEqual("[ 110, 95 ]", self.__bst.post_order())
        self.assertEqual([95, 110], self.__bst.to_list())
        self.assertEqual(2, self.__bst.get_height())

    def test_17(self):
        self.__bst.insert_element(80)
        self.__bst.insert_element(100)       
        self.__bst.insert_element(90) 
        self.__bst.insert_element(95)
        self.__bst.insert_element(97)        
        self.__bst.insert_element(85)
        self.__bst.remove_element(80) 
        self.__bst.remove_element(85)         
        self.__bst.remove_element(97) 
        self.__bst.remove_element(100) 

        self.assertEqual("[ 90, 95 ]", str(self.__bst))
        self.assertEqual("[ 90, 95 ]", self.__bst.in_order())
        self.assertEqual("[ 95, 90 ]", self.__bst.pre_order())
        self.assertEqual("[ 90, 95 ]", self.__bst.post_order())
        self.assertEqual([90, 95], self.__bst.to_list())
        self.assertEqual(2, self.__bst.get_height())

        self.__bst.insert_element(93) 
        self.__bst.insert_element(105)        
        self.__bst.insert_element(91) 
        self.__bst.insert_element(92)
        self.__bst.remove_element(91) 

        self.assertEqual("[ 90, 92, 93, 95, 105 ]", str(self.__bst))
        self.assertEqual("[ 90, 92, 93, 95, 105 ]", self.__bst.in_order())
        self.assertEqual("[ 93, 92, 90, 95, 105 ]", self.__bst.pre_order())
        self.assertEqual("[ 90, 92, 105, 95, 93 ]", self.__bst.post_order())
        self.assertEqual([90, 92, 93, 95, 105], self.__bst.to_list())
        self.assertEqual(3, self.__bst.get_height())





if __name__ == '__main__':
  unittest.main()
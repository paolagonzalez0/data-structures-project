class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.__height = 0

  def __init__(self):
    self.__root = None

  # Inserts the value specified into the tree at the correct location based on "less is left; greater is right" binary
  # search tree ordering. If the value is already contained in the tree, raise a ValueError.
  def insert_element(self, value):
    self.__root = self.__rins(value,self.__root)

  # Private function which aids in recursivly inserting original value into binary search tree.
  def __rins(self, x, subroot):
    if subroot == None: # Base case: create a new node with value x.
      subroot = Binary_Search_Tree.__BST_Node(x)
    # If the value is less than the current subroot, recursive insert at the subroot's left node.
    elif x < subroot.value:
      subroot.left = self.__rins(x,subroot.left)
    # If the value is greater than the current subroot, recursive insert at the subroot's right node.
    elif x > subroot.value:
      subroot.right = self.__rins(x,subroot.right)
    elif x == subroot.value: # If the value is a dupilcate, raise a ValueError.
      raise ValueError
    subroot = self.__balance(subroot) # Balance the subtree.
    subroot.__height = self.__cur_height(subroot) # Calculate the height of the current subroot.
    return subroot

  # Removes the value specified from the tree, raising a ValueError if the value isn't found. When a replacement value is
  # necessary, the minimum value from the right is selected as this element's replacement.
  def remove_element(self, value):
    self.__root = self.__rrem(value, self.__root)

  # Private function which aids in recursivly removing original value from binary search tree.
  def __rrem(self, x, subroot):
    if subroot == None: # If value is not found, raise ValueError.
      raise ValueError
    # If value is less than the current subroot's value, recursive remove at the subroot's left node.
    if x < subroot.value:
      subroot.left = self.__rrem(x, subroot.left)
    # If value is greater than the current subroot's value, recursive remove at the subroot's right node.
    elif x > subroot.value:
      subroot.right = self.__rrem(x, subroot.right)
    elif x == subroot.value: # If you found the value to remove, check its number of children.
      # Current subroot has no children.
      if subroot.left is None and subroot.right is None:
        subroot = None # Set subroot to None.
      # Current subroot has right children only.
      elif subroot.left is None and subroot.right is not None: 
        subroot = subroot.right # Set subroot's right child as new subroot.
      # Current subroot has left children only.
      elif subroot.right is None and subroot.left is not None: 
        subroot = subroot.left  # Set subroot's left child as new subroot.
      # Current subroot has both left and right children.
      elif subroot.left is not None and subroot.right is not None:
        subroot.value = self.__min_from_right(subroot.right) # Set subroot's value to the minimum from right.
        # Remove the original minimum from right node from subroot's right subtree.
        subroot.right = self.__rrem(subroot.value, subroot.right)
        subroot = self.__balance(subroot) # Balance the tree before taking the new heights.
        subroot.__height = self.__cur_height(subroot) # Calculate the height of the current subroot.
      return subroot
    subroot = self.__balance(subroot) # Balance the tree before taking the new heights.
    subroot.__height = self.__cur_height(subroot) # Calculate the height of the current subroot.
    return subroot
    
  # Private function that recursively finds and returns the minimum value from the right.
  def __min_from_right(self, subroot):
    # Base case: Return the current value (minimum from right).
    if subroot.left is None:
      return subroot.value
    # If the left value is not None, there is still a value smaller than the current one, so recur right.
    elif subroot.left is not None:
      cur_min = self.__min_from_right(subroot.left)
      return cur_min

  # Constructs and returns a string representing the in-order traversal of the tree. Empty trees are printed as [ ].
  # Trees with one value are printed as [ 4 ]. Trees with more than one value are printed as [ 4, 7 ].
  def in_order(self):
    if self.__root == None: # If the tree is empty, return an empty string.
      return "[ ]"
    else: # Return a string of the tree in left + parent(subroot) + right format.
      left = self.__in_trav(self.__root.left)
      right = self.__in_trav(self.__root.right)
      vals = str(left) + str(self.__root.value)+ ", " + str(right)
      vals = vals[:len(vals)-2]
      return "[ " + str(vals) + " ]"

# Private recursive function to aid in the constuction of the final in-order string representation of the binary search tree.
  def __in_trav(self, subroot):
    if subroot is None: # If the tree is empty, return an empty string.
      return ""
    else: # Return a string of the tree in left + parent(subroot) + right format.
      left = self.__in_trav(subroot.left)
      right = self.__in_trav(subroot.right)
      return str(left) + str(subroot.value)+ ", " + str(right)
    
# Constructs and returns a string representing the pre-order traversal of the tree. String is formatted the same as
# in-order string representation.
  def pre_order(self):
    # If the tree is empty, return an empty string.
    if self.__root == None:
      return "[ ]"
    # Return a string of the tree in parent(subroot) + left + right format.
    else:
      left = self.__pre_trav(self.__root.left)
      right = self.__pre_trav(self.__root.right)
      vals = str(self.__root.value) + ", " + str(left) + str(right)
      vals = vals[:len(vals)-2]
      return "[ " + str(vals) + " ]"

# Private recursive function to aid in the constuction of the final pre-order string representation of the binary search tree.
  def __pre_trav(self, subroot):
    if subroot is None: # If the tree is empty, return an empty string.
      return ""
    else: # Return a string of the tree in parent(subroot) + left + right format.
      left = self.__pre_trav(subroot.left)
      right = self.__pre_trav(subroot.right)
      return  str(subroot.value) + ", " + str(left) + str(right)
  
# Constructs and returns a string representing the post-order traversal of the tree. String is formatted the same as
# in-order string representation.
  def post_order(self):
    if self.__root == None: # If the tree is empty, return an empty string.
      return "[ ]"
    else: # Return a string of the tree in left + right + parent(subroot) format.
      left = self.__post_trav(self.__root.left)
      right = self.__post_trav(self.__root.right)
      vals = str(left) + str(right) + str(self.__root.value) + ", "
      vals = vals[:len(vals)-2]
      return "[ " + str(vals) + " ]"

# Private recursive function to aid in the constuction of the final post-order string representation of the binary search tree.
  def __post_trav(self, subroot):
    if subroot is None: # If the tree is empty, return an empty string.
      return ""
    else: # Return a string of the tree in left + right + parent(subroot) format.
      left = self.__post_trav(subroot.left)
      right = self.__post_trav(subroot.right)
      return  str(left) + str(right) + str(subroot.value) + ", "

  # Returns an integer that represents the height of the tree, 
  # assuming that an empty tree has height 0 and a tree with one node has height 1.
  def get_height(self):
    if self.__root is None:
      return 0
    return self.__root.__height

  # Private recursive function that aids in calculating the final tree height.
  def __cur_height(self, cur_root):
    if cur_root is None:
      return 0
    elif cur_root.left is None and cur_root.right is None:
      cur_root.__height = 1
    elif cur_root.left is None and cur_root.right is not None:
      cur_root.__height = cur_root.right.__height + 1
    elif cur_root.right is None and cur_root.left is not None:
      cur_root.__height = cur_root.left.__height + 1
    elif cur_root.left is not None and cur_root.right is not None:
      if cur_root.left.__height <= cur_root.right.__height:  
        cur_root.__height = cur_root.right.__height + 1
      elif cur_root.right.__height <= cur_root.left.__height:
        cur_root.__height = cur_root.left.__height + 1    
    return cur_root.__height

  # Private function that balances the binary search tree.
  def __balance(self,t):
    cur_balance = self.__cur_height(t.right) - self.__cur_height(t.left)
    if abs(cur_balance) == 1 or cur_balance == 0:
      return t
    elif abs(cur_balance) >= 2:
      # Single left cases
      if cur_balance == -2 and self.__child_balance(t.left) == -1: 
        t = self.__rotate_right(t) # Rotate left heavy tree to the right.
        cur_balance_2 = self.__cur_height(t.right) - self.__cur_height(t.left)
        if cur_balance_2 == -3: # Rotate left heavy tree to the right.
          t = self.__rotate_right(t)
      elif cur_balance == -2 and self.__child_balance(t.left) == 0: # Rotate left heavy tree to the right.
        t = self.__rotate_right(t) 
      # Single right cases
      elif cur_balance == 2 and self.__child_balance(t.right) == 1: # Rotate the right heavy tree to the left.
        t = self.__rotate_left(t) 
        cur_balance_2 = self.__cur_height(t.right) - self.__cur_height(t.left)
        if cur_balance_2 == 3: # Rotate the right heavy tree to the left.
          self.__rotate_left(t)
      elif cur_balance == 2 and self.__child_balance(t.right) == 0: # Rotate the right heavy tree to the left.
        t = self.__rotate_left(t)
      # Left-right case
      elif cur_balance == -2 and self.__child_balance(t.left) == 1: # Double rotation case
        t.left = self.__rotate_left(t.left) # Rotate t's left child left
        t = self.__rotate_right(t) # Rotate t to the right
      # Right-left case
      elif cur_balance == 2 and self.__child_balance(t.right) == -1:
        t.right = self.__rotate_right(t.right) # Rotate t's right child right
        t = self.__rotate_left(t) # Rotate t to the left
      self.__cur_height(t) # Calcuate the height of t
      return t

  # Returns the current balance of the binary search tree.
  def __child_balance(self, child_root):
    cur_balance = self.__cur_height(child_root.right) - self.__cur_height(child_root.left)
    return cur_balance

  # Rotates the binary search tree to the right to keep it balanced.
  def __rotate_right(self, subroot):
    old_subroot = subroot # Save current subroot
    floater = subroot.left.right # Save the floater(s)/inner child(ren)
    subroot = subroot.left # Set the left child of the current subroot as the new subroot
    old_subroot.left = floater # Move the floater to the old subroot's left child
    subroot.right = old_subroot # Set the new subroot's right child as the old subroot
    subroot.right.__height = self.__cur_height(subroot.right) # Recalculate the height of the right child(ren)
    return subroot

  # Rotates the binary search tree to the left to keep it balanced.
  def __rotate_left(self, subroot):
    old_subroot = subroot # Save current subroot
    floater = subroot.right.left # Save the floater(s)/inner child(ren)
    subroot = subroot.right # Set the right child of the current subroot as the new subroot
    old_subroot.right = floater # Move the floater to the old subroot's right child
    subroot.left = old_subroot # Set the new subroot's left child as the old subroot
    subroot.left.__height = self.__cur_height(subroot.left) # Recalculate the height of the left child(ren)
    return subroot

  # Returns an in-order list representation of the binary search tree.
  def to_list(self):
    final_list = []
    self.__rlist(self.__root, final_list)
    return final_list

  # Private recursive function which helps return an in-order list representation of the binary search tree.
  def __rlist(self, subroot, final_list):
    if subroot is None: 
      return 
    else:
      self.__rlist(subroot.left, final_list)
      final_list.append(subroot.value)
      self.__rlist(subroot.right, final_list)
      return
    
  # Returns an in-order string representation of the binary search tree.
  def __str__(self):
    return self.in_order()

from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
    
  # Note: The functions below were written assuming the head position is the front and the tail position is the back.

  # Adds value to the front of the deque.
  def push_front(self, val):
    if len(self.__list) == 0:
      self.__list.append_element(val)
    else:
      self.__list.insert_element_at(val,0)
  
  # Removes the value at the front of the deque.
  def pop_front(self):
    if len(self.__list) == 0:
      return None
    return self.__list.remove_element_at(0)

  # Returns value at the front of the deque.
  def peek_front(self):
    if len(self.__list) == 0:
      return None
    return self.__list.get_element_at(0)

  # Adds a value to the back of the deque.
  def push_back(self, val):
      self.__list.append_element(val)
  
  # Removes the value at the back of the deque.
  def pop_back(self):
    if len(self.__list) == 0:
      return None
    return self.__list.remove_element_at(len(self.__list)-1)

  # Returns value at the front of the deque.
  def peek_back(self):
    if len(self.__list) == 0:
      return None
    return self.__list.get_element_at(len(self.__list)-1)    

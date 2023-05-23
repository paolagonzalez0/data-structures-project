from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # Capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__front = 0
    self.__back = 0
    self.__size = 0
  
  # Returns string representation of the array deque.
  def __str__(self):
    # Note: String is oriented from front (left) to back (right).
    if self.__size == 0:
      return "[ ]"
    else:
      final = ""
      front_bracket = "[ "
      x = self.__front
      for i in range(self.__size -1):
        final += str(self.__contents[x])
        final += ", "
        x = (x+1) % self.__capacity
      final += str(self.__contents[x]) + " ]"
      final_str = front_bracket + final
      return final_str

  # Returns length of array deque.
  def __len__(self):
    return self.__size

  # This function doubles the capacity and positions existing items in the deque starting in cell 0.
  def __grow(self):
    old = self.__contents
    new = [None] * (self.__capacity * 2)
    cur_walk = self.__front
    for i in range(self.__capacity):
      new[i] = old[cur_walk]
      cur_walk = (cur_walk + 1) % self.__capacity
    self.__contents = new
    self.__front = 0
    self.__back = self.__capacity - 1 
    self.__capacity = self.__capacity * 2

  # Adds value to the front of the deque.
  def push_front(self, val):
    if self.__size == self.__capacity:
      self.__grow()
    self.__front = (self.__front - 1) % self.__capacity
    self.__contents[self.__front] = val
    self.__size += 1
  
  # Removes the value at the front of the deque.
  def pop_front(self):
    if self.__size == 0:
      return None
    popped_val = self.__contents[self.__front]
    self.__front = (self.__front + 1) % self.__capacity
    self.__size -= 1
    return popped_val

  # Returns value at the front of the deque.
  def peek_front(self):
    if self.__size == 0:
      return None
    return self.__contents[self.__front]
  
  # Adds a value to the back of the deque.
  def push_back(self, val):
    if self.__size == self.__capacity:
      self.__grow()
    self.__back = (self.__back + 1) % self.__capacity
    self.__contents[self.__back] = val
    self.__size += 1

  # Removes the value at the back of the deque.
  def pop_back(self):
    if self.__size == 0:
      return None
    popped_val = self.__contents[self.__back]
    self.__back = (self.__back - 1) % self.__capacity
    self.__size -= 1
    return popped_val

  # Returns value at the front of the deque.
  def peek_back(self):
    if self.__size == 0:
      return None
    return self.__contents[self.__back]

import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_
  
  #Empty Deque testing
  def test_empty_deque(self):
    # Testing string, len, pop, and peek functions
    self.assertEqual("[ ]", str(self.__deque)) # Use example in write up #1
    self.assertEqual(0,len(self.__deque)) # Use example in write up #1
    self.assertEqual(None,self.__deque.pop_front())
    self.assertEqual("[ ]", str(self.__deque))
    self.assertEqual(None,self.__deque.pop_back())
    self.assertEqual("[ ]", str(self.__deque))
    self.assertEqual(None,self.__deque.peek_front())
    self.assertEqual(None,self.__deque.peek_back())
  #One value testing
  def test_one_value_push_front(self):
    self.__deque.push_front(7)
    self.assertEqual(1, len(self.__deque))
    self.assertEqual("[ 7 ]",str(self.__deque))

  def test_one_value_peek_front(self):
    self.__deque.push_front(7)
    self.assertEqual(7,self.__deque.peek_front())
    # Note: The deque does not change because of peeking.
    self.assertEqual("[ 7 ]",str(self.__deque))
    self.assertEqual(1, len(self.__deque))

  def test_one_value_pop_front(self):
    self.__deque.push_front(7)
    self.assertEqual(1, len(self.__deque)) # Use example in write up #1
    self.assertEqual("[ 7 ]",str(self.__deque))
    self.assertEqual(7,self.__deque.pop_front())
    self.assertEqual(0, len(self.__deque)) # Use example in write up #1
    self.assertEqual("[ ]",str(self.__deque))

  def test_one_value_push_back(self):
    self.__deque.push_back([3, 4])
    self.assertEqual(1, len(self.__deque))
    self.assertEqual("[ [3, 4] ]",str(self.__deque))

  def test_one_value_peek_back(self):
    self.__deque.push_back([3, 4])
    self.assertEqual([3, 4],self.__deque.peek_back())
    self.assertEqual(1, len(self.__deque))
    # Note: The deque does not change because of peeking.
    self.assertEqual("[ [3, 4] ]",str(self.__deque))

  def test_one_value_pop_back(self):
    self.__deque.push_back([3, 4])
    self.assertEqual([3, 4], self.__deque.pop_back())
    self.assertEqual(0, len(self.__deque))
    self.assertEqual("[ ]",str(self.__deque))

  # One None value testing
  def test_one_none_value_push_front(self):
    self.__deque.push_front(None)
    self.assertEqual(1, len(self.__deque)) # Use example in write up #1
    self.assertEqual("[ None ]",str(self.__deque)) # Use example in write up #1

  def test_one_none_value_peek_front(self):
    self.__deque.push_front(None)
    self.assertEqual(None,self.__deque.peek_front())
    # Note: The deque does not change because of peeking.
    self.assertEqual("[ None ]",str(self.__deque))
    self.assertEqual(1, len(self.__deque))
  
  def test_one_none_value_pop_front(self):
    self.__deque.push_front(None)
    self.assertEqual(None,self.__deque.pop_front())
    self.assertEqual(0, len(self.__deque)) # Use example in write up #1
    self.assertEqual("[ ]",str(self.__deque))

  def test_one_none_value_push_back(self):
    self.__deque.push_back(None)
    self.assertEqual(1, len(self.__deque))
    self.assertEqual("[ None ]",str(self.__deque))

  def test_one_none_value_peek_back(self):
    self.__deque.push_back(None)
    self.assertEqual(None,self.__deque.peek_back())
    self.assertEqual(1, len(self.__deque))
    # Note: The deque does not change because of peeking.
    self.assertEqual("[ None ]",str(self.__deque))

  def test_one_none_value_pop_back(self):
    self.__deque.push_back(None)
    self.assertEqual(None, self.__deque.pop_back())
    self.assertEqual(0, len(self.__deque))
    self.assertEqual("[ ]",str(self.__deque))

  #Two value testing
  def test_two_values_push_front(self):
    self.__deque.push_front("Structures")
    # Appending "Data" shows the grow function has increased by size.
    # If we still had a capacity of 1, then "Data" would not be pushed 
    # onto the Deque and the following assertion would fail.
    self.__deque.push_front("Data")
    self.assertEqual("[ Data, Structures ]",str(self.__deque))
    self.assertEqual(2, len(self.__deque))

  def test_two_values_peek_front(self):
    self.__deque.push_front("Structures")
    self.__deque.push_front("Data")
    self.assertEqual("Data",self.__deque.peek_front())
    # Note: The deque does not change because we peek at values.
    self.assertEqual("[ Data, Structures ]",str(self.__deque))

  def test_two_values_pop_front(self):
    self.__deque.push_front("Structures")
    self.__deque.push_front("Data")
    self.assertEqual("Data", self.__deque.pop_front())
    self.assertEqual("[ Structures ]",str(self.__deque))
    self.assertEqual(1, len(self.__deque)) 

  def test_two_values_push_back(self):
    self.__deque.push_back("Data")
    # Appending "Structures" shows the grow function has increased by size.
    # If we still had a capacity of 1, then "Structures" would not be pushed 
    # onto the Deque and the following assertion would fail.
    self.__deque.push_back("Structures")
    self.assertEqual("[ Data, Structures ]",str(self.__deque))
    self.assertEqual(2, len(self.__deque))

  def test_two_values_peek_back(self):
    self.__deque.push_back("Data")
    self.__deque.push_back("Structures")
    self.assertEqual("Structures",self.__deque.peek_back())
    # Note: The deque does not change because we peek at values.
    self.assertEqual("[ Data, Structures ]",str(self.__deque))

  def test_two_values_pop_back(self):
    self.__deque.push_back("Data")
    self.__deque.push_back("Structures")
    self.assertEqual("Structures", self.__deque.pop_back())
    self.assertEqual("[ Data ]",str(self.__deque))
    self.assertEqual(1, len(self.__deque))   

  #Three Value Testing
  def test_three_values_push_front(self):
    self.__deque.push_front(55)    
    self.__deque.push_front(44)
    self.__deque.push_front(33)
    self.assertEqual("[ 33, 44, 55 ]",str(self.__deque))
    self.assertEqual(3, len(self.__deque))
  
  def test_three_values_peek_front(self):
    self.__deque.push_front(55)    
    self.__deque.push_front(44)
    self.__deque.push_front(33)
    self.assertEqual(33,self.__deque.peek_front())
    self.assertEqual("[ 33, 44, 55 ]",str(self.__deque))

  def test_three_values_pop_front(self):
    self.__deque.push_front(55)    
    self.__deque.push_front(44)
    self.__deque.push_front(33)
    self.assertEqual(33, self.__deque.pop_front()) 
    self.assertEqual("[ 44, 55 ]",str(self.__deque))
    self.assertEqual(2, len(self.__deque))

  def test_three_values_push_back(self):
    self.__deque.push_back(33)    
    self.__deque.push_back(44)
    self.__deque.push_back(55)
    self.assertEqual("[ 33, 44, 55 ]",str(self.__deque))
    self.assertEqual(3, len(self.__deque))

  def test_three_values_peek_back(self):
    self.__deque.push_back(33)    
    self.__deque.push_back(44)
    self.__deque.push_back(55)
    self.assertEqual(55,self.__deque.peek_back())
    # Note: The deque does not change because we peek at values.
    self.assertEqual("[ 33, 44, 55 ]",str(self.__deque))

  def test_three_values_pop_back(self):
    self.__deque.push_back(33)    
    self.__deque.push_back(44)
    self.__deque.push_back(55)
    self.assertEqual(55, self.__deque.pop_back())
    self.assertEqual("[ 33, 44 ]",str(self.__deque))
    self.assertEqual(2, len(self.__deque))

# Three None value testing
  def test_three_none_values_push_front(self):
    self.__deque.push_front(None)    
    self.__deque.push_front(None)
    self.__deque.push_front(None)
    self.assertEqual("[ None, None, None ]",str(self.__deque))
    self.assertEqual(3, len(self.__deque))
  
  def test_three_none_values_peek_front(self):
    self.__deque.push_front(None)    
    self.__deque.push_front(None)
    self.__deque.push_front(None)
    self.assertEqual(None,self.__deque.peek_front())
    self.assertEqual("[ None, None, None ]",str(self.__deque))

  def test_three_none_values_pop_front(self):
    self.__deque.push_front(None)    
    self.__deque.push_front(None)
    self.__deque.push_front(None)
    self.assertEqual(None, self.__deque.pop_front())
    self.assertEqual("[ None, None ]",str(self.__deque))
    self.assertEqual(2, len(self.__deque))

  def test_three_none_values_push_back(self):
    self.__deque.push_back(None)    
    self.__deque.push_back(None)
    self.__deque.push_back(None)
    self.assertEqual("[ None, None, None ]",str(self.__deque))
    self.assertEqual(3, len(self.__deque))

  def test_three_none_values_peek_back(self):
    self.__deque.push_back(None)    
    self.__deque.push_back(None)
    self.__deque.push_back(None)
    self.assertEqual(None,self.__deque.peek_back())
    # Note: The deque does not change because we peek at values.
    self.assertEqual("[ None, None, None ]",str(self.__deque))

  def test_three_none_values_pop_back(self):
    self.__deque.push_back(None)    
    self.__deque.push_back(None)
    self.__deque.push_back(None)
    self.assertEqual(None, self.__deque.pop_back())
    self.assertEqual("[ None, None ]",str(self.__deque))
    self.assertEqual(2, len(self.__deque))

  def test_push_peek_pop_random_deque_case(self):
    self.__deque.push_front("Data")
    self.__deque.push_back("Structures")
    self.__deque.push_front([2, 4, 1])
    self.assertEqual([2, 4, 1], self.__deque.peek_front())
    self.assertEqual("Structures", self.__deque.peek_back())
    self.__deque.push_back("!")
    self.__deque.push_front("CSCI")
    self.assertEqual("[ CSCI, [2, 4, 1], Data, Structures, ! ]", str(self.__deque))
    self.assertEqual(5, len(self.__deque))
    self.__deque.push_back(2022)
    self.assertEqual("[ CSCI, [2, 4, 1], Data, Structures, !, 2022 ]", str(self.__deque))
    self.assertEqual(6, len(self.__deque))
    self.assertEqual("CSCI", self.__deque.pop_front())
    self.assertEqual([2, 4, 1], self.__deque.pop_front())
    self.assertEqual(2022, self.__deque.pop_back())
    self.assertEqual("!", self.__deque.pop_back())  
    self.assertEqual("[ Data, Structures ]", str(self.__deque))

  # Stack testing

  # Empty Stack
  def test_empty_stack(self):
    self.assertEqual("[ ]", str(self.__stack))
    self.assertEqual(0, len(self.__stack))
    self.assertEqual(None, self.__stack.peek())
    self.assertEqual(None, self.__stack.pop())
    self.assertEqual(0, len(self.__stack))
    self.assertEqual("[ ]", str(self.__stack))

  # One value testing
  def test_one_value_stack_push(self):
    self.__stack.push(5)
    self.assertEqual("[ 5 ]", str(self.__stack))
    self.assertEqual(1, len(self.__stack))   

  def test_one_value_stack_peek(self):
    self.__stack.push("Data")
    self.assertEqual("[ Data ]", str(self.__stack))
    self.assertEqual(1, len(self.__stack))
    self.assertEqual("Data", self.__stack.peek()) 
    # Note: The stack does not change because we peek at values.
    self.assertEqual("[ Data ]", str(self.__stack))
  
  def test_one_value_stack_pop(self):
    self.__stack.push([2, 4, 1])
    self.assertEqual("[ [2, 4, 1] ]", str(self.__stack))
    self.assertEqual(1, len(self.__stack))
    self.assertEqual([2, 4, 1], self.__stack.pop())
    self.assertEqual("[ ]", str(self.__stack))
    self.assertEqual(0, len(self.__stack)) 

  # Two value testing
  def test_two_values_stack_push(self):
    self.__stack.push(-22)
    self.__stack.push(None)
    self.assertEqual("[ None, -22 ]", str(self.__stack))
    self.assertEqual(2, len(self.__stack))

  def test_two_values_stack_peek(self):
    self.__stack.push(-22)
    self.__stack.push(None)
    self.assertEqual(None, self.__stack.peek()) 
    # Note: The stack does not change because we peek at values.
    self.assertEqual("[ None, -22 ]", str(self.__stack))
    self.assertEqual(2, len(self.__stack))

  def test_two_values_stack_pop(self):
    self.__stack.push("Data Structures")
    self.__stack.push("[")
    self.assertEqual("[ [, Data Structures ]", str(self.__stack))
    self.assertEqual(2, len(self.__stack)) 
    self.assertEqual("[", self.__stack.pop())
    self.assertEqual("[ Data Structures ]", str(self.__stack))
    self.assertEqual(1, len(self.__stack)) 

  # None value testing
  def test_three_none_values_stack(self):
    self.__stack.push(None)
    self.__stack.push(None)
    self.__stack.push(None)
    self.assertEqual("[ None, None, None ]", str(self.__stack))
    self.assertEqual(3, len(self.__stack)) 
    self.assertEqual(None, self.__stack.pop())
    self.assertEqual(None, self.__stack.pop())
    self.assertEqual(None, self.__stack.pop())
    self.assertEqual("[ ]", str(self.__stack))
    self.assertEqual(0, len(self.__stack)) 

  # Random value testing
  def test_push_peek_pop_random_stack_case(self):
    self.__stack.push(-17)
    self.__stack.push([2, 4, 1])
    self.__stack.push(None)
    self.__stack.push("Data Structures")
    self.assertEqual("[ Data Structures, None, [2, 4, 1], -17 ]", str(self.__stack))
    self.assertEqual(4, len(self.__stack)) 
    self.assertEqual("Data Structures", self.__stack.peek()) 
    self.assertEqual("Data Structures", self.__stack.pop())
    self.assertEqual(None, self.__stack.pop())
    self.assertEqual([2, 4, 1], self.__stack.peek()) 
    self.assertEqual(2, len(self.__stack)) 
    self.assertEqual("[ [2, 4, 1], -17 ]", str(self.__stack))
    self.assertEqual([2, 4, 1], self.__stack.pop())
    self.assertEqual(-17, self.__stack.pop())
    self.assertEqual("[ ]", str(self.__stack))
    self.assertEqual(0, len(self.__stack))

  # Queue Testing

  # Empty Queue Testing
  def test_empty_queue(self):
    self.assertEqual("[ ]", str(self.__queue))
    self.assertEqual(0, len(self.__queue))
    self.assertEqual(None, self.__queue.peek())
    self.assertEqual(None, self.__queue.dequeue())

  # One Value Testing
  def test_one_value_enqueue_queue(self):
    self.__queue.enqueue(-1)
    self.assertEqual("[ -1 ]", str(self.__queue))
    self.assertEqual(1, len(self.__queue))

  def test_one_value_peek_queue(self):
    self.__queue.enqueue(None)
    self.assertEqual(None, self.__queue.peek())
    # Note: The queue does not change because we peek at values.
    self.assertEqual("[ None ]", str(self.__queue))
    self.assertEqual(1, len(self.__queue))

  def test_one_value_dequeue_queue(self):
    self.__queue.enqueue("Data")
    self.assertEqual("[ Data ]", str(self.__queue))
    self.assertEqual(1, len(self.__queue))
    self.assertEqual("Data", str(self.__queue.dequeue()))
    self.assertEqual("[ ]", str(self.__queue))
    self.assertEqual(0, len(self.__queue))

  # Two Value Testing
  def test_two_values_enqueue_queue(self):
    self.__queue.enqueue("CSCI")
    self.__queue.enqueue([2, 4, 1])
    self.assertEqual("[ CSCI, [2, 4, 1] ]", str(self.__queue))
    self.assertEqual(2, len(self.__queue))

  def test_two_values_peek_queue(self):
    self.__queue.enqueue(None)
    self.__queue.enqueue("Data Structures")
    self.assertEqual(None, self.__queue.peek())
    # Note: The queue does not change because we peek at values.
    self.assertEqual("[ None, Data Structures ]", str(self.__queue))
    self.assertEqual(2, len(self.__queue))

  def test_two_values_dequeue_queue(self):
    self.__queue.enqueue("Data")
    self.__queue.enqueue("Structures")
    self.assertEqual("[ Data, Structures ]", str(self.__queue))
    self.assertEqual(2, len(self.__queue))
    self.assertEqual("Data", str(self.__queue.dequeue()))
    self.assertEqual("[ Structures ]", str(self.__queue))
    self.assertEqual("Structures", str(self.__queue.dequeue()))
    self.assertEqual("[ ]", str(self.__queue))
    self.assertEqual(0, len(self.__queue))

  def test_three_none_values_enqueue_queue(self):
    self.__queue.enqueue(None)
    self.__queue.enqueue(None)
    self.__queue.enqueue(None)
    self.assertEqual("[ None, None, None ]", str(self.__queue))
    self.assertEqual(3, len(self.__queue)) 

  def test_three_none_values_peek_queue(self):
    self.__queue.enqueue(None)
    self.__queue.enqueue(None)
    self.__queue.enqueue(None)
    self.assertEqual("[ None, None, None ]", str(self.__queue))
    self.assertEqual(None, self.__queue.peek())
    # Note: The queue does not change because we peek at values.
    self.assertEqual("[ None, None, None ]", str(self.__queue))
    
  def test_three_none_values_pop_queue(self):
    self.__queue.enqueue(None)
    self.__queue.enqueue(None)
    self.__queue.enqueue(None)
    self.assertEqual("[ None, None, None ]", str(self.__queue))
    self.assertEqual(None, self.__queue.dequeue())
    self.assertEqual(None, self.__queue.dequeue())
    self.assertEqual(None, self.__queue.dequeue())
    self.assertEqual("[ ]", str(self.__queue))
    self.assertEqual(0, len(self.__queue)) 

  # Random Value testing:
  def test_enqueue_peek_dequeue_random_queue_case(self):
    self.__queue.enqueue("Data")
    self.__queue.enqueue(-22)
    self.assertEqual("Data", self.__queue.dequeue())
    self.__queue.enqueue("Structures")
    self.assertEqual(-22, self.__queue.peek())
    self.__queue.enqueue([2, 4, 1])
    self.assertEqual("[ -22, Structures, [2, 4, 1] ]", str(self.__queue))
    self.assertEqual(3, len(self.__queue)) 
    self.assertEqual(-22, self.__queue.dequeue())
    self.assertEqual("[ Structures, [2, 4, 1] ]", str(self.__queue))
    self.assertEqual(2, len(self.__queue)) 


if __name__ == '__main__':
  unittest.main()

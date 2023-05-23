class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the Node class.
            self.val = val
            self.next = None
            self.prev = None


    def __init__(self): # O(1)
        # Declare and initialize the private attributes for objects of the sentineled Linked_List class
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__size = 0


    def __len__(self): # O(1)
        # Return the number of value-containing nodes in this list. 
        return self.__size


    def append_element(self, val): # O(1)
        """Increase the size of the list by one, and add a node containing val at
        the new tail position. this is the only way to add items at the tail
        position."""
        newest = Linked_List.__Node(val)
        if self.__size == 0:
            newest.next = self.__trailer
            newest.prev = self.__header
            self.__header.next = newest
        else:
            newest.next = self.__trailer
            newest.prev = self.__trailer.prev
            newest.prev.next = newest
        self.__trailer.prev = newest
        self.__size += 1

    # Additional Functions

    def __check_index(self, index): # O(1)
         if index >= self.__size or index < 0:
           raise IndexError    

    def __cur_walk(self, index): # O(n)
        cur = self.__header.next
        for i in range(1,index):
            cur = cur.next
        return cur 


    def insert_element_at(self, val, index): # O(n)
        """Assuming the head position (not the header node) is indexed 0, add a
        node containing val at the specified index. If the index is not a
        valid position within the list, raise an IndexError exception. This
        method cannot be used to add an item at the tail position.""" 
        newest = Linked_List.__Node(val)
        self.__check_index(index)
        if index == 0:
            newest.prev = self.__header
            newest.next = self.__header.next
            self.__header.next.prev = newest
            self.__header.next = newest
        else:
            cur = self.__cur_walk(index)
            newest.next = cur.next
            newest.prev = cur
            cur.next.prev = newest
            cur.next = newest
        self.__size += 1


    def remove_element_at(self, index): # O(n)
        """Assuming the head position (not the header node) is indexed 0, remove
        and return the value stored in the node at the specified index. If the
        index is invalid, raise an IndexError exception."""
        self.__check_index(index)
        removed_val = self.get_element_at(index)
        if index == 0:
            self.__header.next = self.__header.next.next
            self.__header.next.prev = self.__header
        else:
            cur = self.__cur_walk(index)
            cur.next = cur.next.next
            cur.next.prev = cur
        self.__size -= 1
        return removed_val


    def get_element_at(self, index): # O(n)
        """Assuming the head position (not the header node) is indexed 0, return
        the value stored in the node at the specified index, but do not unlink
        it from the list. If the specified index is invalid, raise an
        IndexError exception."""
        self.__check_index(index)
        if index == 0:
            return self.__header.next.val
        else:
            cur = self.__cur_walk(index)
            return cur.next.val


    def rotate_left(self): # O(1)
        """Rotate the list left one position. Conceptual indices should all
        decrease by one, except for the head, which should become the tail.
        For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        must not return a value."""
        if self.__size == 0:
           return
        else:
            self.__header.next.prev = self.__trailer.prev
            self.__trailer.prev.next = self.__header.next
            self.__trailer.prev = self.__header.next
            self.__header.next.next.prev = self.__header
            self.__header.next = self.__header.next.next
            self.__trailer.prev.next = self.__trailer


    def __str__(self): # O(n)
        """ Return a string representation of the list's contents. An empty list
        should appear as [ ]. A list with one element should appear as [ 5 ].
        A list with two elements should appear as [ 5, 7 ]. You may assume
        that the values stored inside of the node objects implement the
        __str__() method, so you call str(val_object) on them to get their
        string representations."""

        if self.__size == 0:
            return '[ ]' 
        else:
            final_str = '[ '
            cur = self.__header.next 
            while cur is not self.__trailer:
                final_str += str(cur.val)
                if cur.next is self.__trailer:
                    final_str += ' ]'
                else:
                    final_str += ', '
                cur = cur.next
            return final_str



    def __iter__(self): # O(1)
        # Initialize a new attribute for walking through your list. Do not modify the return statement.

        # Next line added to check for initialization in testing.
        print("iter function was called and iter_index was initialized to 0.\n")
        self.__iter_index = 0
        self.__current = self.__header
        return self


    def __next__(self): #O(1)
        """ Using the attribute that you initialized in __iter__(), fetch the next
        value and return it. If there are no more values to fetch, raise a
        StopIteration exception."""

        # Next line added to keep track of iter_index during for loop testing.
        print("next function called while iter_index is " + str(self.__iter_index))

        if self.__iter_index == self.__size:
            raise StopIteration
        self.__current = self.__current.next
        self.__iter_index += 1
        return self.__current.val


    def __reversed__(self): # O(n)
        """ Construct and return a new Linked_List object whose nodes alias the
        same objects as the nodes in this list, but in reverse order. For a
        Linked_List object ll, Python will automatically call this function
        when it encounters a call to reversed(ll) in an application. If
        print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        the object on which it is called. Calling print(ll) again will still
        display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        method must operate in linear time. """
        rev_ll = Linked_List()
        cur_node = self.__trailer.prev
        while rev_ll.__size != self.__size:
            rev_ll.append_element(cur_node.val)
            cur_node = cur_node.prev
        return rev_ll


if __name__ == '__main__':
    # Note: For the first half of this project, the directions instructed us to write multiple test cases under this section, rather than using unit testing. In the second half of the project, we implemented unit testing.
    ll = Linked_List()

    # Testing functions on an empty list
    print('\n')
    print("Empty list function testing:\n")
    try:
        print("Empty list: " + str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        # Next line should fail inserting an element to empty list. Must use append_element function instead.
        ll.insert_element_at("fail",0)
    except IndexError:
        print("Error: Cannot insert value at given index. The linked list is empty." )
        print("Correctly recognized empty list.")
    print('')
    try:
        # Next line should fail because there are no elements in the list.
            ll.remove_element_at(0)
    except IndexError:
        print("Error: Cannot remove value at given index. The linked list is empty." )
        print("Correctly recognized empty list.")
    print('')
    try:
        # Next line should fail because there are no elements in the list.
            ll.get_element_at(0)
    except IndexError:
        print("Error: Cannot obtain value at given index. The linked list is empty." )
        print("Correctly recognized empty list.")
    print('')
        # Next line should not do anything because there are no elements in the list.
    ll.rotate_left()
    print("rotate_left function called.")
    print(str(ll))
    print('')
    # Next line should not iterate because there are no elements in the list.
    for val in ll:
        print(val)
    print("Cannot iterate through an empty list.")
    print('')
    # Next line should return a new empty list Linked_list object.
    print("Reversed linked list will look the same as original linked list.")
    print("Reversed Linked_List: " + str(reversed(ll)))
    print("Original Linked_List: " + str(ll))
    print('')
    print("After trying all invalid functions, list str and length should remain unchanged:")
    print(str(ll))
    print("The linked list contains " + str(len(ll)) + " elements.")
    print('')
    print('-----------------------------')
    print('')


    ## Testing linked list with one value
    print("Testing functions on a linked list with one value:\n")
    try:
        ll.append_element(123)
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        ll.rotate_left()
        print("rotate_left function called.")
        print(str(ll))
        print("This is the list with one value when reversed:")
        print(reversed(ll))
        ll.remove_element_at(0)
        #After applying remove_element_at(), list should be empty.
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
    except IndexError:
        print("Error: Index value out of bounds.")
        print("Correctly caught invalid indexing.")
    print('')
    print('-----------------------------')
    print('')


    ## append_element function testing
    print('append_element function testing:\n')
    try:
        ll.append_element("hello")
        ll.append_element(3)
        ll.append_element([1,2,3])
        ll.append_element(False)        
        ll.append_element("%")
        ll.append_element((2,4,6))
        ll.append_element(None)
        ll.append_element(0)
        ll.append_element(-222)
        ll.append_element(True)
        # Linked list should contain 10 elements.
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        print('-----------------------------')
        print('')


    ## insert_element_at function testing
        print("insert_element_at function testing:\n")
        # Inserting different value types
        ll.insert_element_at(97,0)
        ll.insert_element_at('no',1)
        ll.insert_element_at(None, 2)
        ll.insert_element_at(-55,7)
        ll.insert_element_at(['red','yellow'],9)
        ll.insert_element_at(('fall','winter'),14)
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        # Next line should insert 'yes' as the second to last node/value in the list.
        ll.insert_element_at('yes',15) 
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        # Next line should fail because this function should not be used to add a value 
        # at the tail position.
        ll.insert_element_at('fail',17)
        # Next two lines should not print because line above returned an error.
    except IndexError:
        print("Error: Index value out of bounds. Cannot add a value at the tail position.")
        print("Correctly caught invalid indexing.")
    print('')
    try:
        # Next line should raise an IndexError because negative indexing is invalid.
        ll.insert_element_at('fail',-1)
    except IndexError:
        print("Error: Index value out of bounds. Negative indexing not accepted.")
        print("Correctly caught invalid indexing.")
    print('')
    try:
        # Next line should fail because the index too large and out of bounds.
        ll.insert_element_at('fail',500)
    except IndexError:
        print("Error: Index value out of bounds. Too large.")
        print("Correctly caught invalid indexing.")
    print('')
    print("After testing invalid indices the list is left unchanged:")
    print(str(ll))
    print("The linked list contains " + str(len(ll)) + " elements.")
    print('')
    print('-----------------------------')
    print('')


    ## remove_element_at function testing
    print('remove_element_at function testing:\n')

    print("We begin with our current list:\n" + str(ll))
    print("The linked list contains " + str(len(ll)) + " elements.")
    print('')
    try:
        # Removing different value types.
        print(ll.remove_element_at(0))
        print("Removed value at index 0.")
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        print(ll.remove_element_at(1))
        print("Removed value at index 1.")
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        print(ll.remove_element_at(1))
        print("Removed value at index 1.")
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        print(ll.remove_element_at(3))
        print("Removed value at index 3.")
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        print(ll.remove_element_at(3))
        print("Removed value at index 3.")
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        print(ll.remove_element_at(2))
        print("Removed value at index 2.")
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        print(ll.remove_element_at(8))
        print("Removed value at index 8.")
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        # Next line should raise an IndexError because index is too large and out of bounds.
        print(ll.remove_element_at(10))  
    except IndexError:
        print("Error: Index value out of bounds. Too large.")
        print("Correctly caught invalid indexing.")
    print('')
    try:
        # Next line should fail because we do not accept negative indexing.
        ll.remove_element_at(-2)
    except IndexError:
        print("Error: Index value out of bounds. Negative indexing not accepted.")
        print("Correctly caught invalid indexing.")
    print('')
    print("After testing invalid indices the list is left unchanged:")
    print(str(ll))
    print("The linked list contains " + str(len(ll)) + " elements.")
    print('')
    print('-----------------------------')
    print('')


    ## get_element_at function testing
    print("get_element_at function testing:\n")
    try:
        # Returning elements at random indices.
        print("The element at index 0 is " + str(ll.get_element_at(0)) + ".")
        print("The element at index 1 is " + str(ll.get_element_at(1)) + ".")
        print("The element at index 3 is " + str(ll.get_element_at(3)) + ".")
        print("The element at index 5 is " + str(ll.get_element_at(5)) + ".")
        print("The element at index 9 is " + str(ll.get_element_at(9)) + ".")
        print('')
        print("The list should remain unchanged after returning values:")
        print(str(ll))
        print("The linked list contains " + str(len(ll)) + " elements.")
        print('')
        # Next line should raise an IndexError because index is too large and out of bounds.
        print(ll.get_element_at(10))
    except IndexError:
        print("Error: Index value out of bounds. Too large.")
        print("Correctly caught invalid indexing.")
    print('')
    try:
        # Next line should raise an IndexError because negative indexing is invalid.
        print(ll.get_element_at(-3))
    except IndexError:
        print("Error: Index value out of bounds. Negative indexing not accepted.")
        print("Correctly caught invalid indexing.")
    print('')
    print("After testing invalid indices, list remains unchanged:")
    print(str(ll))
    print("The linked list contains " + str(len(ll)) + " elements.")
    print('')
    print('-----------------------------')
    print('')


    ## rotate_left function testing
    print("rotate_left function testing:\n")
    print("Original list: " + str(ll))
    ll.rotate_left()
    print("rotate_left function called.")
    # Next line rotates list left once.
    print("Updated list: " + str(ll))
    print('')
    # get_element_at(0) should now return 3.
    print("The value at index 0 is now " + str(ll.get_element_at(0)) + ".")
    # get_element_at(9) should now return "no".
    print("The value at index 9 is now " + str(ll.get_element_at(9)) + ".")
    print('')
    # Next two lines rotate the updated list left two more times.
    ll.rotate_left()
    print("rotate_left function called.")
    ll.rotate_left()
    print("rotate_left function called.")
    print("Updated list: " + str(ll))
    print('')
    # The length of the list remains unchanged.
    print("The linked list contains " + str(len(ll)) + " elements.")
    print('')
    print('-----------------------------')
    print('')


    ## __iter__ and __next__ function testing
    print("__iter__ and __next__ function testing:\n")
    print("Current list: " + str(ll))
    print("Current length: " + str(len(ll)))
    print('')
    # For loop should print each value in the linked list.
    for val in ll:
        print(val)
    print('')
    print('-----------------------------')
    print('')


    ## reversed function testing
    print("reversed function testing:\n")
    print("Original Linked List: \n" + str(ll))
    print("Reversed Linked List: \n" + str(reversed(ll)))
    # Linked list remains unmodified.
    print("Original Linked List after reversed function: \n" + str(ll))
    print("The linked list contains " + str(len(ll)) + " elements.")
    print('')

    # Reversed for loop
    print("Reversed Linked List: " + str(reversed(ll)))
    print("Reversed list length: " + str(len(ll)))

    print('')
    for val in reversed(ll):
        print(val)
    print('\n')

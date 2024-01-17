class Node():

  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
    """
    - Creates a LinkedList
    - Head property will point to the first node in list
    - Multiple nodes can be inserted

    Parameters:
    - None

    Return:
    - Returns True when a value is found that exists
    - Returns false when a value is not found
    - Returns a collection of all values that exist
    """

    def __init__(self):
        # initialization here
        self.head = None

    def __str__(self):
        # Returns: a string representing all the values in the Linked List:
        result = []
        current_node = self.head
        string = ''
        while current_node:
            string += f"{{ {current_node.value} }} -> "
            current_node = current_node.next
        string += "NULL"
        return string
    
    def insert(self,value):
        # 
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
    
    def append(self, value):
        current_node = self.head
        while current_node.next:
           current_node = current_node.next
        current_node.next = Node(value)

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        current_node = self.head

        if self.head is None:
            raise TargetError("List is empty")

        if current_node.value == value:
            new_node.next = self.head
            self.head = new_node
            return self.__str__()
        
        while current_node.next:
            if current_node.next.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return self.__str__()
            current_node = current_node.next
        raise TargetError("Value not found")
        # return self.__str__()
    
    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        current_node = self.head         

        if self.head is None:
            raise TargetError("List is empty")
        
        while current_node.next:
            if current_node.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return self.__str__()
            current_node = current_node.next
        raise TargetError("Value not found")
        # return self.__str__()
    
    def kth_from_end(self, k):
        og_list = []
        current_node = self.head

        if self.head is None:
            raise TargetError("List is empty")
        
        while current_node:
            og_list.append(current_node.value)
            current_node = current_node.next
            
        if k < 0:
            raise TargetError("Please enter a number between 0 and length of linked list")
        elif k <= len(og_list)-1:
            og_list.reverse()
            return og_list[k]   
        else:
            raise TargetError("Index is larger than length of the Linked List")
        

class TargetError(Exception):
    print(Exception)

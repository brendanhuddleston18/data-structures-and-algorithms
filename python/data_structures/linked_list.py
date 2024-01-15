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



class TargetError:
    pass

class Node():

  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
    """
    Put docstring here
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
    
    def __str__(self):
        # Returns: a string representing all the values in the LInked List:
        current = self.head
    



class TargetError:
    pass

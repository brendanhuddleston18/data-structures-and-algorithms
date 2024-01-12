class Node():

  def __init__(self, value):
    self.value = value
    self.next = none

class Linked_list():

  def __init__(self):
    self.head = none

  def insert(self,value):
    # 
    new_node = Node(value)
    new_node.next = self.headself.head = new_node
    pass

  def includes(self, value):
    pass

  def __str__(self):
    # Returns: a string representing all the values in the LInked List:

    current = self.head

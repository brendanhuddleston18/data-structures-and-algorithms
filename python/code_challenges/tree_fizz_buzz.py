from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


def fizz_buzz_tree(tree):
    
    collection = tree.breadth_first()   
    fizz_buzz_collection = []
    cloned_tree = tree.clone()

    def walk_and_change(source_node):
        if source_node is None:
                return None

        if (source_node.value % 3) == 0 and (source_node.value % 5) == 0:
            source_node.value = "FizzBuzz"
        elif (source_node.value % 3) == 0 :
            source_node.value = "Fizz"
        elif (source_node.value % 5 == 0):
            source_node.value = "Buzz"
        else:
            source_node.value = str(source_node.value)
        
        if source_node.children:
            for child in source_node.children:
                walk_and_change(child)
    
    walk_and_change(cloned_tree.root)

    return cloned_tree
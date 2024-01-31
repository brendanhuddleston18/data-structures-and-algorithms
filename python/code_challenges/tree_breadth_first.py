from data_structures.binary_tree import BinaryTree
from data_structures.queue import Queue


def breadth_first(tree):
    value_list = []

    if tree.root is None:
        return []

    bfs_queue = Queue()
    bfs_queue.enqueue(tree.root)

    

    while not bfs_queue.is_empty():
        current_node = bfs_queue.dequeue()
        value_list.append(current_node.value)
    
        if current_node.left is not None:
            bfs_queue.enqueue(current_node.left)
           
        if current_node.right is not None:
           bfs_queue.enqueue(current_node.right)


    return value_list
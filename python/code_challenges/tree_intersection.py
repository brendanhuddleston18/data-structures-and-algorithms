from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable

def tree_intersection(tree1, tree2):
  hashmap = Hashtable()

  match_list = []
  def set_hashmap(node):
    if node is None:
      return None

    hashmap.set(str(node.value), str(node.value))
    set_hashmap(node.left)
    set_hashmap(node.right)

  set_hashmap(tree1.root)

  def check_hashmap(node):
    if node is None:
      return None

    if hashmap.has(str(node.value)):
      match_list.append(node.value)

    check_hashmap(node.left)
    check_hashmap(node.right)

  check_hashmap(tree2.root)

  return match_list



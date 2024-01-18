from data_structures.linked_list import LinkedList



def zip_lists(a, b):
    linked_list_one = []
    linked_list_two = []
    zipped_list = []

    a.current_node = a.head
    while a.current_node:
        linked_list_one.append(a.current_node.value)
        a.current_node = a.current_node.next

    b.current_node = b.head
    while b.current_node:
        linked_list_two.append(b.current_node.value)
        b.current_node = b.current_node.next

    
    # ChatGPT helped me with this, once my before code didn't pass test three
    index = 0
    while index < len(linked_list_one) or index < len(linked_list_two):
        if index < len(linked_list_one):
            zipped_list.append(linked_list_one[index])
        if index < len(linked_list_two):
            zipped_list.append(linked_list_two[index])
        index += 1


    # What I had BEFORE
    # if len(linked_list_one) >= len(linked_list_two):
    #     for node in range(len(linked_list_one)):
    #         zipped_list.append(linked_list_one[node])
    #         zipped_list.append(linked_list_two[node])
    # else: 
    #     for node in range(len(linked_list_two)):
    #         zipped_list.append(linked_list_one[node])
    #         zipped_list.append(linked_list_two[node])


    new_zipped_linked_list = LinkedList()
    zipped_list.reverse()
    for value in zipped_list:
        new_zipped_linked_list.insert(value)

    return new_zipped_linked_list
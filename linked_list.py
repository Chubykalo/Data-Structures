class Node:
    def __init__(self, data):  # every node consists of self and data
        self.data = data
        self.next = None  # initially the node is set to None per logic of the linked list data structure


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head  # self.head is set to None by default
        while current_node:  # while current node is not None
            print(current_node.data)  # print the data field of each of the nodes and iterate through the list by going to the next line
            current_node = current_node.next

    def len_iterative(self):
        count = 0  # keep track of the number of nodes encountered thus far
        current_node = self.head  # current node set to the head of the list
        while current_node:  # is not None  --- loop through the list
            count += 1
            current_node = current_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def append(self, data):  # insert a node at the end of the list
        new_node = Node(data)  # initialize Node class

        if self.head is None:  # check if list is empty by checking if the header points to None
            self.head = new_node  # if list is empty, appoint the new node as the head of the list
            return

        last_node = self.head
        while last_node.next:  # checks if last node is not None
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):  # the inserted data needs to point to the head of the list and become the head itself
        new_node = Node(data)  # initialize Node class

        new_node.next = self.head  # points the new node to the head of the list
        self.head = new_node  # makes the new node to be the head of the list

    def insert_after_node(self, previous_node, data):  # inserts a node after a specific node

        # A -> B -> C -> Null   Add D after B  ::::: A -> D -> B -> C

        if not previous_node:  # checks if previous node is in the list
            print('Previous node is not in the list')
            return

        new_node = Node(data)  # initialize the Node class

        new_node.next = previous_node.next  # assigns the pointer of the new node to be the same as the pointer of the previous node
        previous_node.next = new_node  # assigns the pointer of the previous node to the new node.

    def delete_node(self, key):

        # edge case for when the node is head
        current_node = self.head
        if current_node and current_node.data == key:  # if the current node is not None and not key
            self.head = current_node.next
            current_node = None  # gets rid of the head element
            return

        # standard case
        # find the node in the list which consists of the searched key and keep track of the previous node as we move through the list
        previous_node = None
        while current_node and current_node.data != key:  # move the current node along the list
            previous_node = current_node
            current_node = current_node.next

        # check if current node is in the list
        if current_node is None:
            return

        previous_node.next = current_node.next  # make the pointer jump the slot of the node to be deleted
        current_node = None

    def delete_node_at_position(self, pos):
        current_node = self.head

        #  case for when node is head
        if pos == 0:
            self.head = current_node.next
            current_node = None
            return

        previous_node = None
        count = 0
        while current_node and count != pos:
            previous_node = current_node
            current_node = current_node.next
            count += 1

        if current_node is None:
            return

        previous_node.next = current_node.next
        current_node = None

    def swap_nodes(self, key1, key2):
        if key1 == key2:  # if both nodes are the same one, there is no swap logic
            return

        # finding the appropriate nodes

        previous_node1 = None
        current_node1 = self.head  # set current node to the head of the list
        while current_node1 and current_node1.data != key1:  # while current node is not none and its data element is not the first key
            previous_node1 = current_node1  # find node corresponding to key 1
            current_node1 = current_node1.next

        previous_node2 = None
        current_node2 = self.head
        while current_node2 and current_node2.data != key2:
            previous_node2 = current_node2  # find the node corresponding to key 2
            current_node2 = current_node2.next

        if not current_node1 or not current_node2:  # check if current nodes exist. Cannot swap an element that is not present in the list
            return

        # condition when first key is the head of the list

        if previous_node1:
            previous_node1.next = current_node2  # set pointer
        else:
            self.head = current_node2

        if previous_node2:
            previous_node2.next = current_node1
        else:
            self.head = current_node1

        # swapping the nodes

        current_node1.next, current_node2.next = current_node2.next, current_node1.next

    def merge_two_sorted_lists(self, llist):  # merges itself with another list

        pointer_1 = self.head  # pointer of the original list
        pointer_2 = llist.head  # pointer of the list with which we merge
        merged_list_pointer = None

        if not pointer_1:  # if either of the lists is None, return the other list
            return pointer_2
        if not pointer_2:
            return pointer_1

        if pointer_1 and pointer_2:  # if both lists exist...
            if pointer_1.data <= pointer_2.data:
                merged_list_pointer = pointer_1  # assigns the lesser value to the head of the new list
                pointer_1 = merged_list_pointer.next  # advances the merging lists' pointers
            else:  # mirror case
                merged_list_pointer = pointer_2
                pointer_2 = merged_list_pointer.next
            merged_list_head = merged_list_pointer

        while pointer_1 and pointer_2:  # loop which advances the pointers through both lists until reaching a None
            if pointer_1.data <= pointer_2.data:
                merged_list_pointer.next = pointer_1
                merged_list_pointer = pointer_1
                pointer_1 = merged_list_pointer.next
            else:
                merged_list_pointer.next = pointer_2
                merged_list_pointer = pointer_2
                pointer_2 = merged_list_pointer.next

        if not pointer_1:  # when merged list point reaches none in one list, follow up with the other
            merged_list_pointer.next = pointer_2
        if not pointer_2:
            merged_list_pointer.next = pointer_1
        return merged_list_head






llist1 = LinkedList()
llist2 = LinkedList()

llist1.append('1')
llist1.append('5')
llist1.append('7')
llist1.append('9')
llist1.append('10')

llist2.append('1')
llist2.append('3')
llist2.append('4')
llist2.append('6')
llist2.append('8')

llist1.print_list()
print('\n')
llist2.print_list()

llist1.merge_two_sorted_lists(llist2)
print('\n')
llist1.print_list()
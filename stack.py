class Stack():
    def __init__(self):
        self.items = []  # class variable that represents the items of the stack and has an empty list

    def push(self, item):  # push a given item to the top of the stack
        self.items.append(item)  # add to the end of the list (top of the stack)

    def pop(self):  # return the top element of the stack
        return self.items.pop()

    def get_stack(self):  # return stack list
        return self.items

    def is_empty(self):  # returns True if items is empty
        return self.items == []

    def peek(self):  # look at top item from the stack
        if not self.is_empty():
            return self.items[-1]

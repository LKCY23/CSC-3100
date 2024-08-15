class Linked_List_Node:
    def __init__(self, x): # O(1)
        self.item = x
        self.next = None

    def later_node(self, i): # O(i)
        if i == 0:
            return self
        assert self.next
        return self.next.later_node(i - 1)
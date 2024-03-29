# Date of completion : 12-06-2023
# Author : Malnika Shrestha,Wobo Nancy,Sudin Adhikari
# section: ZDD
class SetList:
    class Node: # node class to add properties like data and links to next and previous nodes.
        def __init__(self, data=None, set_list=None, next_node=None, prev_node=None):
            self.data = data
            self.set_list = set_list
            self.next_node = next_node
            self.prev_node = prev_node

        def get_data(self): #returns data of the node
            return self.data

        def get_next(self): #returns next node
            return self.next_node

        def get_previous(self): #returns previous node
            return self.prev_node

        def get_set(self):
            return self.set_list

    def __init__(self): #costructor to initiate a empty linked list
        self.head = None
        self.tail = None

    def get_front(self): #returns the head node of the list
        return self.head 

    def get_back(self): # returns the tail/last node of the list
        return self.tail

    def make_set(self, data): #creates a new set with a single node
        if self.head is not None:
            return None
        else:
            new_node = self.Node(data, self, None, None)
            self.head = new_node
            self.tail = new_node
            return new_node

    def find_data(self, data): # searches a node with given data, returns None if not found
        current = self.get_front()
        while current is not None:
            if current.data == data:
                return current
            current = current.get_next()
        return None

    def representative_node(self): 
        if len(self) == 0:
            return None
        return self.get_front()

    def representative(self): #returns the data of representative node
        if len(self) == 0:
            return None
        return self.get_front().get_data()

    def union_set(self, other_set): #joins the list with another list
        current = other_set.head
        while current is not None:
            current.set_list = self
            current = current.get_next()
        if self.tail is not None:
            self.tail.next_node = other_set.head
            self.tail = other_set.tail
        else:
            self.head = other_set.head
            self.tail = other_set.tail
        other_set.head = None
        other_set.tail = None
        return len(other_set)

    def __len__(self): #returns the number of nodes in the list
        length = 0
        current = self.get_front()
        while current is not None:
            length = length + 1
            current = current.get_next()
        return length

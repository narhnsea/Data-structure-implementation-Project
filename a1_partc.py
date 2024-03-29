# Date of completion : 13-06-2023
# Author : Sudin Adhikari
# Supporters: Malnika Shrestha,Wobo Nancy
# section: ZDD
from a1_partb import SetList

class DisjointSet:
    def __init__(self):
        self.parent = {}  # dictionary to store key-value
        self.size = {}    # dictionary to store size of each set
        self.n_sets = 0
        self.n_elements = 0

    def make_set(self, element):# returns False if element matches any key in DisjointSet object, else returns True after creating a key-value pair
        if element in self.parent:
            return False
        new_node = SetList.Node(element)
        self.parent[element] = new_node.get_data()
        self.size[element] = 1
        self.n_sets += 1
        self.n_elements += 1  # new element/key gets created when make_set() is called
        return True

    def get_set_size(self, element): # returns 0 if element doesn't match any keys in DisjointSet object(self), else using root returns size of set from size dictionary
        if element not in self.parent:
            return 0
        return self.size[self.find_set(element)]

    def find_set(self, element):# returns None if element doesn't match any key in DisjointSet object(self), else returns parent[element]/data in new_node
        if element not in self.parent:
            return None
        if self.parent[element] != element:
            self.parent[element] = self.find_set(self.parent[element]) # recursion to find root, one recursion call at max
        return self.parent[element]

    def union_set(self, element1, element2): # returns False if element1 or element2 doesn't match any keys, or if element1 and element2 belong to same set, else returns True after updating the parent of root and size
        if (element1 not in self.parent) or (element2 not in self.parent) or (self.find_set(element1) == self.find_set(element2)):
            return False
        if self.get_set_size(element1) < self.get_set_size(element2):
            self.parent[self.find_set(element1)] = self.parent[self.find_set(element2)]
            self.size[self.find_set(element2)] += self.size[self.find_set(element1)]
            self.n_sets -= 1
            count = 0
            for element in self.parent: # prevents incorrect size 
                if self.parent[element] == self.parent[self.find_set(element2)]:
                    count += 1
            if count < self.size[self.find_set(element2)]:
                self.size[self.find_set(element2)] -= 1
        else:
            self.parent[self.find_set(element2)] = self.parent[self.find_set(element1)]
            self.size[self.find_set(element1)] += self.size[self.find_set(element2)]
            self.n_sets -= 1
            count = 0
            for element in self.parent:
                if self.parent[element] == self.parent[self.find_set(element1)]:
                    count += 1
            if count < self.size[self.find_set(element1)]:
                self.size[self.find_set(element1)] -= 1
        return True

    def get_num_sets(self): # returns number of sets in DisjointSet object (self)
        return self.n_sets

    def __len__(self):# returns number of keys in DisjointSet object parent dictionary
        return self.n_elements




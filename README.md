# Data-structure-implementation-Project
 Data-structure-implementation-Project-in-python
# Data Structure implemenation

## Objectives

- draw diagrams of your implementation in order to gain a better insight as to how this is accomplished.
- implement a linked list that we can use to create a disjoint set
- implement a data structure
- write a more complicated recursive function

## Part A: Drawings

The specs (parts B and C) should be read first to get an idea of the functionalities in Part A.
Then, modify each of the lists in the drawings to show what the result of the operation (mentioned in each of the drawings) is:

- Notice what is changing and how.
- The idea is to think through what needs to change to achieve your goals.
- Modify the diagrams electronically using something like paint or other diagramming software

## Part B: Implementing our SetList

Add data members to both Node and SetList.

### Node

The Node class is declared within SetList. It stores:

- a piece of data
- a reference to the next Node in the SetList (None if Node is last node)
- a reference to the previous Node in the SetList (None if Node is first node)
- a reference to the SetList.

When a Node is initialized, it is passed a data value and a reference to the SetList the Node belongs to. Optionally it is also passed a reference to the next node and a reference to the previous node (in that order). If the data values are not passed in, they are defaulted to None.

The Node function has the following member functions:

---

```python
def get_data(self)
```

function returns data stored in node

---

```python
def get_next(self)
```

function returns reference to next node in SetList

---

```python
def get_previous(self)
```

function returns reference to previous node in SetList

---

```python
def get_set(self)
```

function returns reference to the SetList

### SetList

A SetList is a doubly linked list that can be used to represent a single set of a disjoint set. With a SetList, each node contains data and is linked to other nodes in the list. The difference with a regular doubly linked list is that each node also contains a link to the SetList object. The first node within the SetList contains the set's **representative**.

The following is a diagram of the set: {"cat", "fish", "dog"}. Note that values within a set do not have any particular ordering and the exact ordering does not matter in your implementation. This means that any of the 3 can be the representative..its simply a matter of which one is at the front of the list
![SetList](https://user-images.githubusercontent.com/1699186/214759162-b11c10bd-f188-4e7b-8275-1681d6ad79b1.png)

When a SetList is initialized, the SetList is empty.

The SetList has the following member functions

---

```python
def get_front(self)
```

This function returns a reference to the first node in the list

---

```python
def get_back(self)
```

This function returns a reference to the last node in the list

---

```python
def make_set(self, data)
```

This function adds the first value to the SetList object if the list is empty and returns a reference to newly created Node. If the list is not empty, function does nothing and returns None.

---

```python
def union_set(self, other_set)
```

This function is passed a SetList and performs a union with the current object. This means that the elements of other_set are transfered to current object and other_set becomes empty in the process. Function returns number of elements transferred. Note, this process does not create or destroy any of the nodes.

---

```python
def find_data(self, data)
```

This function is passed a data value, the function returns the a reference to the Node containing data. If data does not exist, function returns None

---

```python
def representative_node(self)
```

This function returns a reference to the node that holds the representative of the SetList. If SetList is empty, function returns None

```python
def representative(self)
```

This function returns the data of the representative node of the SetList. If SetList is empty, function returns None

---

```python
def __len__(self)
```

This function returns the number of items within the SetList.

---

## Part C - DisjointSet Class (15 marks)

Implementation of this class is done in a1_partc.py

A DisjointSet class represents a disjoint set which is a set of sets where every element can only belong to exactly one set.

When a DisjointSet class is instantiated it is passed nothing and contains no sets. It creates an empty [Python dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) which will be used to store the elements of the DisjointSet.

The DisjointSet has the following member functions:

---

```python
def make_set(self,element)
```

If element already exists within the Disjoint set, the function does nothing and returns false.

If element does not exist in the DisjointSet, this function will add it to the DisjointSet by:

- creating a new SetList object containing only one node, with the element as only value in the SetList
- adding a new dictionary entry where element is the key and a reference to the node containing element as the value
- return true

Suppose we ran the following code:

```python
    ds = DisjointSet()
    ds.make_set("cat")
    ds.make_set("dog")
    ds.make_set("fish")
```

The following is what we would create:
![DisjointSet](https://user-images.githubusercontent.com/1699186/214759216-899b4334-bf04-4cea-8cdb-78f5f4a7e76f.png)

---

```python
def find_set(self, element)
```

Function returns the representative of the set containining element.

---

```python
def get_num_sets(self)
```

This function returns the number of sets in the DisjointSet. Note that this is not the same as the number of elements. You can start with 2 elements in unique sets and join them using the union_set() function.

---

```python
def __len__(self)
```

This function returns the number of elements in the DisjointSet.

---

```python
def get_set_size(self, element):
```

This function returns the size of the set containing element. If element does not exist within the disjoint set, function returns 0

---

```python
def union_set(self, element1, element2)
```

Function performs a union of the two sets containing element1 and element2 respectively. If the two elements are already in the same set or if either of the elements do not exist, function does nothing and returns false. otherwise perform a union on the two sets, creating one set and return true

Example, suppose we ran the following code:

```python
    ds = DisjointSet()
    ds.make_set("cat")
    ds.make_set("dog")
    ds.make_set("fish")
    ds.union_set("cat","dog")
```

Our DisjointSet would look like:

![union_set](https://user-images.githubusercontent.com/1699186/216095712-b65af297-9c27-4a70-9e39-e806eff17a74.png)

---

## Part D - Maze Runner Function - Recursive (5 Marks):

Implementation of this function is done in a1_partd.py

We describe a maze as having row x col cells. For example if row was 3, and col was 4, then we would have a grid of cells as follows. We describe a wall by the two cell numbers the wall separates. If every single wall existed, there would be (row-1)(col) + (col-1)(row) walls.

```
  0 |  1 |  2 |  3
-------------------
  4 |  5 |  6 |  7
--------------------
  8 |  9 | 10 | 11
```

A Maze class (which you do not need to implement) describes a maze as mentioned above. This class is defined in maze.py. It has methods that you can use to travel through the maze (i.e. figure out where you are, find a neighbour cell etc.)

Write a **recursive** maze runner function:

```python
def find_path(maze, from_cell, to_cell);
```

The find\*path function will find a path from cell number \*\*\_from*cell**\* to cell number **\_to_cell*\*\* and will return it as a list containing all the cell numbers along the path, from the from_cell to the to_cell.

You are allowed to use this function as a wrapper to a recursive function that does the work, allowing for other arguments to your function prototype or additional processing. However, the function that does the work to find the path must be recursive.

For example, suppose the from_cell was 0 and the to_cell was 3, using the maze below:

```
  0 |  1    2    3
         ----------
  4    5 |  6    7
----
  8    9   10 | 11
```

The find*path function would return this path: [0, 4, 5, 1, 2, 3].
\*\*\_Note that in case there exists a path to the to_cell, that path is unique.*\*\*

### Online visualizer

To help you debug your program, when you run the tester, the tester will create a "path" file based on the path your find_path function generates (its return values.) You can see what is happening by going to this site:

[Online Visualizer](https://seneca-dsa456.github.io/dsa456-s23/)

- Use the radio buttons to select the test in question (see your error message.)
- Then, load the corresponding testpath file.

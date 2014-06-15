"""
disjoint_set.py
"""

class DisjointSet:
  """
  This is an ADT that implements a disjoint set when
  each element is represented by a _unique_ number.
  """
  
  def __init__(self, number_of_elements):
    """ 
    The constructor for this ADT.

    number_of_elements -- The total number of elements the
                          set is to have. 
    """

    self.array = [-1] * number_of_elements
    
  def union(self, root1, root2):
    """ 
    Unites two roots. In case the args are not roots, this
    function calls self.find() and uses the roots of the numbers.
    """

    root1, root2 = self.find(root1), self.find(root2)
    if (self.array[root2] < self.array[root1]):
      self.array[root2] += self.array[root1]
      self.array[root1] = root2
    else:
      self.array[root1] += self.array[root2]
      self.array[root2] = root1

  def find(self, int_x):
    """ 
    Finds the roots of the passed in number. If x is not a root,
    it carries out path compression while looking for x's root.
    """

    if (self.array[int_x] < 0):
      return int_x
    else:
      self.array[int_x] = self.find(self.array[int_x])
      return self.array[int_x]

  def getList(self):
    """
    Returns a list of lists that represents all elements of the
    set. 
    
    If L = getList() and l = L[0],
    l[0] is the element and l[1] is the parent. 
    If the parent is negative, it is a root. 
    """

    lst = []
    for i in range(len(self.array)):
      lst.append([i, self.array[i]])
    return lst

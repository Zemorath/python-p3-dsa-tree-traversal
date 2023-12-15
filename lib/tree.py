class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = []
    nodes_to_visit = [self.root]
    
    if nodes_to_visit:
      while len(nodes_to_visit) > 0:
        self.root = nodes_to_visit.pop(0)
        if self.root["id"] == id:
          return self.root
        else:
          result.append(self.root)
          nodes_to_visit = self.root['children'] + nodes_to_visit
    else:
      return None
    


"""Initialize an empty output list
Initialize an list of nodes to visit and add the root node to it
While there are nodes in the nodes to visit list
    Remove the first node from the nodes to visit list
    Add its value to the output list
    Add its children (if any) to the end of the nodes to visit list
Return the output list"""
#!/usr/bin/env python
"""Provides Node class for Trie

Node holds a dictionary with mappings of all of the key mappings to other Nodes
or the "None" reference.
"""

__author__ = "Jesse Hughes"
__credits__ = ["Jesse Hughes"]
__license__ = "GPL"
__version__ = "0.9"
__email__ = "jessebhughes@gmail.com"
__status__ = "Beta"

class Node:
    def __init__(self, parent, value, *childVals):
        """ Initialize a node object
        : param Node parent : The parent Node
        : param var childVals : 0-n values to add as children of this node
        : return : None
        """
        self.parent = parent
        self.val = value
        self.children = { childValue : Node(self, childValue) \
                          for childValue in childVals \
                          if childValue not in self.children }

    def __contains__(self, childValue):
        """ Overloading the "contains" operator for using "in"
        : param var childValue : Value to be checked against children added
        : return : True if childValue has been added, False otherwise
        """
        return key in self.children

    def addChild(self, childVal = None):
        """ Initializes and adds a Node object to the dict of children
        : param var childVal : value to add as child to this node
        : return : True if success, False if failure (node already exists)
        """
        if childVal not in self.children:
            self.children[val] = Node(self, childVal)
            return True
        return False

    def getChild(self, childVal):
        """ Returns the requested child Node object if present """
        if childVal in self.children:
            return self.children[childVal]
        raise KeyError("Value:", childVal, "not added to children nodes")

    def getViewChildVal(self):
        """ Returns a view of the child values """
        return self.children.values()

    def getViewChildKeys(self):
        """ Returns a view of the child keys """
        return self.children.keys()

if __name__ == "__main__":
    pass

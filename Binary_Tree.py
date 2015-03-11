#define the binary tree class
class BinarySearchTree():
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        
#define insert function for binary search tree
    def insert(self, key):
        if not self.key:
            self.key = key
        elif key < self.key:
            if self.left is None:
                self.left = BinarySearchTree(key)
            else:
                self.left.insert(key)
        elif key >= self.key:
            if self.right is None:
                self.right = BinarySearchTree(key)
            else:
                self.right.insert(key)
#function for getting the values between an interval
#by going through the whole tree
    def get_values_in_interval(self, leftMargin, rightMargin):
        if self.left is not None:
            self.left.get_values_in_interval(leftMargin, rightMargin)
        if self.right is not None:
            self.right.get_values_in_interval(leftMargin, rightMargin)
        if self.key >= leftMargin and self.key <= rightMargin:
            print self.key
#function for retrieving an item and verifying that it is in the tree    
    def get_item(self, key):
        if self is None:
            return None
        if self.key == key:
            return self.key
        elif key < self.key and self.left is not None:
            return self.left.get_item(key)
        elif key > self.right and self.right is not None:
            return self.right.get_item(key)
        return None

# create the tree and insert the nodes
tree = BinarySearchTree(50)
tree.insert(17)
tree.insert(72)
tree.insert(12)
tree.insert(23)
tree.insert(54)
tree.insert(76)
tree.insert(9)
tree.insert(14)
tree.insert(19)
tree.insert(67)
#print the values from the interval 23 and 68
print tree.get_values_in_interval(23, 68)




        
    

import sys
sys.path.append('../queue_and_stack')



class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #Compare root
        if value < self.value:
            #If lesser, go left child
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                #If somethings already there, recurse
                self.left.insert(value)
        elif value > self.value:    #value >= nodes value:
            #If greater, go right
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    # def get_max(self):
    #     if not self.right:
    #         return self.value
    #     else:
    #         self.right.get_max()

    # # Call the function `cb` on the value of each node
    # # You may use a recursive or iterative approach
    # def for_each(self, cb):
    #     cb(self.value)
    #     if self.left:
    #         self.left.for_each(cb)
    #     if self.right:
    #         self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     pass

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     pass

    # # STRETCH Goals -------------------------
    # # Note: Research may be required

    # # Print In-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass

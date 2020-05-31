import time
from collections import Counter

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# # Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# copy/pasted BSTNode from past project
class BSTNode:
    def __init__(self, value="Default Value"):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # create node to insert into tree
        new_node = BSTNode(value)

        # check to see if there are existing children
        if self.value:
            if value >= self.value:
                if self.right is None:
                    self.right = new_node
                else:
                    self.right.insert(value)
            else:
                if self.left is None:
                    self.left = new_node
                else:
                    self.left.insert(value)
        else:
            self.value = value  
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check to see if the BST is empty
        if self.value:
            # check to see if the target == the self.value
            if target == self.value:
                return True
            # check to see if target is larger or smaller then the self.value
            if target > self.value:
                if not self.right:
                    return False
                return self.right.contains(target)
            else:
                if not self.left:
                    return False
                return self.left.contains(target)                    
        # if there is no value then just return False
        else:
            return False

# Create new BST node

BST = BSTNode()    

counter1 = Counter(names_1)
counter2 = Counter(names_2)

for key in counter1:
    if key in counter2:
        duplicates.append(key)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

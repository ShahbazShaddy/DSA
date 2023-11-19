# #---------------------------Question 3---------------------------

# The task of designing a binary search tree (BST) data structure that performs
# INSERT operations in O(√log n) time using a comparison-based algorithm is impossible.
# The Proof is given below:
# A binary search tree (BST) is a tree data structure in which each node has at most two children
# referred to as the left child and the right child. For each node
# all elements in the left subtree are less than the node, and all elements
# in the right subtree are greater than the node. The time complexity of the INSERT operation
# in a BST is determined by the height of the tree. In the worst-case scenario (a skewed tree)
# the height of the tree is n (where n is the number of nodes), and the time complexity of the INSERT
# operation is O(n). In the best-case scenario (a balanced tree) the height of the tree is log n
# and the time complexity of the INSERT operation is O(log n). Therefore, even with the best-case
# scenario, the time complexity of the INSERT operation in a BST is O(log n), which is greater than O(√log n). 
# This is due to the nature of the comparison-based algorithm, which must traverse the tree from
# the root to the appropriate leaf for insertion, making comparisons at each step.
# Therefore, it is impossible to design a BST that performs INSERT operations in O(√log n) time
# using a comparison-based algorithm.

#---------------------------Question 4---------------------------
# (a)
def findDuck(ducks, start, end):
    if start > end:
        return "No such duck"
    
    mid = (start + end) // 2
    result = compareToStick(mid)
    
    if result == "the same":
        return mid
    elif result == "taller":
        return findDuck(ducks, start, mid - 1)
    else: # result == "shorter"
        return findDuck(ducks, mid + 1, end)
def compareToStick(duck, stick):
    if duck == stick:
        return "the same"
    elif duck > stick:
        return "taller"
    else: # duck < stick
        return "shorter"

# Description: The algorithm starts by comparing the middle duck to the stick.
# If the duck is the same height as the stick, it returns the index of that duck. If the duck is taller
# it repeats the process for the left half of the ducks. If the duck is shorter, it repeats the process
# for the right half of the ducks. If no matching duck is found, it returns "No such duck".

# (b)

# Any algorithm in this model of computation must use Ω(log(n)) comparisons because of the nature of the problem.
# The ducks are sorted, but we have no other information about their heights.
# The only way to find a specific height is to compare it to the stick, and the most efficient
# way to do this is to use a binary search, which has a lower bound of Ω(log(n)) comparisons.
# This is because with each comparison, we eliminate half of the remaining ducks from consideration.
# Therefore, in the worst case, we must make log(n) comparisons.


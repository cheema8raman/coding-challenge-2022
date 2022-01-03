'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.
'''

'''
Task in hand - Serialization is to store a tree in an array so that it can be later restored ,
       Deserialization is reading tree back from the array. 
       Now your task is to complete the function serialize which stores the tree into an array A[ ] and 
       deSerialize which deserializes the array to the tree and returns it.
       
Given tree is Binary Search Tree, we can store it by either storing preorder or postorder traversal
Resource - https://www.youtube.com/watch?v=u4JAi2JJhI8
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    values = []

    def serializer(node):
        if not node:
            values.append('N')
        else:
            values.append(node.val)
            serializer(node.left)
            serializer(node.right)

    serializer(root)

    return ','.join(values)


def deserialize(s):
    values = iter(s.split(','))

    def deserializer():
        # this will automatically gives next element
        val = next(values)

        # this step when node has no left or right child
        if val == 'N':
            return None
        else:
            node = Node(val)
            node.left = deserializer()
            node.right = deserializer()
            return node

    return deserializer()

node = Node('root', Node('left', Node('left.left')), Node('right'))
print(deserialize(serialize(node)).left.left.val == 'left.left')
print(deserialize(serialize(node)).left.left.val == 'left.wrong')
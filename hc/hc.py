# Huffman tree

class Node:
    def __init__(self, x, y):
        self.total = x + y

def insert(queue, node):
    x = 0
    while x < len(queue):
        if type(queue[x]) == tuple:
            val = queue[x][1]
        else:
            val = queue[x].total
        if val >= node.total:
            queue.insert(x, node)
        return queue
    queue.append(node)
    return queue

def reverse(tree):
    new_tree = {}
    for x in list(set(tree.values())):
        new_tree[x] = []
    for key, value in tree.items():
        print(key, value)
        new_tree[value].append(key)

    return new_tree
        

    
letter_frequencies = {"a": 12, "b":13, "c": 14, "d": 15, "e": 16, "f": 17}
queue = list(sorted(letter_frequencies.items(), key=lambda x:x[1]))

n1 = Node(queue[0][1], queue[1][1])
tree = {queue[0][0]: n1, queue[1][0]: n1}
queue = insert(queue, n1)
current_letter = False

while len(queue) != 0:
    print(current_letter, "cl", current_letter == False)
    y = queue.pop(0)
    if type(y) == tuple:
        val = y[1]
        letter = y[0]
    else:
        val = y.total
        letter = y
    if current_letter != False:
        t = Node(current_letter[1], val)
        queue = insert(queue, t)
        print(current_letter[0], "---")
        tree[current_letter[0]] = t
        tree[letter] = t
        current_letter = False
    else:
        current_letter = letter, val
        
print(queue, "\n", tree)
reverse_tree = reverse(tree)
print()
print(reverse_tree)
# Need to reverse the tree for reading/writing

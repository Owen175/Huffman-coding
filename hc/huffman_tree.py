class Node:
    def __init__(self, value, letter=None, x=None, y=None, parent=None, hasChildren=False):
        self.value = value
        self.letter = letter
        self.hasChildren = hasChildren
        self.children = [x, y]
        self.pos = None
        self.parent = parent
        self.root = False

class HuffmanTree:
    def __init__(self, letterNodeConnection, root: Node):
        self.lnc = letterNodeConnection
        self.root = root

def string_to_compressed(string, hmt: HuffmanTree):
    conversion_dict = {}
    compressed = ""
    for char in string:
        if char in conversion_dict.keys():
            compressed += conversion_dict[char]
        else:
            temp = ascend_tree(hmt.lnc[char])
            compressed += temp
            conversion_dict[char] = temp

    return compressed
def ascend_tree(node: Node):
    char_code = ""
    while not node.root:
        char_code += node.pos
        node = node.parent

    return char_code[::-1]  # Reverses so that you can descend the tree.

def compressed_to_string(compressed, hmt: HuffmanTree):
    node = hmt.root
    string = ""
    for x in compressed:
        node = node.children[int(x)]

        if not node.hasChildren:
            string += node.letter
            node = hmt.root
    return string

def get_letter_frequencies(string):
    lfd = {}
    for x in string:
        if x in lfd.keys():
            lfd[x] += 1
        else:
            lfd[x] = 1
    return lfd
def make_huffman_tree(letter_frequencies):
    queue = [Node(x[1], x[0]) for x in list(sorted(letter_frequencies.items(), key=lambda x:x[1]))]
    letter_node_connection = {}
    for x in queue:
        letter_node_connection[x.letter] = x

    while len(queue) != 1:
        n1, n2 = queue.pop(0), queue.pop(0)
        n3 = Node(n1.value + n2.value, x=n1, y=n2, hasChildren = True)
        n1.parent, n2.parent = n3, n3
        n1.pos, n2.pos = "0", "1"  # 0 is left, 1 is right
        queue.append(n3)
        queue = sorted(queue, key=lambda x: x.value)

    queue[0].root = True
    return HuffmanTree(letter_node_connection, queue[0])


string = "bananna balls"

HMT = make_huffman_tree(get_letter_frequencies(string))

compressed = string_to_compressed(string, HMT)
uncompressed = compressed_to_string(compressed, HMT)



def toBinary(a):
  l,m=[],""
  for i in a:
    l.append(ord(i))
  for i in l:
    m += (str(bin(i)[2:]))
  return m

print(round(len(compressed) / (len(string) * 8) * 100, 2), "% of original size.")

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''  # This will store 0 or 1 to represent the binary code.

    def printNodes(self, val=''):
        newVal = val + str(self.huff)

        # If the node is not a leaf, recursively call for left and right children
        if self.left:
            self.left.printNodes(newVal)
        if self.right:
            self.right.printNodes(newVal)
        
        # If it's a leaf node, print the symbol and its Huffman code
        if not self.left and not self.right:
            print(f"{self.symbol} -> {newVal}")


# Gather user input for symbols and their frequencies
num_symbols = int(input("Enter the number of symbols:\n"))

chars = []
freq = []
print("Enter the symbols and their frequencies:")
for i in range(num_symbols):
    symbol = input(f"Enter symbol {i + 1}:\n")
    frequency = int(input(f"Enter frequency for symbol '{symbol}':\n"))
    chars.append(symbol)
    freq.append(frequency)

# Create initial list of nodes
nodes = []
for i in range(len(chars)):
    nodes.append(Node(freq[i], chars[i]))

# Building the Huffman Tree
while len(nodes) > 1:
    # Sort nodes based on frequency
    nodes = sorted(nodes, key=lambda x: x.freq)

    # Pick two nodes with lowest frequency
    left = nodes[0]
    right = nodes[1]

    # Assign binary codes (0 and 1)
    left.huff = '0'
    right.huff = '1'

    # Combine the two nodes to create a new parent node with combined frequency
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)

    # Remove the two nodes and add the new node to the list
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(newNode)

# Print the Huffman codes
print("Huffman Codes are:")
if nodes:
    nodes[0].printNodes()


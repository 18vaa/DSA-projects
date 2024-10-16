#Import libraries
import heapq
import struct
from collections import Counter

#Setup a Huffman Tree

#Setup a node class to initialize new nodes in the tree
class Node:
    #Every node will have a character and a frequency associated with it. Init the left and right pointers to null.
    def __init__(self,char,freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    #In order to build a huffman tree, we need to be able to compare the frequency with which a character appears in the tree. We need to compare the frequency of the current node with the other node and return a boolean value.
    def __lt__(self,other):
        return self.freq < other.freq
    
class HuffmanTree:
    def __init__(self, text):
        self.text = text
        self.root = self.build_tree()
        self.code_table = self.build_code_table()

    def build_tree(self):
        freq_dict = Counter(self.text)
        heap = [Node(char,freq) for char,freq in freq_dict.items()]
        heapq.heapify(heap)

        while len(heap)>1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)

            parent = Node(None, left.freq + right.freq)
            parent.left = left
            parent.right = right
            heapq.heappush(heap,parent)

        return heap[0]
    
    def build_code_table(self):
        code_table = {}
        self.traverse_tree(self.root, "", code_table)
        return code_table
    
    #Recursively traverse the tree
    def traverse_tree(self, node, code, code_table):
        if node.char:
            code_table[node.char] = code
        else:
            self.traverse_tree(node.left, code + "0", code_table)
            self.traverse_tree(node.right, code + "1", code_table)

def compress(text):
    tree = HuffmanTree(text)
    compressed_data = ""
    for char in text:
        compressed_data += tree.code_table[char]
    return compressed_data

def decompress(compressed_data, tree):
    decompressed_text = ""
    current_node = tree.root
    for bit in compressed_data:
        if bit=="0": current_node = current_node.left
        else: current_node = current_node.right
        if current_node.char:
            decompressed_text += current_node.char
            current_node = tree.root
    return decompressed_text


def main():
    text = input("Enter some text here:")
    compressed_data = compress(text)
    decompressed_text = decompress(compressed_data, HuffmanTree(text))
    print("Original text:", text)
    print("Compressed data:", compressed_data)
    print("Decompressed text:", decompressed_text)

if __name__ == "__main__":
    main()

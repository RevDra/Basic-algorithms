import heapq
from collections import defaultdict

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq
    
def huffman_coding(data: str):
    freq_dict = defaultdict(int)
    for char in data:
        freq_dict[char] += 1

    heap = []
    for char, freq in freq_dict.items():
        heapq.heappush(heap, Node(char, freq))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(heap, parent)

    root = heap[0]
    huffman_codes = {}

    def generate_codes(node, current_code = ""):
        if node is None: return
        if node.char is not None: 
            huffman_codes[node.char] = current_code if current_code else "0"
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root)
    return huffman_codes, root

def encode(data, huffman_codes):
    return "".join(huffman_codes[char] for char in data)

def decode(encoded_data, root):
    decoded_output = []
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_output.append(current_node.char)
            current_node = root

    return "".join(decoded_output)

if __name__ == "__main__":
    data = str(input("Enter a string: "))

    codes, tree = huffman_coding(data)
    print("Huffman Code: ")
    for char, code in codes.items():
        print(f"{char}: {code}")

    encoded = encode(data, codes)
    print(f"Encoded: {encoded}")

    decoded = decode(encoded, tree)
    print(f"Decoded: {decoded}")
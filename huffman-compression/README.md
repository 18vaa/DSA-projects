# Huffman Compression

**Huffman Compression** is a lossless data compression algorithm which encodes the characters in a string based on their frequency.

## Key Steps
1. Frequency Counting
   - Counting the frequency of every character in the input
2. Constructing the Huffman Tree
   - Using a min-heap to construct a huffman tree in order to find and combine the least frequent nodes
3. Creating a code table
   - A code table will assign binary codes to the characters based on their position in the tree. i.e it assigns codes to the characters based on whether they are in the left child node or the right.
4. Compression
   - Encoding the input text using Huffman coding
5. Decompression
   - Decoding the compressed data using the code table



from restaurantData import types, restaurant_data as restaurants

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.isEndOfWord = False

    def add_child(self, letter):
        self.children[letter] = TrieNode(letter) #child is stored as key, value pair. Letter is key and node is value

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.add_child(letter)
            current_node = current_node.children[letter]
        current_node.isEndOfWord = True

    def search_by_prefix(self, prefix):
        #traverse through the trie to the node representing the prefix's last letter
        current_node = self.root
        for letter in prefix:
            if letter not in current_node.children:
                return "No match"
            current_node = current_node.children[letter]

        #Search for all the word under the current_node
        return self.depth_first_search(current_node, prefix)

    def depth_first_search(self, current_node, prefix):
        result = []
        #If current_node is end of a word, then prefix is already a word
        if current_node.isEndOfWord:
            result.append(prefix)
        
        #Base case for recursive calls: if current_node is a leaf
        if not current_node.children:
            return result
        #Recursivly call depth_first_search on all children nodes with new prefix
        for child, child_node in current_node.children.items():
            result += self.depth_first_search(child_node, prefix + child)
        return result
            

typesTrie = Trie()
for type in types:
    typesTrie.insert(type)

print(typesTrie.search_by_prefix("c"))
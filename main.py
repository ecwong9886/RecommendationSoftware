from restaurantData import types as restaurant_types, restaurant_data as restaurants

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

    #child is stored as key, value pair. Letter as key and node as value
    def add_child(self, letter):
        self.children[letter] = TrieNode() 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for letter in word:
            if letter not in current_node.children:
                current_node.add_child(letter)
            current_node = current_node.children[letter]
        current_node.isEndOfWord = True

    def search_by_prefix(self, prefix):
        #traverse through the trie to find the node representing the prefix's last letter
        current_node = self.root
        for letter in prefix:
            if letter not in current_node.children:
                return []
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
            
#Create the trie
restaurant_type_trie = Trie()
for type in restaurant_types:
    restaurant_type_trie.insert(type)


#Main body
while True:
    
    while True:
        print("\nWhat type of food would you like to eat?")
        print("Type the beginning of that food type\n")
        user_input = input().lower()
        food_types = restaurant_type_trie.search_by_prefix(user_input)
        if len(food_types) == 0:
            print("\nSorry. We coundn't find any restaurant type with that beginning.")
            continue
        if len(food_types) == 1:
            break
        print("\nYour choices are:\n")
        for type in food_types:
            print(type.capitalize())

    user_input = input(f"\nDo you want to look at {food_types[0].capitalize()} restaurant? (y/n)\n\n").lower()
    if user_input != "y":
        continue
    print(f"\nThe {food_types[0]} restaurants in SOHO are...\n")

    for restaurant in restaurants:
        if restaurant[0] == food_types[0]:
            print(f"--------------------")
            print(f"\nName: {restaurant[1]}")
            print(f"Price: {restaurant[2]}/5")
            print(f"Rating: {restaurant[3]}/5")
            print(f"Address: {restaurant[4]}\n")
  
    print()
    user_input = input("Would you like to find more restaurant? (y/n)").lower()
    if user_input != "y":
        break
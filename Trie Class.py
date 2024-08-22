class TrieNode:
    def __init__(self, char):
        self.char = char
        self.counter = 0
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.counter += 1

    def report(self, node, prefix):
        words = []
        if node.counter > 0:
            words.append((prefix, node.counter))
        for child in node.children.values():
            words.extend(self.report(child, prefix + child.char))
        return words

    def query(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        return self.report(node, prefix)



# Test the Trie class
trie = Trie()
trie.insert("apple")
trie.insert("applet")
trie.insert("apples")
trie.insert("apply")

assert trie.query("appl") == [('apple', 1), ('applet', 1), ('apples', 1), ('apply', 1)]
assert trie.query("apple") == [("apple", 1), ("applet", 1), ("apples", 1)]
assert trie.query("app") == [("apple", 1), ("applet", 1), ("apples", 1), ("apply", 1)]
        
    
from collections import deque

class WordDictionary:
    def __init__(self):
        self.root = {alpha: {} for alpha in string.ascii_lowercase}

    def addWord(self, word: str) -> None:
        
        node = self.root
        for char in word:
            node[char] = node.get(char, {})
            node = node[char]
        node["val"] = word

    def addChildren(self, curr_queue, char_match, add_all = False):
        curr_level_nodes = len(curr_queue)
        for _ in range(curr_level_nodes):
            node = curr_queue.popleft()
            for child in node:
                if child != "val" and add_all or (char_match == child):
                    curr_queue.append(node[child])
        return curr_queue
    
    def search(self, word: str) -> bool:
        queue = deque([self.root])
        for char in word:
            queue = self.addChildren(queue, char, char == '.')
            
        for node in queue:
            if "val" in node:
                return True
        return False
                
            
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

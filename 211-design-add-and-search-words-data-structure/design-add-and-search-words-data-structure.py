class trie:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root= trie()

    def addWord(self, word: str) -> None:
        node=self.root
        for w in word:
            if w not in node.children:
                node.children[w]=trie()
            node=node.children[w]
        node.end=True

        

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i==len(word):
                return node.end
            char=word[i]
            if char==".":
                for c in node.children.values():
                    if dfs(i+1,c):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(i+1,node.children[char])
        return dfs(0,self.root)
                
    


        
        

            
        

class FileSystem:

    def __init__(self):
        self.directories = defaultdict(set)
        self.files = {}

    def ls(self, path: str) -> List[str]:
        
        if path in self.files:
            return [self.files[path][1]]
        
        return sorted(self.directories[path])
        
        
    def mkdir(self, path: str) -> None:
        
        components = path.split("/")[1:]
        subpaths = "/"
        for c in components:
            if c not in self.directories[subpaths]:
                self.directories[subpaths].add(c)
            subpaths = (subpaths + "/" if subpaths[-1] != "/" else subpaths) + c
        
    def addContentToFile(self, filePath: str, content: str) -> None:
        
        last_split = filePath.rindex("/")
        directory = filePath[:last_split] if last_split > 0 else "/"
        fileName = filePath[last_split + 1:]
        if filePath not in self.files:
            if fileName not in self.directories:
                self.directories[directory].add(fileName)
            self.files[filePath] = [content, fileName]
        else:
            self.files[filePath][0] += content
            
    def readContentFromFile(self, filePath: str) -> str:
        
        return self.files[filePath][0]

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)

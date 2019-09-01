class FileSystem:

    def __init__(self):
        self.d = {"/": 0,
                  "": -1}

    def create(self, path: str, value: int) -> bool:
        if len(path) <= 1:
            return False

        plst = path.split("/")
        if "/".join(plst[:-1]) in self.d.keys():
            self.d[path] = value
            return True
        return False

    def get(self, path: str) -> int:
        if len(path) <= 1:
            return -1
        v = self.d.get(path)
        if v:
            return v
        return -1

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.create(path,value)
# param_2 = obj.get(path)
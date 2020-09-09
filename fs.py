
# Enter your code here. Read input from STDIN. Print output to STDOUT
# mkdir(path:string)
# write_file(path:string, data:string)
# read_file(path:string) -> string

# write_file '/foo/bar.txt' /foo doesn't exist => raise error

#       / root
# /foo          /bar
# /foo/bar      /bar/bar  
import typing
class inode:
    def __init__(self, path, isDir = True, children = dict(), data= None):
        self.path = path
        # path -> inode
        self.children = children
        self.data = data
        self.isDir = isDir
class fs:
    root = None
    def __init__(self):
        if fs.root == None:
            fs.root = inode('/', isDir = True )
    
    def dfs_search(self, node, path):
        # node = fs.root 
        if not node:
            return None
        if node.path == path:
            return node
        
        path_len = len(node.path)
        # path == /foo/bar
        # node.path =  /foo
        if node.path != path[0:path_len]:
            return None
        
        child_node = node.children[path[0:path_len]]
        return self.dfs_search(child_node)

            
    def find(self, path:str):
        node = self.dfs_search(fs.root, path)
        if node: 
            return node
        return None
    
    def create_idnoe(self, path:str, isDir = True, ):
        node = self.find(path)
        if node:
            return node 
        last_slash_id = 0
        for i in range(len(path)):
            if path[i] == '/':
                last_slash_id = i
        
        parent_path = path.find(path[:last_slash_id+1])
        parent = self.find(parent_path)
        if not parent:
            return None
        new_node = inode(path, isDir)
        parent.children[path] = new_node
        return new_node
            
    def mkdir(self, path:str):
        new_node = self.create_idnoe(path, isDir = True)
        return new_node
    def write(self, path:str, data):
        # this function create a new file if it does not exist
        node = self.create_idnoe(path, isDir = True)
        node.data = data
        
    def read(self, path:str):        
        node = self.find(path)
        if not node:
            return None
        return node.data 
        

my_fs = fs()
my_fs.mkdir("/foo")
my_fs.mkdir("/foo/bar")

my_fs.write("/foo/file.txt", "data")
        
assert(my_fs.read("/foo/file.txt"),  "data")


        

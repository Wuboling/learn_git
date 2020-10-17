class Node(Object):
    def __init__(self,item):
        self.item = item
        self.lchild = None
        self.rchild = None
class tree(Object):
    def __init__(self,node = None):
        self.root = node
    def add(self,item):
        if self.root is None:
            self.root = Node(item)
        else:
            queue = []
            queue.append(self.root)
            while len(queue)>0:
                node = queue.pop(0)
                if not node.lchild:
                    node.lchild = Node(item)
                    return
                else:
                    queue.append(node.lchild)
                if not node.rchild:
                    node.rchild = Node(item)
                    return
                else:
                    queue.append(rchild)

    def breadth_travel(self):
        if self.root is Node:
            return
        else:
            queue = []
            queue.append(self.root)
            while len(queue)>0:
                node = queue.pop(0)
                print(node.item,end="   ")
                if node.lchild:
                    queue.append(node.lchild)
                if node.rchild:
                    queue.append(node.rchild)

    def preorder_travel(self,node):
        if node:
            self.preorder_travel(node.rchild)
            print(node.item, end="  ")
            self.preorder_travel(node.lchild)
            return
        else:
            return





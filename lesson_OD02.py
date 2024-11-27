print("Стэк")

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

stack = Stack()

print(stack.is_empty())

stack.push(5)
stack.push(25)
stack.push(50)
stack.push(125)

print(stack.is_empty())

print(stack.peek())

print()
print("Очередь")

class Queue:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def enqueue(self, item):
       self.items.insert(0, item)

   def dequeue(self):
       return self.items.pop()

   def size(self):
       return len(self.items)

queue = Queue()

print(queue.is_empty())

queue.enqueue("Никита")
queue.enqueue("Максим")
queue.enqueue("Марина")
queue.enqueue("Андрей")
queue.enqueue("Нина")

print(queue.is_empty())

print(queue.size())

print(queue.dequeue())

print(queue.size())

print()
print("Дерево")

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

root = Node(50)

root = insert(root, 20)
root = insert(root, 65)
root = insert(root, 10)
root = insert(root, 30)
root = insert(root, 60)
root = insert(root, 80)
root = insert(root, 90)

print()
print("Графы")

class Graph:
   def __init__(self):
       self.graph = {}

   def add_edge(self, u, v):
       if u not in self.graph:
           self.graph[u] = []
       self.graph[u].append(v)

   def print_graph(self):
       for node in self.graph:
           print(node, "->", " -> ".join(map(str, self.graph[node])))

g = Graph()

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('E', 'F')
g.add_edge('F', 'G')

g.print_graph()
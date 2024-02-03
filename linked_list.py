class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list 
    """
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "<Node data: %s>" % self.data
    
class LinkedList:
        
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
        
    def size(self):
        """
        Returns the number of elements in the list
        Takes 0(n) time
        """
        current = self.head
        count = 0
        
        while current:
            count += 1
            current = current.next_node
            
        return count
            
    def  add(self, data):
        """"
        adds new node containing data at the end of the list"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self, key):
        """"Search for the first node containing data that matches the key
        Return the nide if not found
        
        takes O(n) time
        """
        current = self.head
        
        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
    
    def __repr__(self):
        """"
        Return a string representation of the list
        Takes O(n) time
        """
        
        nodes =[]
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
                
            current = current.next_node
        return '-> '.join(nodes)

l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
n = l.search(1)
print(n)
print(l)
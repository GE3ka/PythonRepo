class SList:
        def __init__(self):
            self.head = None
        def add_to_front(self, val):
            new_node = SLNode(val)
            current_head = self.head 
            new_node.next = current_head
            self.head = new_node
            return self
        def print_values(self):
            runner = self.head
            while (runner != None):
                print(runner.value)
                runner = runner.next 	# set the runner to its neighbor
            return self	 
        def add_to_back(self, val):
            if self.head == None:	# if the list is empty
                self.add_to_front(val)# run the add_to_front method
                return self	
            new_node = SLNode(val)
            runner = self.head
            while (runner.next != None):
                runner = runner.next
            runner.next = new_node	# increment the runner to the next node in the list
            return self       
        def remove_from_front(self):
            print (self.head)
            print(self.next)     

class SLNode:
        def __init__(self, val):
            self.value = val
            self.next = None   

my_list = SList()	# create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").remove_from_front().print_values()
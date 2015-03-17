#Task 3.1
def print_opt():
    print('''1. Add an item
2. Traverse the linked list of used nodes and output the data values
3. Output all pointers and data values
5. exit''')



#Task 3.2
class ListNode:
    def __init__(self, data, pointer):
        self.PointerValue = pointer
        self.DataValue = data

class LinkedList:
    def __init__(self):
        self.Start = 0
        self.NextFree = 0
        self.Node = [ListNode('', i) for i in range(1,30)]
        self.Node.append(ListNode('', None))
        print('Init done')

    def IsEmpty(self):
        if self.Start == 0:
            return True
        else:
            return False
    def AddNode(self):
        NewItem = input('New item to place into linked list: ')
        self.Node[self.NextFree].DataValue = NewItem
        if self.Start == 0:
            self.Start = self.NextFree
            Temp = self.Node[self.NextFree].PointerValue
            self.Node[self.NextFree].PointerValue = 0
            self.NextFree = Temp
        else:
            #traverse the list starting at the start to find the position at which to insert
            #the new item
            Temp = self.Node[self.NextFree].PointerValue
            if NewItem < self.Node[self.Start].DataValue:
                #new item will be the start of the list
                self.Node[NextFree].PointerValue = self.Start
                self.Start = self.NextFree
                self.NextFree = Temp
            else:
                #the new item is not at the start of the list
                Previous = 0
                Current = self.Start
                Found = False
                while Found == False or current == 0: 
                    if NewItem <= self.Node[Current].DataValue:
                        self.Node[Previous].PointerValue = self.NextFree
                        self.Node[self.NextFree].PointerValue = Current
                        NextFree = Temp
                        Found = True
                    else:
                        Previous = Current
                        Current = Node[Current].PointerValue
                if Current == 0:
                    self.Node[Previous].PointerValue = self.NextFree
                    self.Node[self.NextFree].PointerValue = 0
                    self.NextFree = Temp
                
                    
            
    def DisplayLinkedList(self):
        current_node = self.Node[self.Start]
        while current_node.PointerValue != None:
            print('Data value: ', current_node.DataValue)
            print('Pointer value: ', current_node.PointerValue)
            current_node = self.Node[current_node.PointerValue]
        #print the last value
        print('Data value: ', current_node.DataValue)
        print('Pointer value: ', current_node.PointerValue)
        
        
        

user_input = 'pass'
l = LinkedList()
while user_input != '5':
    print_opt()
    user_input = input('Choose an option: ')
    if user_input == '1':
        l.AddNode()
    elif user_input == '2':
        l.Traversal()
    elif user_input == '3':
        l.DisplayLinkedList()

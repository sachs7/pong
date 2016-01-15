    def insert(self,head,data): 
        #Complete this method
        if head == None:
            self.head = data
            print(self.head, end=" ")
        else:
            tmp = head
            while tmp.next != None:
                tmp = tmp.next
            tmp.data = data
            print(self.head, end=" ")

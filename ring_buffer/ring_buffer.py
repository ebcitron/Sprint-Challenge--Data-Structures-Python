from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #If self.storage.length is at capacity:
        if self.storage.length == self.capacity:
            if self.current is None:
                self.current = self.storage.tail
            self.current.value = item
            if self.current.prev:
                self.current = self.current.prev
            else:
                self.current = self.storage.tail

    
        else:
             self.storage.add_to_head(item)
        


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.tail
        while current:
            if current.value is not None:
                list_buffer_contents.append(current.value)
            current = current.prev
        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass

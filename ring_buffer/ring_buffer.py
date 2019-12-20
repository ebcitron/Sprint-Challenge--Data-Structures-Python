from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #If self.storage.length is at capacity:
            #if self.currentitem = none: set it as the tail of self.storage
                 #self.current.value = item.value
            #if self.current.previous:

        #else self.storage.add_to_head(item)
        


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
 
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

from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #If storage is empty, add item as head and set as current.
        if len(self.storage) == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        #If storage is not at capacity, add to tail and set tail as current
        elif len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        #If the current node is the last node, you reconsider the head node as oldest, remove it and add the new item in its place, set it to current
        elif self.current == self.storage.tail:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
        #If self.storage.length is at capacity, insert item after current,  adjust storage length, set new item as current. 
        if self.storage.length == self.capacity:
            self.current.insert_after(item)
            self.storage.length += 1
            self.current = self.current.next
            self.storage.delete(self.current.next)



            #if self.storage.length == self.capacity:
            # #Keep track of where the most current node is, which will be the tail
            # #If its empty, you may set its value  == to item
            # if self.current is None:
            #     self.current = self.storage.tail
            # self.current.value = item
            # #If it has any previous nodes, set the previous one up as current
            # if self.current.prev:
            #     self.current = self.current.prev
            # else:
            #     self.current = self.storage.tail


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current:
            if current.value is not None:
                list_buffer_contents.append(current.value)
            current = current.next
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

class RingBuffer:
    def __init__(self, capacity):
        # Set the max capacity
        self.capacity = capacity
        # create a list and grow list to capacity
        self.data = [None]*capacity
        # To track current item
        self.current = 0

    def append(self, item):
        # check current against capacity 
        if self.current < self.capacity:
            # remove the oldest element using the current index
            self.data.pop(self.current)
            # insert the new item at the current index
            self.data.insert(self.current, item)
            # add 1 to the current index
            self.current += 1

            # check if current is equal to capacity
            if self.current == self.capacity:
                # reset current to 0
                self.current = 0

    def get(self):
        # define a list to store the not NONE values
        get_list = []
        # loop over the self.data list 
        for n in self.data:
            # if the item in the list doesn't equal None
            if n != None:
                # append it to the list
                get_list.append(n)
        # return the list
        return get_list   
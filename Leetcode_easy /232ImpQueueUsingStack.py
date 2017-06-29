'''
implement Queue using Stacks

'''

class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.data:
            self.data.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        if self.data:
                    return self.data[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.data:
            return False
        else:
            return True
        
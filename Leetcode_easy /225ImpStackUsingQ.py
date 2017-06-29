
'''
mplement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
'''

class Stack(object):
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
            self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if self.data:
            return False
        else:
            return True
        
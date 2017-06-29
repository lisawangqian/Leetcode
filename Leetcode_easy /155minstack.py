class MinStack(object):
    def __init__(self):
        """
            initialize your data structure here.
            """
        self.data = []
        self.datamin = []
    
    def push(self, x):
        """
            :type x: int
            :rtype: nothing
            """
        self.data.append(x)
        if not self.datamin:
            self.datamin.append(x)
        else:
            if x <= self.datamin[-1]:
                self.datamin.append(x)


def pop(self):
    """
        :rtype: nothing
        """
            if self.data:
            tem = self.data.pop()
                if self.datamin and (tem == self.datamin[-1]):
                    self.datamin.pop()


def top(self):
    """
        :rtype: int
        """
            if self.data:
            return self.data[-1]
        
        def getMin(self):
        """
            :rtype: int
            """
        if self.datamin:
            return self.datamin[-1]

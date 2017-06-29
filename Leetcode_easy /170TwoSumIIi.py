'''
Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.
'''


class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.table = {}

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        if number in self.table:
            self.table[number] +=1
        else:
            self.table[number] = 1
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for (key, val) in self.table.iteritems():
            if (value - key) in self.table:
                if value != 2*key:
                    return True
                elif (value == 2 * key) and val >=2:
                    return True
        return False
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)
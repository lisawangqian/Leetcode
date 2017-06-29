class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dic = {}
        self.dicSame = {}
        for s in dictionary:
            if len(s) <= 2:
                abb = s
            else:
                abb = s[0] + str(len(s)-2) + s[-1]
            if not (s in self.dicSame):
                self.dicSame[s] = 1
                if abb in self.dic:
                    self.dic[abb] +=1
                else:
                    self.dic[abb] = 1
            
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) <= 2:
            abb = word
        else:
            abb = word[0] + str(len(word)-2) + word[-1]
            
        if not (abb in self.dic):
            return True
        elif self.dic[abb] == 1 and (word in self.dicSame):
            return True
        else:
            return False
        
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord") vwa.isUnique("word")
# vwa.isUnique("anotherWord")
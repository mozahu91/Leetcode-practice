def repeatedSubstringPattern(str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False
            
        ss = (str + str)[1:-1]
        if str in ss:
            return True
        else:
            return False

from itertools import combinations
class PasswordGen:
    def __init__(self):
        self.year : str = ""
        self.initials : str = ""
        self.postFixs : str = "";
        self.characterSet : list[str] = []
        
    def setYear(self,year : str):
        self.year = year
    def setInitials(self,initials: str):
        self.initials = initials
    def setPostFixs(self,postFixs : str):
        self.postFixs = postFixs;
    def setCharacterSet(self,characters : str):
        self.characterSet = list(characters)
    def generateList(self,outputFile):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        with open(outputFile,"w") as file:
            listPassKeys = self._getFirstPasswordSuggestion()
            for i in range(len(listPassKeys)):
                file.write(listPassKeys[i]+"\n")
            pass
        pass
    def _getFirstPasswordSuggestion(self):
        array : list[str] = [self.year,self.initials,self.postFixs,*self.characterSet]
        possiblePasswords : list[str] = []
        for r in range(1, len(array) + 1):
            for c in combinations(array, r):
        # Add the original combination
                possiblePasswords.append("".join(map(str, c)))
        # Add the reversed combination if it's not the same as the original
                reversed_c = tuple(reversed(c))
                if reversed_c != c:
                    possiblePasswords.append("".join(map(str, reversed_c)))
        return possiblePasswords


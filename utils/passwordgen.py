from itertools import combinations
def lowercase_first_letter(input_string):
    if not input_string:  # Handle empty string case
        return input_string
    return input_string[0].lower() + input_string[1:]
class PasswordGen:
    def __init__(self):
        self.year : str = ""
        self.initials : list[str] = ""
        self.characterSet : list[str] = []
    def setYear(self,year : str):
        self.year = year
    def setInitials(self,initials: str):
        init0 = map( lambda x : x.capitalize(),initials.split(' '))
        init1 = map( lambda x : lowercase_first_letter(x),initials.split(' '))
        self.initials = [*init0,*init1]
    def setCharacterSet(self,characters : str):
        self.characterSet = list(characters)
    def generateList(self,outputFile):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        with open(outputFile,"w") as file:
            listPassKeys = self._getFirstPasswordSuggestion()
            for i in range(len(listPassKeys)):
                file.write(listPassKeys[i]+"\n")
            file.close()
            pass
        pass
    def _getFirstPasswordSuggestion(self):
        array : list[str] = [self.year,*self.initials,*self.characterSet]
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

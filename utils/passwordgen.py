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

            pass
        pass
    def _getFirstPasswordSuggestion(self):
        array : list[str] = [self.year,self.initials,self.postFixs,*self.characterSet]
        
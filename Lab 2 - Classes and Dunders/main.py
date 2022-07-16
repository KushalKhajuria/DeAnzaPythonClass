class MorseCode:
    def __init__(self, character, morseCode): #initializing
        self.character = character
        self.morseCode = morseCode
    def __str__(self): #printing
        str = self.character + ": " + self.morsecode
        return str
    def __eq__(self, other): #for supporting searching
        return self.character == other.character
    def __lt__(self, other): #for supporting sorting
        return self.character < other.character

class MorseCodeCollection:
    def __init__(self): #initializing 
        self.morseCodeDict = {}
    
    def __str__(self): #printing
        str = ""
        for morseCode in morseCodeDict:
            str += morseCode.__str__ + "\n"
        return str
    def __iter__(self): #sequence iterator for iterating through MorseCodeCollection's MorseCode objects
        self.iterator = iter(morseCodeDict)
        return self.iterator
    def __next__(self):
        try:
            return next(self.iterator)
        except IndexError:
            raise StopIteration()
    def __getitem__(self, key): #for getting particular morse code
        return self.morseCodeDict[key]
    def __setitem__(self, key, value): #for adding to the morse code list
        self.morseCodeDict[key] = value
    def sort(self):
        return sorted(self.morseCodeDict)


file = open(MorseCode.csv)
morse = MorseCodeCollection()

for line in file:
    line = line.split(",")
    morseObject = MorseCode(line[0], line[1])
    morse[morseObject.character] = morseObject.morseCode

print(morse)

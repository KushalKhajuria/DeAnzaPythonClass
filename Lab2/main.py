class MorseCode:
    def __init__(self, character, morseCode): #initializing
        self.character = character
        self.morseCode = morseCode
    def __str__(self): #printing
        str = self.character + ": " + self.morseCode
        return str
    def __eq__(self, other): #for supporting searching
        print(self.character + "__eq__" + other.character)
        return self.character == other.character
    def __lt__(self, other): #for supporting sorting
        print(self.character + "__lt__" + other.character)
        return self.character < other.character

class MorseCodeCollection:
    def __init__(self): #initializing 
        self.morseCodeDict = {}
    
    def __str__(self): #printing
        str = ""
        for morseCode in self.morseCodeDict:
            str += self.morseCodeDict[morseCode].__str__() + "\n"
        return str
    def __iter__(self): #sequence iterator for iterating through MorseCode objects
        print("__iter__")
        self.counter = 0
        return self
    def __next__(self):
        print("__next__")
        try:
            self.iterator = self.morseCodeDict[self.counter]
        except KeyError:
            raise StopIteration()
        self.counter += 1
        return self.iterator
    def __getitem__(self, key): #for getting particular morse code
        return self.morseCodeDict[key]
    def __setitem__(self, key, value): #for adding to the morse code list
        self.morseCodeDict[key] = value
    def sort(self):
        valuesIterator = iter(sorted(self.morseCodeDict.values()))
        for key in self.morseCodeDict:
            self.morseCodeDict[key] = next(valuesIterator)
    def search(self, value):
        if value in self.morseCodeDict.values():
            print("Found: " + value.character)
    def reader (self, csvfile):
        file = open(csvfile)
        key = 0
        for line in file:
            line = line.rstrip()
            line = line.split(",")
            morseObject = MorseCode(line[0], line[1])
            self.morseCodeDict[key] = morseObject
            key += 1
#initializing
morse = MorseCodeCollection()
morse.reader("MorseCode.csv")
#printing
print("Lab2/Morse Code:")
print(morse)
#sorting
print("\n\n\n\n\nSorting list:")
morse.sort()
print(morse)
#searching
print("\n\n\n\n\nLooking for 'K' in Morse Code:")
find = MorseCode('K', "-.-")
morse.search(find)
#iterating
print("\n\n\n\n\nIterating through Morse Code:")
for m in morse:
    print(m)
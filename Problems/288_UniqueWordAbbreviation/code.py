from typing import List, Set

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.dictionary: dict[str, Set] = {}

        for d in dictionary:
            abbr = self.makeWordAbbreviation(d)
            if abbr in self.dictionary:
                self.dictionary[abbr].add(d)
            else:
                self.dictionary[abbr] = {d}

        print(self.dictionary)
    
    def makeWordAbbreviation(self, word: str) -> str:
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]
        

    def isUnique(self, word: str) -> bool:
        abbr = self.makeWordAbbreviation(word)
        if abbr not in self.dictionary: 
            return True
        else:
            if word in self.dictionary[abbr] and len(self.dictionary[abbr]) == 1:
                return True
            else:
                return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

def makeabbr(word: str) -> str:
    if len(word) <= 2:
        return word
    else:
        return word[0] + str(len(word) - 2) + word[-1]


print(makeabbr("internationalization"))
print(makeabbr("maker"))
print(makeabbr("cart"))
print(makeabbr("you"))
print(makeabbr("a"))
print(makeabbr("is"))

v = ValidWordAbbr(["deer", "door", "cake", "card"])
print(v.isUnique("dear"))
print(v.isUnique("cart"))
print(v.isUnique("cane"))
print(v.isUnique("make"))
print(v.isUnique("cake"))
print("-------------")
print(v.isUnique("dear"))
print(v.isUnique("door"))
print(v.isUnique("cart"))
print(v.isUnique("cake"))
print(v.isUnique("care"))
from typing import List

def addOperators(num: str, target: int) -> List[str]:
    l: int = len(num)
    p1: int = 0
    p2: int = 1
    tokens: [str] = ['+', '-', '*']
    allTokenPaths: [str] = []
    allShuffles: [str] = []
    operatorTokens: [str] = []
    currentTokens: [str] = []
    currentAnswer: int = 0

    def getAPerm(currentString: str, tokens: [str], comboLength: int):
        if len(currentString) == comboLength: # you're done?
            allTokenPaths.append(currentString)
            return
        
        for i in range(len(tokens)):
            getAPerm(currentString + tokens[i], tokens, comboLength)

    s = "+-*"
    l = len(num) - 1
    c = getAPerm("", s, l)

    def shuffleNumbersWithTokens(numbers: [str], tokenPaths: [str]):
        currentShuffle: str = ""

        for t in tokenPaths:
            for i in range(len(numbers)):
                currentShuffle += numbers[i]
                if i < len(t): 
                    currentShuffle += t[i]
                print(currentShuffle)
            
            allShuffles.append(currentShuffle)
            currentShuffle = ""

    # print(shuffleNumbersWithTokens(num, allTokenPaths))
    shuffleNumbersWithTokens(num, allTokenPaths)
    print(allShuffles)

    validShuffles: [str] = []
    currentAnswer: int = 0

    # two pointer with allShuffles?
    for s in allShuffles:
        p1 = 0
        p2 = 1
        currentAnswer = 0
        print("Working on: {}".format(s))
        while p1 < p2 and p2 < len(s):
            print("P1: {} | P2: {}".format(p1, p2))
            if p1 == 0:
                currentAnswer += int(s[p1])
                print("Answer is now: {}".format(currentAnswer))
                p1 += 1
                p2 += 1
            else:
                print("Do something with... {} and {}".format(s[p1], s[p2]))
                match s[p1]:
                    case "+":
                        currentAnswer += int(s[p2])
                        print("Answer is now: {}".format(currentAnswer))
                    case "=":
                        currentAnswer -= int(s[p2])
                        print("Answer is now: {}".format(currentAnswer))
                    case "*":
                        currentAnswer = currentAnswer * int(s[p2])
                        print("Answer is now: {}".format(currentAnswer))

                p1 += 2
                p2 += 2
        
        if currentAnswer == target:
            print("Match found ({}).".format(s))
            validShuffles.append(s)

    print("VALID SHUFFLES:")
    print(validShuffles)
            
                
        

    return []


#addOperators('3456237490', 9191)
#addOperators('232', 8)
#addOperators('123', 6)

sh = ['2+3*2', '2*3+2']
for s in sh:
    print(s.split('*+-'))

def doOrderOfOps(numString: str) -> int:
    p1: int = 0
    p2: int = 1
    previousNumber = 0
    previousOp = ""
    previousAnswer = 0
    currentAnswer = 0

    while p1 < len(numString):
        # two pointers, always do the math but prioritize multiplication
        previousAnswer = currentAnswer
        print("Previous answer: {}".format(previousAnswer))
        if numString[p1].isdigit():
            print("processing this: {}".format(numString[p1]))
            match previousOp:
                case "+":
                    currentAnswer += int(numString[p1])
                case "-":
                    currentAnswer -= int(numString[p1])
                case "*":
                    currentAnswer = currentAnswer * int(numString[p1])
            previousNumber = int(numString[p1])
        else:
            print("Setting previous operator ({})".format(numString[p1]))
            previousOp = numString[p1]
        
        p1 += 1

doOrderOfOps("1+2*3")

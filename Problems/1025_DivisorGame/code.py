class Solution:
    def divisorGame(self, n: int) -> bool:

        dp = [0] * (n + 1)
        print(dp)
        maxNumber = n
        i = n - 1
        aliceTurn = True

        # for i in range(maxNumber - 1, 0, -1):
        while i > 0:
            if maxNumber % i == 0:
                print(f"TRUE {'ALICE' if aliceTurn else 'Bob'} Current: {i}, max: {maxNumber}")
                maxNumber -= i
                if aliceTurn == True:
                    aliceTurn = False
                else:
                    aliceTurn = True

                i = maxNumber
                # maxNumber = maxNumber - i
            else:
                print(f"FALSE {'ALICE' if aliceTurn else 'Bob'} Current: {i}, max: {maxNumber}")

            i -= 1


        if aliceTurn == True:
            return False
        else:
            return True
    
s = Solution()
print(s.divisorGame(2)) # true
print(s.divisorGame(3)) # false
print(s.divisorGame(4))
print(s.divisorGame(100))

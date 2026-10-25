## A Perfect Square is an int that equals some int multiplied by itself
## e.g. 1 = 1*1, 4 = 2*2, 9 = 3*3, 16 = 4*4
## check whether n is a perfect square, return True if it is or False if it isn't

def isPerfectSquare(n):
## please fill in your codes below, n is the input number to check
    if n>=0:
        for i in range(0,n//2+2):
            if i * i == n:
                return True
        
        return False
    else:
        return False

        

print(isPerfectSquare(16))   # True
print(isPerfectSquare(15))   # False
print(isPerfectSquare(0))    # True
print(isPerfectSquare(1))    # True
print(isPerfectSquare(-4))   # False

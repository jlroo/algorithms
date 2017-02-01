####### Newton Method
global t;
import math
t = 10**6

# Logarithm nlog(n)
f = lambda n:n*math.log(n,2)

# Factorial n!
f = lambda n:1 if n==0 else n*f(n-1)

# Exponential 2^n
f = lambda n:math.pow(2,n)

# Newtons Method 
def newtons(f):
    cnt = 1
    N = f(cnt)
    while N-t<0 and N<t:
        cnt+=1
        N = f(cnt)
    return cnt-1

newtons(f)
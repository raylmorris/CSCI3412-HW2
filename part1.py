import time
import numpy as np
import math
def fixedIter(func, a0, eps):
    a1 = func(a0)
    #print(a1, a0)
    if a1 - a0 < eps and a0 - a1 < eps:
        return a1
    return fixedIter(func, a1, eps)
def invFactorial(x,guess=1):
    if math.factorial(guess) > x: return guess - 1
    return invFactorial(x, guess+1)
np.set_printoptions(precision=1,suppress=False)
functions = [
    lambda t: 2**t, # t = np.log2(n)
    lambda t: t**2, # t = math.sqrt(n)
    lambda t: t, # t = n
    lambda t: fixedIter(lambda n: t/np.log2(n),t,0.5), # t = n*lg(n)
    lambda t: t**0.5, # t = n^2
    lambda t: t**(1/3), # t = n^3
    lambda t: np.log2(t), # t = 2^n
    lambda t: invFactorial(t) # t = n!
]
parameters = [
    1*1000000,
    1*60*1000000,
    1*60*60*1000000,
    1*60*60*24*1000000,
    1*60*60*24*30*1000000,
    1*60*60*24*365*1000000,
    1*60*60*24*365*100*1000000
]
results = np.zeros((len(functions),len(parameters)),dtype=int)
exception_results = [[0]*len(functions)]*len(parameters)
print(results)
for row in range(len(functions)):
    for column in range(len(parameters)):
        try:
            result = functions[row](parameters[column])
        except:
            result = np.inf
#        result = functions[row](float(parameters[column]))
        #print(result)
        try:
            results[row, column] = result
        except OverflowError:
            continue
            results[row, column] = -1 #2**32 - 1
            exception_results[row][column] = result
    #print(results[row,])
print(results)
print(exception_results)

#
#with open("Part1Output.html", "w") as f:
#    print("<table>","\t<tr>",sep="\n",file = f)
#    print(f.read())

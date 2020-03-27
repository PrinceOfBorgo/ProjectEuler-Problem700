N = 1504170715041707
M = 4503599627370517
min = N
sum = N

# Utility function to nicely format output in two columns.
def t_print(strings, lengths = []):
    lenStr = len(strings)
    lenLen = len(lengths)
    if lenLen < lenStr:
        lengths.extend(len(str(s)) for s in strings[lenLen:])
        
    print("".join(str(strings[i]).ljust(lengths[i]) for i in range(lenStr)))

    
t_print(["Eulercoin", "Sum"], [20])
print("-"*36)
t_print([min, sum], [20])
# Brute-force attack to find the first Eulercoins for the next attack. 
Nn = N
while Nn > 100000000:
    Nn = (Nn + N) % M
    if Nn < min:
        min = Nn
        sum += Nn
        t_print([min, sum], [20])

t_print(["","","<< end brute-force attack"], [20,18])        
t_print(["","","<< start tail analysis"], [20,18])

# Modular multiplicative inverse: used to find the inverse of N modulo M.
def modinv(a, n):
    t = 0
    newt = 1
    r = n
    newr = a

    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr

    if r > 1:
        return "a is not invertible"
    if t < 0:
        t = t + n
        
    return t

# Inverse of N modulo M.
invN = modinv(N, M)

# N * n = Nn (mod M) ---> n = Nn / N (mod M) = Nn * invN (mod M)
# We start from Nn = min (precalculated during brute-force stage).
n = (min * invN) % M 

# Dictionary with items (n: Nn) where Nn = N * n (mod M).
dict = {}
# Iterate descending from min to 0.
for Nn in range(min, 0, -1):
    # Find the new n (namely n1) from which Nn comes: Nn = N * n1 (mod M).
    n1 = (Nn * invN) % M
    
    # - If n1 > n, then the key-value pair (n1: Nn) is added to dict.
    # - Otherwise do nothing (we got through this step during brute-force
    #   stage).
    if n1 > n:
        dict[n1] = Nn

# Order dict by ascending keys and iterate.
dict = sorted(dict.items())
for n, Nn in dict:
    # If Nn < min, then we got Eulercoin: update min and add it to sum.
    if Nn < min:
        min = Nn
        sum += Nn
        t_print([min, sum], [20])
        # If Nn is 1, the only remaining Eulercoin is 0.
        if Nn == 1:
            t_print([0, sum], [20])
            break

print()
print("Solution: ", sum)

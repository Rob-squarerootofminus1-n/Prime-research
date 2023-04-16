import time

# initial list of primes, increased it as you want!
listP = [2, 3, 5]

def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        if i**2>n:
            return True
    return True

def is_prime_with_list(n):
    for elt in listP:
        if n%elt == 0: #not prime
            return False
        if elt**2>n: #yipee prime \(°u°)/
            return True
    return True

assert(is_prime_with_list(4)==False) #just to assure you the code works
assert(is_prime_with_list(11)==True) #same here

#your intervall of research
min = 7 
max = 1500

st = time.time()

k_min = min//6
k_max = max//6

for i in range(k_min, k_max+1):
    
    if is_prime_with_list(6*i+1)==True:
        listP.append(6*i+1)
    if is_prime_with_list(6*i+5)==True:
        listP.append(6*i+5)
print("Liste des nombre premiers :\n", listP)
print("Il y en a : ", len(listP))


#if you want to check the time needed to generate all of this
"""
et = time.time()
print('Temps nécessaire/Execution time:', et - st, 'secondes/seconds')
"""

#to save all the primes you discovered!
f=open("Nbr_prime.txt", "w")
for elt in listP:
    f.write(str(elt)+", ")
f.close() #then go find your file!

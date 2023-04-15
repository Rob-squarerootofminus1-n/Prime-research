import time

# liste initiale de nombre premiers
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
        if n%elt == 0: #nombre pas premier
            return False
        if elt**2>n:
            return True
    return True

assert(is_prime_with_list(4)==False)
assert(is_prime_with_list(11)==True)

min = 7 
max = 1500

st = time.time()
k_min = min//6
k_max = max//6

for i in range(k_min, k_max+1):
    #print("i=",i)
    if is_prime_with_list(6*i+1)==True:
        listP.append(6*i+1)
    if is_prime_with_list(6*i+5)==True:
        listP.append(6*i+5)
print("Liste des nombre premiers :\n", listP)
print("Il y en a : ", len(listP))
et = time.time()
print('Execution time:', et - st, 'seconds')

"""
st = time.time()
cpt = 0
for i in range(min, max+1):
    if is_prime(i)==True:
        #print(i)
        cpt = cpt +1
print("Il y en a :", cpt)
et = time.time()
print('Execution time:', et - st, 'seconds')
"""


f=open("Nbr prime.txt", "w")
for elt in listP:
    f.write(str(elt)+"\n")
f.close()
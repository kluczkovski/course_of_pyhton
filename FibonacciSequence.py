
# Fibonacci Sequence is 0, 1, 1, 2, 3, 5, 8, ...
# The first two terms are 0 and 1. All other terms are obtained by adding
# the preceding two terms. This means to say the nTh term is
#  the sum of (n-1)th and (n-2)th term.


nterms = input("Enter numers of terms: ")
nterms = int(nterms)

# first two term
n1 = 0
n2 = 1
count = 0
tn = 0

if nterms <=0 :
    print("Enter with positive number")
elif nterms == 1:
    print("Fibonacci sequence up to", nterms,":")
    print(n1)
elif nterms == 2:
    print("Fibonacci sequence up to", nterms, ":")
    print(n1)
else:
    print("Fibonacci sequence up to", nterms, ":")
    while (count < nterms):
        print(n1, end=", ")
        th = n1 + n2
        n1 = n2
        n2 = th
        count +=1







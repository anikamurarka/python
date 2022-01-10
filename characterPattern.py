# A
# BC
# CDE
# DEFG

n =int(input())
i =  1
while i<=n:
    j = 1
    while j<=i:
        print(chr(65+i+j-2), end='')
        j = j+1
    print()
    i=i+1

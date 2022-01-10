# E
# DE
# CDE
# BCDE
# ABCDE

n =int(input())
i =  1
while i<=n:
    j = 1
    while j<=i:
        print(chr(ord('A')-1+n-(i-j)), end='')
        j = j+1
    print()
    i=i+1

S=input()
li=S.split()
M=li[::-1]
if(len(S)<=10000000):
    for i in range(2):
        print(M[i], end = " ")
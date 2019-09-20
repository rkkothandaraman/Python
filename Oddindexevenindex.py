K=input()
O=''
E=''
for i in range(len(K)):
    if i%2==0:
        O=O+K[i]
    else:
        E=E+K[i]
print(O+" "+E)

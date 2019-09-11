A,B,C=map(int,input().split())
if((A and B and C) and (A<=100000 and B<=100000 and C<=100000)):
    if(A+B>=C or B+C>=A or A+C>=B):
        print("yes")
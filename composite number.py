#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     18-07-2019
# Copyright:   (c) User 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
count=0
comp=int(input())
if(comp>0):
    for i in range(1,comp):
         if(comp%i==0):
                count=count+1
    if(count>2):
         print("yes")
    else:
        print("no")
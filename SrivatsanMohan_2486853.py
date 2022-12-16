import numpy as np
import pandas as pd
import re # regex library to split strings
from random import choices # randomly choose letters
from itertools import combinations
import itertools

#global values to be used through all functions
global dvalues
dvalues=[]
global data
data={}
global dataf
dataf={}
global uvalues
uvalues=[]

# function to read file and remove all unwanted characters
def readfile():
    abbr =[]
    with open('1.txt') as f: # opening and reading file
        for lines in f:
            str = lines.strip().upper() # split the file into indiviual sentence
            y = str.replace("'","").replace('"', '') # remove apostrophe
            y = re.sub(r'[^\w\s]', ' ',y) # use regex to remove all non-alphabets and replace with space
            y=y.upper()  
        #print(y)
        #combcomp(y)    
            abbr.append(y) # change case to upper
    return abbr       

# save output
def outfile(z1):
        datafin={}
        
        for i in z1:
            tmpmin={}
            minsco=0
            c=0
            for j in z1[i].keys():
                tempsco=z1[i][j]
                c=c+1
                if tempsco<minsco or c==1:
                        minsco=tempsco
                        loc=j   
            if c>0:
                tmpmin[loc] = minsco
                datafin[i]=tmpmin

        with open('srivatsan_output_abbrev1.txt','w') as f:
                    for i in z1:
                            f.write(i + '\n') 
                            if i in datafin:
                                    for j in datafin[i].keys():
                                        f.write(j + '\n')
                            else:
                                    f.write('\n')

# function to score the values    
def score(x,y):
    # lower score better
    sloc=[]
    tloc=[]
    tscore = []
    sletter = x[1]
    tletter = x[2]
    z=len(y)
    #calculate the location of the letter
    sloc = [pos for pos, char in enumerate(y) if char == sletter]
    tloc = [pos for pos, char in enumerate(y) if char == tletter]
    for p in sloc:
        ssc=0
        if p == z-1 or y[p-1]==' ' or y[p+1] == ' ': 
            if sletter != 'e':
                ssc= ssc+5
            elif sletter == 'e':
                ssc= ssc+20
        elif p != 0 or p != z-1 or y[p-1]==' ' or y[p+1] == ' ':
            ssc = ssc+p+1
            if sletter == 'Q' or sletter =='Z':
                ssc = ssc+1
            elif sletter == 'J' or sletter =='X':
                ssc = ssc+3
            elif sletter == 'K':
                ssc = ssc+6
            elif sletter == 'F' or sletter =='H' or sletter =='V' or sletter =='W' or sletter =='Y'  :
                ssc = ssc+7  
            elif sletter == 'B' or sletter =='C' or sletter =='M' or sletter =='P' :
                ssc = ssc+8
            elif sletter == 'D' or sletter =='G':
                ssc = ssc+9
            elif sletter == 'L' or sletter =='N' or sletter =='R' or sletter =='S' or sletter =='T'  :
                ssc = ssc+15
            elif sletter == 'O' or sletter =='U':
                ssc = ssc+20
            elif sletter == 'A' or sletter =='I':
                ssc = ssc+25
            elif sletter == 'E' :
                ssc =ssc+35
        for q in tloc:
            tsc=0
            if q == z-1 or y[q-1]==' ' or y[q+1] == ' ': 
                if tletter != 'E':
                    tsc= tsc+5
                elif tletter == 'E':
                    tsc= tsc+20
            elif q != 0 or q != z-1 or y[q-1]==' ' or y[q+1] == ' ':
                tsc = tsc+q+1
                if tletter == 'Q' or tletter =='Z':
                    tsc = tsc+1
                elif tletter == 'J' or tletter =='X':
                    tsc = tsc+3
                elif tletter == 'K':
                    tsc = tsc+6
                elif tletter == 'F' or tletter =='H' or tletter =='V' or tletter =='W' or tletter =='Y'  :
                    tsc = tsc+7  
                elif tletter == 'B' or tletter =='C' or tletter =='M' or tletter =='P' :
                    tsc = tsc+8
                elif tletter == 'D' or tletter =='G':
                    tsc = tsc+9
                elif tletter == 'L' or tletter =='N' or tletter =='R' or tletter =='S' or tletter =='T'  :
                    tsc = tsc+15
                elif tletter == 'O' or tletter =='U':
                    tsc = tsc+20
                elif tletter == 'A' or tletter =='I':
                    tsc = tsc+25
                elif tletter == 'E' :
                    tsc =tsc+35
            tscore.append(ssc+tsc)
    cscore=min(tscore)
    
    return(cscore)

# function to calculate all the abreviations
def Abbfunc(x):
    #abb ={} #create dict for output
    #abb1 = [] # create list for output
    #print(x)
    for y in x:
        abb ={}
        #print(y)
        #print(y)
        y1 = y.replace(" ", "") #remove spaces
        #print(y1)
        var1 = [''.join(i) for i in combinations(y1[1:], r = 2)] # create all possible combinations of letters except first letter
        for x in var1:
            c=([y1[0] + x ]) # add first letter to the string     
            #print(c) 
            for i in range(len(c)):
                
            #print(x[i])
                #print(i)
                #print(c[i])
                if c[i] not in dvalues:
                    if c[i] not in uvalues:
                        uvalues.append(c[i])
                        #print(c[i])
                        sc=score(c[i],y)
                        abb[c[i]]=sc
                        #print(abb[c[i]])
                        #data[c[i]]=sc
                        #print(abb)
                        #print(data)
                    elif c[i] in uvalues:
                        uvalues.remove(c[i])
                        #abb.pop(c[i])
                        dvalues.append(c[i])
        #print(abb)
                #print(data)
        dataf[y]=abb
            #print(data)
            #abb1.append([y1[0] + x ]) # add first letter to the string
            
    for i in dataf:
        for j in dvalues:
            if j in dataf[i].keys():
                del dataf[i][j]
    #dataf = dict(zip(x,data))  
    
    return dataf 

# mainfunction to execute command
def main():
        str=readfile()
        z1 = Abbfunc(str)
        outfile(z1)

if __name__ == "__main__":
    main()
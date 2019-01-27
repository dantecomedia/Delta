#!/usr/bin/env python
import csv
import time
import math

tt=0
r=[]

seconds=time.time()
local_time=time.ctime(seconds)
r.append(local_time)
print(local_time, end="\n")

def writerfile(r):
    with open("Delt_time.csv","a") as csvFile:
        writer=csv.writer(csvFile)
        writer.writerow(r)
    csvFile.close()

def countdown(t):
    while(t>0):
        time.sleep(1)
        t=t-1
        print('Time left :',t,end="\r")


def start(r):
    b=int(input("Enter the intermedaite interval\n"))
    r.append("Interval time :")
    r.append(b)
    t_sub=int(input("Enter the time in min for each subject : "))
    r.append(t_sub)
    c=input("Enter the Subject\n").split()
    print("Subject : ",c)
    pr=map(int,input("Enter the respective priority: ").split())
    zz=zip(c,pr)
    zz=list(zz)
    sub_n=len(c)
    b=[]
    t=[]
    temp_tt=tt
    print("Calling automatic allocation system...\n")
    allocate(c,t_sub,b,r)

# ---------------------------------time allocation-----------------------------
def allocate(c,t_sub,b,r):
    time1=[]
    for i in c:
        print("Enter time allocation for the given subject :",i, end="\n")
        r.append(i)
        k=int(input("Enter the time in hours: "))
        time1.append(k)
        r.append(k)
        r.append(" \n")
    writerfile(r)
    scheduler(time1, c, t_sub, b)









# ---------------------------------scheduling---------------------------------
def scheduler(time1, c, t_sub, b):
    for i in c:
        j=0
        print("Time for subject :", i, end="")
        bar=math.ceil((time1[j]*60)/t_sub)
        for i in range(bar):
            print("Time Block %d for studying initatied \n"%i)
            countdown(t_sub*60)
            print("Time Block %d for release initatied \n"%i)
            countdown(b*60)
            print("Remaining the time Bar :",(bar-i), end="\n")
        j=j+1





# ----------------------------------------------command-----------------------------------------------
def main(tt=0):
    print("Commands : \r")
    print("1.start 2.Break  3.RESET 4.Save to file 5.Scheduler 6.end \n")
    z=input()
    if z=="break" or z=="2":
        print("Break Initatied....\n")
        tik=time.time()
        print("Press Key when return...\n")
        br=input()
        if isinstance(br,str):
            d=time.time() - tik
            print("TIME ADDED BACK TO ", d, end="\n")
            tt= tt + d
        main(0)
    elif z=="start" or z=="1" :
        start(r)
    elif z=="RESET" or z=="3":
        r.clear()
        main(0)
    elif z=='end' or z=="6":
        exit()
    elif z=="5":
        scheduler(time1, c, t_sub, b)
    elif z=="4":
        writerfile(r)
        print("Written to the file....\n")
    else:
        print("Invalid Response\n")
        main(0)




if __name__=="__main__":
    main(tt)

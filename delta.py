#! /usr/bin/python3



import csv
import time
import math
import getpass
from playsound import playsound



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
    

def countdown(mm):
    while mm>0:
        time.sleep(1)
        mm=mm-1
        print('Time left :',mm,end="\r")


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
        print("Time for subject :", i, end="\n")
        bar=math.ceil((time1[j]*60)/t_sub)
        print("-------------------------------",i,"--------------------------------\n")
        for k in range(1,bar):
            print("Time Block %d for STUDYING initatied \n"%k)
            playsound("/mnt/F8F8B8AFF8B86E0E/Delta Wing/Countdown 5 Seconds HD (NCI) {NOCOPYRIGHT INTRO}.mp3")
            countdown((t_sub*60)-5)
            print("Time Block %d for INTERVAL initatied \n"%k)
            playsound("/mnt/F8F8B8AFF8B86E0E/Delta Wing/Intro RAW 2 soft music 5 seconds (TEST).mp3")
            countdown((b*60)-5)
            print("Remaining time Bar :",(bar-k), end="\n")
        j=j+1
        print("-------------------------------xxx----------------------------------\n")
    print("ENTIRE SCHEDULE COMPLETED \n")
    run(0)





# ----------------------------------------------command-----------------------------------------------

def run(tt=0):
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
        run(0)
    elif z=="start" or z=="1" :
        start(r)
    elif z=="RESET" or z=="3":
        r.clear()
        run(0)
    elif z=='end' or z=="6":
        exit()
    elif z=="5":
        scheduler(time1, c, t_sub, b)
    elif z=="4":
        writerfile(r)
        print("Written to the file....\n")
        run(0)
    else:
        print("Invalid Response\n")
        run(0)

def main(tt=0):
    print("Enter PASSWORD to PROCEED\n")
    p=getpass.getpass(prompt="Enter Password: ")
    if p=="------":
        run(tt=0)
    else:
        main(tt=0)





if __name__=="__main__":
    main(tt)


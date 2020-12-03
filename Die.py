import random
import csv

frequency1=0
frequency2=0
frequency3=0
frequency4=0
frequency5=0
frequency6=0 
PercFreq1=0
PercFreq2=0 
PercFreq3=0 
PercFreq4=0 
PercFreq5=0 
PercFreq6=0  

def Die():
    global frequency1
    global frequency2
    global frequency3
    global frequency4
    global frequency5
    global frequency6 
    global PercFreq1
    global PercFreq2
    global PercFreq3 
    global PercFreq4 
    global PercFreq5 
    global PercFreq6  
      
    for i in range(1000):

        dice1 = random.randint(1,6)
        if dice1 == 1:  
            frequency1=frequency1 + 1
        elif dice1 == 2:
            frequency2=frequency2 + 1    
        elif dice1 == 3:
            frequency3=frequency3 + 1
        elif dice1 == 4:
            frequency4=frequency4 + 1    
        elif dice1 == 5:
            frequency5=frequency5 + 1   
        else:
            frequency6=frequency6 + 1
            

    PercFreq1=(frequency1/1000)* 100


    PercFreq2=(frequency2/1000)* 100

    PercFreq3=(frequency3/1000)* 100
    
    PercFreq4=(frequency4/1000)* 100

    PercFreq5=(frequency5/1000)* 100

    PercFreq6=(frequency6/1000)* 100

Die()    

with open('TableOutput.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Face', 'Frequency', '%Frequency',])
    writer.writerow([ 1, frequency1, PercFreq1,])
    writer.writerow([ 2, frequency2, PercFreq2,])
    writer.writerow([ 3, frequency3, PercFreq3,])
    writer.writerow([ 4, frequency4, PercFreq4,])
    writer.writerow([ 5, frequency5, PercFreq5,])
    writer.writerow([ 6, frequency6, PercFreq6,])
    print("file Created")

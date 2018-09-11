import numpy as np
import pandas as pd
import random

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

df = pd.read_csv("demseq.csv");
print(df)

#read csv into 3d array with each step of patient's bmi, age, and power level

step = 0;
patient = -1;
x = 0;
X = [];

seq = df['seq'].tolist();
pl = df['pl'].tolist();
age = df['age'].tolist();
bmi = df['bmi'].tolist();

while(x<192):
    if(seq[x] == 0):
        patient = patient+1;
        patientlist = [];
        print("new patient",x)
        x = x+1;
        while seq[x]>0:
            steparray = [pl[x],age[x],bmi[x]]
            patientlist.append(steparray);
            x = x+1;
            if x == 191:
                x=x+1;
                break;
        X.append(patientlist);
        
    
print(X)
   
y = []
 
for i in range(len(X)):
    j = random.randint(0,10);

    if j%2 == 0:
        y.append(1);
    else:
        y.append(0);
        
print(y)
    
    
X=np.array(X)
y=np.array(y)
print(X.shape)
print(y.shape)


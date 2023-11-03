import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from . import word_recog

def isBipolar(happyNum,sadNum):
 data=pd.DataFrame(pd.read_csv('D:\\mindshift\\backend\\backendMindshift\\mlModel\\bipolar_dataset - Sheet1.csv'))
 print(data.head()) 
 X=data[['goodWords','badWords','mapping']]
 Y=data[['isBipolar']]
 hWords=0
 bWords=0
 #plt.plot(X,Y) 
 model= LinearRegression()
 model.fit(X,Y)
 imp=np.array([30,25,6])
 imp=imp.reshape(-1,1)
 mapped=(min(happyNum,sadNum)+1)/2
 pred_state=model.predict([[happyNum,sadNum,mapped]])
 print(happyNum)
 print(sadNum)
 print(mapped)
 if pred_state>=0.5:
    print("Bipolar")
    return True
 else:
     return False
     print("Not Bipolar")    
 print((pred_state))
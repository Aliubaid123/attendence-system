import matplotlib.pyplot as plt
import numpy as np

y = np.array([1,10,1,5])
mylabls=["python ", "c++", "c" , " Ruby"]
mycolor=["black","red","blue","green"]
myexplode=[0,0.3,0.1,0]
plt.pie(y,labels=mylabls,explode=myexplode,shadow=True,colors=mycolor)
plt.legend(title="Four languages",loc="upper left")
plt.show() 

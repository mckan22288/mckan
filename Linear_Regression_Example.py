import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

x=[1,2,3,4,5,6]
y=[2.2, 3.5, 3.9, 5.1,6.4,7.3]
df=pd.DataFrame({'x':'x','y':'y'})
m=np.polyfit(df['x'],df['y'],1)
f=np.poly1d(m)
df.insert(2,'Fit',f(df[x]))
plt.scatter(df['x'],df['y'],coulor="blue")
plt.scatter(df['x'],df['Fit'],coulor="orange")
plt.title('Linear Regression Example')
plt.xlim([0,5])
plt.ylim([0,7])
plt.xlabel('x')
plt.ylabel('y')
plt.show()
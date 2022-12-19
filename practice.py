import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

y2 = np.array(['8','9','10','11','12','1','2','3','4'])
y1 = np.array([3,5,2,6,1,3,7,3,8])
y3 = np.array([1,5,3,5,5,8,1,3,9])

plt.subplot(2,2,1)
plt.plot(y2,y1, marker = 'o', linestyle = 'dashed')

plt.subplot(2,1,2)
plt.plot(y3, marker = 'o')

plt.subplot(2,3,3)
plt.plot(y2,marker = 'o')

plt.ylabel("Enjoyment Level")
plt.xlabel("Time Of Day") 
plt.grid()
plt.show()


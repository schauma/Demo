import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg

x = np.linspace(0,20,100)
plt.plot(x,np.sin(x))
plt.show()
A=np.array([[1,2],[3,4]])
linalg.inv(A)
print(A)
print(linalg.inv(A))